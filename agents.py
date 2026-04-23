from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct", api_key=os.getenv("GROQ_API_KEY"))
#  1st agent 
def build_search_agent():
    return create_agent(
        model = llm,
        tools = [web_search]
    )

# 2nd agent
def build_scraper_agent():
    return create_agent(
        model = llm,
        tools = [scrape_url]
    )

# writer chain
writer_prompt = ChatPromptTemplate.from_messages([
    ("system", 
     "You are a top-tier research analyst. Your writing is concise, sharp, and insight-dense. You prioritize clarity, speed of understanding, and actionable value."),
    
    ("human", """Create a concise, high-impact research brief on the topic below.

Topic: {topic}

Research Provided:
{research}

Output Requirements:
- make sure the news you are giving is very very latest, if not then search again and give the latest news.
- Assume the reader is a busy founder or executive.
- Keep the entire response tight and scannable
- Avoid long paragraphs, prefer bullets and short sections
- No fluff, no repetition, no generic statements

Structure:

1.(3–5 bullets)
- Most important insights
- Must be immediately useful

2. Key Insights
- 4–6 bullets max
- Each bullet:
  • One strong insight
  • Brief supporting detail (data/example if available)
  • Why it matters

3. Implications / Actions
- What should the reader do with this?
- Clear, practical, decision-oriented bullets

4. Risks / Limitations
- 2–3 concise bullets
- Highlight uncertainty, downsides, or gaps

5. Sources
- Clean bullet list of URLs from the research
- Do not invent sources
- mention date of every source, everything you used.

Writing Style:
- Crisp, direct, and professional
- Prioritize insight over explanation
- Every line should add value
- Write as if the reader has only 30 seconds
"""),
])

writer_chain = writer_prompt | llm | StrOutputParser()

critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "Strict editor. Maximize clarity, brevity, and actionable insight. Remove fluff."),
    
    ("human", """Review and improve:

{report}

Return ONLY:

Score: X/10

Strengths:
- max 3 bullets

Issues:
- max 5 bullets, specific

Fix:
- max 5 bullets, actionable

Rewrite:
- shorter, clearer, more actionable version

Rules:
- be concise
- no repetition
- cut filler.
"""),
])

critic_chain = critic_prompt | llm | StrOutputParser()