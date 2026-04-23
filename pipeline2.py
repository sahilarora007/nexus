from agents import build_scraper_agent, build_search_agent, writer_chain, critic_chain

MAX_ITER = 2
NUM_URLS = 3

def run_research_pipeline(topic: str) -> dict:

    state = {}

    # STEP 1: SEARCH
    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [("user", f"Find top {NUM_URLS} recent, reliable sources for: {topic}")]
    })

    state["search_results"] = search_result["messages"][-1].content


    # STEP 2: SELECT BEST URLS
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
{state["search_results"][:800]}
""")]
    })

    state["selected_urls"] = url_selection["messages"][-1].content


    # STEP 3: SCRAPE + COMPRESS (IMPORTANT CHANGE)
    scraped = scraper_agent.invoke({
        "messages": [("user", f"""
Scrape these URLs and return ONLY key insights.

Rules:
- Max 10 bullets total
- No fluff
- Keep facts, numbers, claims
- Remove repetition

URLs:
{state["selected_urls"]}
""")]
    })

    state["scraped_content"] = scraped["messages"][-1].content


    # STEP 4: WRITER + CRITIC LOOP
    report = None
    feedback = None

    for i in range(MAX_ITER):

        report = writer_chain.invoke({
            "topic": topic,
            "research": state["scraped_content"],   # 👈 direct, compressed input
            "feedback": feedback if feedback else "None"
        })

        feedback = critic_chain.invoke({
            "report": report
        })

        print(f"\nIteration {i+1} Feedback:\n", feedback)

        # early stop
        if "Score: 9" in str(feedback) or "Score: 10" in str(feedback):
            break


    state["final_report"] = report
    state["final_feedback"] = feedback

    return state


if __name__ == "__main__":
    topic = input("Enter topic: ")
    result = run_research_pipeline(topic)

    print("\n" + "="*50)
    print("FINAL REPORT")
    print("="*50)
    print(result["final_report"])