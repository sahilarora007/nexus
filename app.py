import streamlit as st
import streamlit.components.v1 as components
import html as _html
import time

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="NEXUS · Research Intelligence",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;900&family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500&display=swap');

/* ── Reset & Root ── */
:root {
    --bg:        #030712;
    --bg2:       #0a0f1e;
    --bg3:       #0f1729;
    --border:    #1e2d4a;
    --border2:   #2a3f66;
    --cyan:      #00e5ff;
    --cyan2:     #00b4d8;
    --green:     #00ff9d;
    --amber:     #ffb300;
    --red:       #ff3d5a;
    --purple:    #b06eff;
    --text:      #c8d8f0;
    --text-dim:  #5a7098;
    --text-mid:  #8baac8;
    --glow-cyan: 0 0 20px rgba(0,229,255,0.35);
    --glow-grn:  0 0 20px rgba(0,255,157,0.35);
}

html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Inter', sans-serif !important;
}

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse 80% 50% at 50% -20%, rgba(0,229,255,0.06) 0%, transparent 70%),
        radial-gradient(ellipse 60% 40% at 80% 80%, rgba(176,110,255,0.04) 0%, transparent 60%),
        var(--bg) !important;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"] { background: var(--bg2) !important; border-right: 1px solid var(--border) !important; }

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, [data-testid="stToolbar"] { display: none !important; }

/* ── Typography ── */
h1, h2, h3 { font-family: 'Orbitron', monospace !important; letter-spacing: 0.08em; }
code, pre { font-family: 'Space Mono', monospace !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: var(--bg2); }
::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 2px; }

/* ── Hero header ── */
.nexus-header {
    text-align: center;
    padding: 3rem 0 2rem;
    position: relative;
}
.nexus-logo {
    font-family: 'Orbitron', monospace;
    font-size: 3.2rem;
    font-weight: 900;
    letter-spacing: 0.25em;
    background: linear-gradient(135deg, #00e5ff 0%, #b06eff 60%, #00b4d8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: none;
    filter: drop-shadow(0 0 30px rgba(0,229,255,0.4));
}
.nexus-sub {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.4em;
    color: var(--text-dim);
    text-transform: uppercase;
    margin-top: 0.4rem;
}
.nexus-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--cyan), var(--purple), var(--cyan2), transparent);
    margin: 1.5rem auto;
    max-width: 600px;
    opacity: 0.5;
}

/* ── Input area ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: var(--bg2) !important;
    border: 1px solid var(--border2) !important;
    border-radius: 4px !important;
    color: var(--text) !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.85rem !important;
    padding: 0.75rem 1rem !important;
    transition: border-color 0.2s, box-shadow 0.2s;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--cyan) !important;
    box-shadow: 0 0 0 1px var(--cyan), var(--glow-cyan) !important;
    outline: none !important;
}

/* ── All buttons base ── */
.stButton > button {
    background: linear-gradient(135deg, rgba(0,229,255,0.12), rgba(176,110,255,0.12)) !important;
    border: 1px solid var(--border2) !important;
    border-radius: 4px !important;
    color: var(--text-mid) !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.7rem !important;
    font-weight: 400 !important;
    letter-spacing: 0.05em !important;
    padding: 0.4rem 0.8rem !important;
    cursor: pointer !important;
    transition: all 0.18s !important;
    width: 100% !important;
    white-space: normal !important;
    height: auto !important;
    min-height: 2.4rem !important;
    line-height: 1.4 !important;
}
.stButton > button:hover {
    border-color: var(--cyan) !important;
    color: var(--cyan) !important;
    background: rgba(0,229,255,0.1) !important;
    box-shadow: 0 0 12px rgba(0,229,255,0.2) !important;
    transform: translateY(-1px) !important;
}
.stButton > button:active { transform: translateY(0) !important; }
.stButton > button:disabled {
    opacity: 0.4 !important;
    cursor: not-allowed !important;
    transform: none !important;
}

/* ── Launch button override ── */
div[data-testid="column"]:last-child .stButton > button {
    background: linear-gradient(135deg, rgba(0,229,255,0.2), rgba(176,110,255,0.2)) !important;
    border: 1px solid var(--cyan) !important;
    color: var(--cyan) !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 0.72rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.2em !important;
    padding: 0.65rem 1rem !important;
    text-transform: uppercase !important;
}
div[data-testid="column"]:last-child .stButton > button:hover {
    background: linear-gradient(135deg, rgba(0,229,255,0.35), rgba(176,110,255,0.35)) !important;
    box-shadow: var(--glow-cyan) !important;
}

/* ── Thinking expander ── */
.thinking-block {
    background: rgba(176,110,255,0.05);
    border: 1px solid rgba(176,110,255,0.2);
    border-radius: 4px;
    padding: 0.75rem 1rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    line-height: 1.7;
    color: rgba(176,110,255,0.8);
    white-space: pre-wrap;
    word-break: break-word;
    margin-bottom: 0.5rem;
}

/* ── Iteration badge ── */
.iter-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(255,179,0,0.08);
    border: 1px solid rgba(255,179,0,0.3);
    border-radius: 3px;
    padding: 0.2rem 0.6rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.62rem;
    color: var(--amber);
    letter-spacing: 0.1em;
    margin-bottom: 0.6rem;
}

/* ── Pipeline progress ── */
.pipeline-progress {
    display: flex;
    align-items: center;
    gap: 0;
    margin: 1.5rem 0;
    position: relative;
}
.progress-step {
    flex: 1;
    text-align: center;
    position: relative;
}
.progress-step-dot {
    width: 10px; height: 10px;
    border-radius: 50%;
    margin: 0 auto 0.4rem;
    border: 1px solid #1e2d4a;
    background: #030712;
    transition: all 0.3s;
    position: relative;
    z-index: 1;
}
.progress-step-dot.active {
    border-color: #00e5ff;
    background: #00e5ff;
    box-shadow: 0 0 20px rgba(0,229,255,0.35);
    animation: dot-pulse 1.2s ease-in-out infinite;
}
.progress-step-dot.done {
    border-color: #00ff9d;
    background: #00ff9d;
}
@keyframes dot-pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.5); }
}
.progress-step-label {
    font-family: 'Orbitron', monospace;
    font-size: 0.5rem;
    letter-spacing: 0.15em;
    color: #5a7098;
    text-transform: uppercase;
    transition: color 0.3s;
}
.progress-step-label.active { color: #00e5ff; }
.progress-step-label.done { color: #00ff9d; }
.progress-connector {
    flex: 0.5;
    height: 1px;
    background: #1e2d4a;
    transition: background 0.3s;
    position: relative;
    top: -8px;
}
.progress-connector.done { background: #00ff9d; }
.progress-connector.active {
    background: linear-gradient(90deg, #00ff9d, #00e5ff);
}

/* ── Section label ── */
.section-label {
    font-family: 'Orbitron', monospace;
    font-size: 0.6rem;
    letter-spacing: 0.3em;
    color: var(--text-dim);
    text-transform: uppercase;
    margin-bottom: 1rem;
    display: flex; align-items: center; gap: 0.75rem;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--border), transparent);
}

/* ── Error box ── */
.error-box {
    background: rgba(255,61,90,0.08);
    border: 1px solid rgba(255,61,90,0.4);
    border-radius: 4px;
    padding: 1rem 1.25rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    color: var(--red);
}

/* ── Feedback score ── */
.feedback-score {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.25rem 0.75rem;
    border-radius: 3px;
    font-family: 'Orbitron', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.15em;
}
.score-high { background: rgba(0,255,157,0.1); border: 1px solid #00ff9d; color: #00ff9d; }
.score-mid { background: rgba(255,179,0,0.1); border: 1px solid #ffb300; color: #ffb300; }
.score-low { background: rgba(255,61,90,0.1); border: 1px solid #ff3d5a; color: #ff3d5a; }

/* ── Streamlit overrides ── */
[data-testid="stMarkdownContainer"] p { color: var(--text-mid); font-size: 0.85rem; }
.stSpinner > div { border-color: var(--cyan) transparent transparent !important; }

/* ── Final report ── */
.final-report-container {
    background: var(--bg2);
    border: 1px solid var(--cyan);
    border-radius: 8px;
    padding: 2rem;
    box-shadow: var(--glow-cyan), inset 0 0 60px rgba(0,229,255,0.02);
    position: relative;
    overflow: hidden;
    margin-top: 1.5rem;
}
.final-report-container::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--cyan), transparent);
    opacity: 0.6;
}
.final-report-label {
    font-family: 'Orbitron', monospace;
    font-size: 0.6rem;
    letter-spacing: 0.35em;
    color: var(--cyan);
    text-transform: uppercase;
    margin-bottom: 1.25rem;
    display: flex; align-items: center; gap: 0.5rem;
}
.final-report-text {
    font-family: 'Inter', sans-serif;
    font-size: 0.88rem;
    line-height: 1.9;
    color: var(--text);
    white-space: pre-wrap;
    word-break: break-word;
}
.typing-cursor {
    display: inline-block;
    width: 7px; height: 13px;
    background: #00e5ff;
    margin-left: 2px;
    vertical-align: middle;
    animation: blink 0.8s step-end infinite;
}
@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
</style>
""", unsafe_allow_html=True)

# ── Session state init ─────────────────────────────────────────────────────
for key, default in {
    "running": False,
    "topic_input": "",
    "agent_states": {
        "search":     {"status": "idle", "output": "", "thinking": None},
        "url_select": {"status": "idle", "output": "", "thinking": None},
        "scraper":    {"status": "idle", "output": "", "thinking": None},
        "writer":     {"status": "idle", "output": "", "thinking": None},
        "critic":     {"status": "idle", "output": "", "thinking": None},
    },
    "iterations": [],
    "final_report": None,
    "final_thinking": None,
    "error": None,
    "pipeline_done": False,
    "active_step": -1,
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# ── Header ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="nexus-header">
    <div class="nexus-logo">NEXUS</div>
    <div class="nexus-sub">Multi-Agent Research Intelligence System</div>
    <div class="nexus-divider"></div>
</div>
""", unsafe_allow_html=True)

# ── Examples ──────────────────────────────────────────────────────────────
EXAMPLES = [
    "Quantum computing breakthroughs 2025",
    "Impact of AI on software engineering jobs",
    "Latest advances in fusion energy",
    "State of autonomous vehicles 2025",
    "CRISPR gene editing in medicine",
    "The rise of agentic AI systems",
]

st.markdown('<div class="section-label">⬡ Quick start examples</div>', unsafe_allow_html=True)

cols = st.columns(len(EXAMPLES))
for i, ex in enumerate(EXAMPLES):
    with cols[i]:
        if st.button(ex, key=f"ex_{i}", use_container_width=True):
            st.session_state["topic_input"] = ex
            st.rerun()

# ── Input row ─────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
col_input, col_btn = st.columns([5, 1])

with col_input:
    topic = st.text_input(
        label="",
        value=st.session_state["topic_input"],
        placeholder="Enter a research topic…",
        label_visibility="collapsed",
        key="topic_field",
        disabled=st.session_state["running"],
    )

with col_btn:
    run_clicked = st.button(
        "▶  LAUNCH",
        disabled=st.session_state["running"],
        use_container_width=True,
    )

# ── Pipeline progress bar ──────────────────────────────────────────────────
STEPS = ["SEARCH", "SELECT", "SCRAPE", "WRITE", "CRITIQUE"]

def render_progress(active_step: int, done_steps: set):
    parts = []
    for i, s in enumerate(STEPS):
        dot_cls   = "done" if i in done_steps else ("active" if i == active_step else "")
        label_cls = "done" if i in done_steps else ("active" if i == active_step else "")
        parts.append(f"""
        <div class="progress-step">
            <div class="progress-step-dot {dot_cls}"></div>
            <div class="progress-step-label {label_cls}">{s}</div>
        </div>
        """)
        if i < len(STEPS) - 1:
            conn_cls = "done" if i in done_steps else ("active" if i == active_step - 1 else "")
            parts.append(f'<div class="progress-connector {conn_cls}"></div>')

    return f'<div class="pipeline-progress">{"".join(parts)}</div>'

# ── Helper: HTML escape ────────────────────────────────────────────────────
def _esc(text: str) -> str:
    """Escape text so it renders as plain text inside HTML."""
    return _html.escape(str(text) if text else "")

# ── Helper: render agent card via st.components (bypasses markdown parser) ──
CARD_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;900&family=Space+Mono:wght@400;700&display=swap');
*{box-sizing:border-box;margin:0;padding:0;}
body{background:transparent;font-family:'Space Mono',monospace;}
.agent-card{
    background:#0a0f1e;
    border:1px solid #1e2d4a;
    border-radius:6px;
    padding:1.1rem 1.4rem;
    margin:0 0 4px 0;
    position:relative;
    overflow:hidden;
}
.agent-card::before{
    content:'';position:absolute;top:0;left:0;
    width:3px;height:100%;background:#1e2d4a;
}
.agent-card.active{border-color:#00e5ff;box-shadow:0 0 20px rgba(0,229,255,0.25),inset 0 0 40px rgba(0,229,255,0.03);}
.agent-card.active::before{background:#00e5ff;}
.agent-card.done{border-color:rgba(0,255,157,0.4);box-shadow:0 0 15px rgba(0,255,157,0.1);}
.agent-card.done::before{background:#00ff9d;}
.agent-header{display:flex;align-items:center;gap:0.65rem;margin-bottom:0.7rem;}
.agent-icon{font-size:1rem;width:1.9rem;height:1.9rem;display:flex;align-items:center;justify-content:center;border-radius:4px;background:rgba(255,255,255,0.04);border:1px solid #1e2d4a;flex-shrink:0;}
.agent-name{font-family:'Orbitron',monospace;font-size:0.6rem;font-weight:600;letter-spacing:0.2em;color:#5a7098;text-transform:uppercase;}
.agent-card.active .agent-name{color:#00e5ff;}
.agent-card.done .agent-name{color:#00ff9d;}
.agent-status-badge{margin-left:auto;font-family:'Space Mono',monospace;font-size:0.58rem;letter-spacing:0.15em;padding:0.12rem 0.5rem;border-radius:2px;border:1px solid currentColor;text-transform:uppercase;}
.badge-idle{color:#5a7098;border-color:#1e2d4a;}
.badge-active{color:#00e5ff;border-color:#00e5ff;animation:pulse-badge 1.2s ease-in-out infinite;}
.badge-done{color:#00ff9d;border-color:#00ff9d;}
@keyframes pulse-badge{0%,100%{opacity:1;}50%{opacity:0.45;}}
.output-label{font-family:'Orbitron',monospace;font-size:0.52rem;letter-spacing:0.25em;color:#7a99c0;text-transform:uppercase;margin-bottom:0.4rem;}
.agent-output{background:#0b1220;border:1px solid #253a5e;border-radius:4px;padding:0.85rem 1.1rem;font-family:'Space Mono',monospace;font-size:0.72rem;line-height:1.8;color:#ddeeff;white-space:pre-wrap;word-break:break-word;max-height:520px;overflow-y:auto;}
.typing-cursor{display:inline-block;width:7px;height:13px;background:#00e5ff;margin-left:2px;vertical-align:middle;animation:blink 0.8s step-end infinite;}
@keyframes blink{0%,100%{opacity:1;}50%{opacity:0;}}
"""

def agent_card_html(icon: str, name: str, status: str, output: str) -> str:
    """Return a self-contained HTML document for use in st.components.v1.html()."""
    card_cls   = {"active": "active", "done": "done"}.get(status, "")
    badge_cls  = {"active": "badge-active", "done": "badge-done"}.get(status, "badge-idle")
    badge_txt  = {"active": "PROCESSING", "done": "COMPLETE"}.get(status, "STANDBY")
    cursor     = '<span class="typing-cursor"></span>' if status == "active" else ""

    out_html = ""
    if output:
        out_html = f"""
        <div class="output-label">Output</div>
        <div class="agent-output">{_esc(output)}{cursor}</div>"""
    elif status == "active":
        out_html = f"""
        <div class="output-label">Output</div>
        <div class="agent-output" style="color:#5a7098;font-style:italic;">Receiving data…{cursor}</div>"""

    return f"""<!DOCTYPE html>
<html><head><style>{CARD_CSS}</style></head>
<body>
<div class="agent-card {card_cls}">
  <div class="agent-header">
    <div class="agent-icon">{icon}</div>
    <div class="agent-name">{_esc(name)}</div>
    <div class="agent-status-badge {badge_cls}">{badge_txt}</div>
  </div>
  {out_html}
</div>
</body></html>"""

def card_height(output: str, status: str) -> int:
    """Estimate iframe height based on output length."""
    if not output:
        return 115 if status == "active" else 80
    lines = max(1, output.count("\n") + 1)
    chars = len(output)
    # 130px overhead (card chrome) + ~21px per line + extra for long text
    est = 130 + min(lines * 21 + chars // 45, 540)
    return min(est, 680)

def render_agent_card(icon, name, status, output, container=None):
    """Render an agent card using st.components.v1.html to avoid HTML injection issues."""
    html_doc = agent_card_html(icon, name, status, output)
    h = card_height(output, status)
    target = container if container else st
    target.components.v1.html(html_doc, height=h, scrolling=True)

# ── Run pipeline ────────────────────────────────────────────────────────────
if run_clicked and topic.strip():
    st.session_state["running"]      = True
    st.session_state["topic_input"]  = topic
    st.session_state["pipeline_done"] = False
    st.session_state["error"]        = None
    st.session_state["final_report"] = None
    st.session_state["final_thinking"] = None
    st.session_state["iterations"]   = []
    st.session_state["active_step"]  = -1
    st.session_state["agent_states"] = {k: {"status": "idle", "output": "", "thinking": None} for k in
        ["search", "url_select", "scraper", "writer", "critic"]}
    st.rerun()

# ── Live pipeline execution ─────────────────────────────────────────────────
if st.session_state["running"] and not st.session_state["pipeline_done"]:
    topic_val = st.session_state["topic_input"]

    prog_ph   = st.empty()
    ph_search = st.empty()
    ph_select = st.empty()
    ph_scrape = st.empty()
    iter_hdr  = st.empty()
    ph_writer = st.empty()
    ph_critic = st.empty()
    ph_final  = st.empty()

    done_steps: set = set()

    def render_all():
        s = st.session_state["agent_states"]
        prog_ph.markdown(render_progress(st.session_state["active_step"], done_steps), unsafe_allow_html=True)
        with ph_search.container():
            components.html(agent_card_html("🔍", "Search Agent",          s["search"]["status"],    s["search"]["output"]),    height=card_height(s["search"]["output"],    s["search"]["status"]),    scrolling=True)
        with ph_select.container():
            components.html(agent_card_html("🎯", "URL Selector Agent",    s["url_select"]["status"], s["url_select"]["output"]), height=card_height(s["url_select"]["output"], s["url_select"]["status"]), scrolling=True)
        with ph_scrape.container():
            components.html(agent_card_html("🕷", "Scraper · Compressor",  s["scraper"]["status"],   s["scraper"]["output"]),   height=card_height(s["scraper"]["output"],   s["scraper"]["status"]),   scrolling=True)

    def set_agent(name, status, output="", thinking=None):
        st.session_state["agent_states"][name] = {"status": status, "output": output, "thinking": thinking}

    try:
        from agents import build_scraper_agent, build_search_agent, writer_chain, critic_chain

        MAX_ITER = 2
        NUM_URLS = 3

        # ── STEP 1: SEARCH ──
        st.session_state["active_step"] = 0
        set_agent("search", "active")
        render_all()

        search_agent  = build_search_agent()
        search_result = search_agent.invoke({
            "messages": [("user", f"Find top {NUM_URLS} recent, reliable sources for: {topic_val}")]
        })
        raw_msg       = search_result["messages"][-1]
        search_out    = raw_msg.content if hasattr(raw_msg, "content") else str(raw_msg)
        search_think  = getattr(raw_msg, "additional_kwargs", {}).get("thinking")

        set_agent("search", "done", search_out, search_think)
        done_steps.add(0)
        render_all()

        # ── STEP 2: URL SELECT ──
        st.session_state["active_step"] = 1
        set_agent("url_select", "active")
        render_all()

        scraper_agent = build_scraper_agent()
        url_selection = scraper_agent.invoke({
            "messages": [("user", f"""
Select top {NUM_URLS} URLs.

Criteria:
- highly relevant
- trusted sources
- minimal noise

Return ONLY:
URL1:
URL2:
URL3:

Search Results:
{search_out[:800]}
""")]
        })
        raw_url   = url_selection["messages"][-1]
        url_out   = raw_url.content if hasattr(raw_url, "content") else str(raw_url)
        url_think = getattr(raw_url, "additional_kwargs", {}).get("thinking")

        set_agent("url_select", "done", url_out, url_think)
        done_steps.add(1)
        render_all()

        # ── STEP 3: SCRAPE ──
        st.session_state["active_step"] = 2
        set_agent("scraper", "active")
        render_all()

        scraped    = scraper_agent.invoke({
            "messages": [("user", f"""
Scrape these URLs and return ONLY key insights.

Rules:
- Max 10 bullets total
- No fluff
- Keep facts, numbers, claims
- Remove repetition

URLs:
{url_out}
""")]
        })
        raw_scrape    = scraped["messages"][-1]
        scraped_out   = raw_scrape.content if hasattr(raw_scrape, "content") else str(raw_scrape)
        scrape_think  = getattr(raw_scrape, "additional_kwargs", {}).get("thinking")

        set_agent("scraper", "done", scraped_out, scrape_think)
        done_steps.add(2)
        render_all()

        # ── STEP 4: WRITER + CRITIC LOOP ──
        st.session_state["active_step"] = 3
        iter_hdr.markdown('<div class="section-label">⬡ Writer · Critic Loop</div>', unsafe_allow_html=True)

        report = feedback = report_think = feedback_think = None

        for i in range(MAX_ITER):
            set_agent("writer", "active", "")
            set_agent("critic", "idle",   "")
            prog_ph.markdown(render_progress(3, done_steps), unsafe_allow_html=True)
            with ph_writer.container():
                components.html(agent_card_html("✍️", f"Writer Agent — Iteration {i+1}", "active", ""), height=110, scrolling=True)
            with ph_critic.container():
                components.html(agent_card_html("🧠", f"Critic Agent — Iteration {i+1}",  "idle",   ""), height=75,  scrolling=True)

            writer_raw = writer_chain.invoke({
                "topic":    topic_val,
                "research": scraped_out,
                "feedback": feedback if feedback else "None",
            })
            if hasattr(writer_raw, "content"):
                report_think = getattr(writer_raw, "additional_kwargs", {}).get("thinking")
                report = writer_raw.content
            else:
                report = str(writer_raw)
                report_think = None

            set_agent("writer", "done", report, report_think)
            with ph_writer.container():
                components.html(agent_card_html("✍️", f"Writer Agent — Iteration {i+1}", "done", report),
                                height=card_height(report, "done"), scrolling=True)

            # Critic
            st.session_state["active_step"] = 4
            set_agent("critic", "active")
            prog_ph.markdown(render_progress(4, done_steps), unsafe_allow_html=True)
            with ph_critic.container():
                components.html(agent_card_html("🧠", f"Critic Agent — Iteration {i+1}", "active", ""), height=110, scrolling=True)

            critic_raw = critic_chain.invoke({"report": report})
            if hasattr(critic_raw, "content"):
                feedback_think = getattr(critic_raw, "additional_kwargs", {}).get("thinking")
                feedback = critic_raw.content
            else:
                feedback = str(critic_raw)
                feedback_think = None

            set_agent("critic", "done", feedback, feedback_think)
            with ph_critic.container():
                components.html(agent_card_html("🧠", f"Critic Agent — Iteration {i+1}", "done", feedback),
                                height=card_height(feedback, "done"), scrolling=True)

            st.session_state["iterations"].append({
                "i": i + 1,
                "report":           report,
                "report_thinking":  report_think,
                "feedback":         feedback,
                "feedback_thinking": feedback_think,
            })

            done_steps.add(3)
            done_steps.add(4)
            prog_ph.markdown(render_progress(4, done_steps), unsafe_allow_html=True)

            if "Score: 9" in str(feedback) or "Score: 10" in str(feedback):
                break
            else:
                st.session_state["active_step"] = 3
                done_steps.discard(3)
                done_steps.discard(4)

        # ── FINAL ── stream report with typewriter effect
        st.session_state["final_report"]  = report
        st.session_state["final_thinking"] = report_think
        st.session_state["pipeline_done"] = True
        st.session_state["running"]       = False
        prog_ph.markdown(render_progress(-1, {0, 1, 2, 3, 4}), unsafe_allow_html=True)

        safe_full = _esc(report or "")
        CHUNK = 10
        for idx in range(0, len(safe_full) + CHUNK, CHUNK):
            chunk = safe_full[:idx]
            ph_final.markdown(f"""
            <div class="final-report-container">
                <div class="final-report-label">⬡ &nbsp; Final Intelligence Report</div>
                <div class="final-report-text">{chunk}<span class="typing-cursor"></span></div>
            </div>
            """, unsafe_allow_html=True)
            time.sleep(0.011)

        ph_final.markdown(f"""
        <div class="final-report-container">
            <div class="final-report-label">⬡ &nbsp; Final Intelligence Report</div>
            <div class="final-report-text">{safe_full}</div>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.session_state["error"]   = str(e)
        st.session_state["running"] = False
        st.rerun()

# ── Show error ────────────────────────────────────────────────────────────
if st.session_state.get("error"):
    st.markdown(f'<div class="error-box">⚠ Pipeline Error: {_esc(st.session_state["error"])}</div>',
                unsafe_allow_html=True)

# ── Show completed results on re-render ──────────────────────────────────
if st.session_state["pipeline_done"] and not st.session_state["running"]:
    s = st.session_state["agent_states"]

    st.markdown(render_progress(-1, {0, 1, 2, 3, 4}), unsafe_allow_html=True)

    # Search
    components.html(agent_card_html("🔍", "Search Agent",         s["search"]["status"],    s["search"]["output"]),    height=card_height(s["search"]["output"],    s["search"]["status"]),    scrolling=True)
    if s["search"].get("thinking"):
        with st.expander("🧠 Search Agent — Model Thinking", expanded=False):
            st.markdown(f'<div class="thinking-block">{_esc(s["search"]["thinking"])}</div>', unsafe_allow_html=True)

    # URL Selector
    components.html(agent_card_html("🎯", "URL Selector Agent",   s["url_select"]["status"], s["url_select"]["output"]), height=card_height(s["url_select"]["output"], s["url_select"]["status"]), scrolling=True)
    if s["url_select"].get("thinking"):
        with st.expander("🧠 URL Selector — Model Thinking", expanded=False):
            st.markdown(f'<div class="thinking-block">{_esc(s["url_select"]["thinking"])}</div>', unsafe_allow_html=True)

    # Scraper
    components.html(agent_card_html("🕷", "Scraper · Compressor", s["scraper"]["status"],   s["scraper"]["output"]),   height=card_height(s["scraper"]["output"],   s["scraper"]["status"]),   scrolling=True)
    if s["scraper"].get("thinking"):
        with st.expander("🧠 Scraper — Model Thinking", expanded=False):
            st.markdown(f'<div class="thinking-block">{_esc(s["scraper"]["thinking"])}</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-label">⬡ Writer · Critic Loop</div>', unsafe_allow_html=True)

    for it in st.session_state["iterations"]:
        fb = it["feedback"] or ""
        score_cls = ("score-high" if ("Score: 9" in fb or "Score: 10" in fb)
                     else "score-mid" if ("Score: 7" in fb or "Score: 8" in fb)
                     else "score-low")
        score_txt = next((f"Score: {n}" for n in range(10, 0, -1) if f"Score: {n}" in fb), "Score: —")

        st.markdown(f'<div class="iter-badge">↺ &nbsp; Iteration {it["i"]}</div>', unsafe_allow_html=True)

        components.html(agent_card_html("✍️", f"Writer Agent — Iteration {it['i']}", "done", it["report"]),
                        height=card_height(it["report"], "done"), scrolling=True)
        if it.get("report_thinking"):
            with st.expander(f"🧠 Writer Iter {it['i']} — Model Thinking", expanded=False):
                st.markdown(f'<div class="thinking-block">{_esc(it["report_thinking"])}</div>', unsafe_allow_html=True)

        col_crit, col_score = st.columns([4, 1])
        with col_crit:
            components.html(agent_card_html("🧠", f"Critic Agent — Iteration {it['i']}", "done", it["feedback"]),
                            height=card_height(it["feedback"], "done"), scrolling=True)
            if it.get("feedback_thinking"):
                with st.expander(f"🧠 Critic Iter {it['i']} — Model Thinking", expanded=False):
                    st.markdown(f'<div class="thinking-block">{_esc(it["feedback_thinking"])}</div>', unsafe_allow_html=True)
        with col_score:
            st.markdown(f'<br><div class="feedback-score {score_cls}">⬡ {score_txt}</div>', unsafe_allow_html=True)

    final = st.session_state["final_report"]
    if final:
        st.markdown(f"""
        <div class="final-report-container">
            <div class="final-report-label">⬡ &nbsp; Final Intelligence Report</div>
            <div class="final-report-text">{_esc(final)}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.session_state.get("final_thinking"):
            with st.expander("🧠 Final Report — Model Thinking", expanded=False):
                st.markdown(f'<div class="thinking-block">{_esc(st.session_state["final_thinking"])}</div>',
                            unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:3rem 0 1.5rem;font-family:'Space Mono',monospace;
font-size:0.62rem;letter-spacing:0.18em;color:#5a7098;">
Made with <span style="color:#ff3d5a;">♥</span> by <span style="color:#00e5ff;letter-spacing:0.25em;">SAHIL ARORA</span>
</div>
""", unsafe_allow_html=True)