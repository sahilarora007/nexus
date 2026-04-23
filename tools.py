from langchain.tools import tool
import requests
import rich
from tavily import TavilyClient
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from rich import print
import os

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
    """
    Search the web and return structured top results.
    Output is compact and optimized for LLM reasoning.
    """
    try:
        response = tavily.search(
            query=query,
            max_results=5,
            search_depth="advanced"
        )

        results = []
        for i, r in enumerate(response.get("results", []), 1):
            results.append(
                f"[{i}] {r['title']}\n"
                f"{r['url']}\n"
                f"{r['content'][:200]}"
            )

        return "\n\n".join(results)

    except Exception as e:
        return f"ERROR: search failed | {str(e)}"

@tool
def scrape_url(url: str) -> str:
    """
    Extract main readable content from a webpage.
    Removes noise and returns concise plain text.
    """
    try:
        resp = requests.get(
            url,
            timeout=12,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/124.0.0.0 Safari/537.36"
                ),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
                # Explicitly exclude brotli — requests does NOT natively decompress
                # brotli, which causes the garbled binary output.
                # gzip + deflate are handled automatically by requests.
                "Accept-Encoding": "gzip, deflate",
            },
            stream=False,
        )

        if resp.status_code != 200:
            return f"ERROR: HTTP {resp.status_code} for {url}"

        # ── Robust charset detection ──────────────────────────────────────
        # resp.apparent_encoding uses charset_normalizer (bundled with requests >=2.26)
        # which is far more reliable than trusting the Content-Type charset.
        detected_enc = resp.apparent_encoding or "utf-8"
        try:
            html_text = resp.content.decode(detected_enc, errors="replace")
        except (LookupError, UnicodeDecodeError):
            html_text = resp.content.decode("utf-8", errors="replace")

        # ── Binary content guard ──────────────────────────────────────────
        # If more than 30% of the first 2000 chars are non-printable, the
        # page is binary/still-compressed — skip it to avoid garbled output.
        sample = html_text[:2000]
        if sample:
            printable_ratio = sum(
                1 for c in sample if c.isprintable() or c in "\n\r\t"
            ) / len(sample)
        else:
            printable_ratio = 0.0

        if printable_ratio < 0.70:
            return (
                f"ERROR: Received binary/encoded content from {url}. "
                "The page may require JavaScript or block automated access."
            )

        # ── Parse & clean ─────────────────────────────────────────────────
        soup = BeautifulSoup(html_text, "html.parser")

        # Remove noisy / non-content tags
        for tag in soup(["script", "style", "nav", "footer",
                         "header", "aside", "form", "noscript",
                         "svg", "img", "button", "input", "iframe"]):
            tag.decompose()

        raw_text = soup.get_text(separator="\n", strip=True)

        # Collapse blank lines — keep structure readable
        lines = [ln.strip() for ln in raw_text.splitlines() if ln.strip()]
        text = "\n".join(lines)

        # Strip residual control / non-printable characters
        cleaned = "".join(c for c in text if c.isprintable() or c in "\n\t")

        if not cleaned.strip():
            return f"ERROR: No readable text extracted from {url}"

        return cleaned[:3000]

    except requests.exceptions.Timeout:
        return f"ERROR: Request timed out for {url}"
    except requests.exceptions.ConnectionError:
        return f"ERROR: Could not connect to {url}"
    except Exception as e:
        return f"ERROR: scraping failed | {str(e)}"