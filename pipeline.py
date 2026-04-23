from langgraph.graph import state
from agents import build_scraper_agent, build_search_agent, writer_chain, critic_chain

def run_research_pipeline(topic: str) -> dict:
    
    state = {}

    # Step 1: Search
    print("\n" + "="*50)
    print("Step 1 - Search agent is working...")
    print("="*50)

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [("user", f"Find recent, reliable sources for: {topic}")]
    })

    state["search_results"] = search_result["messages"][-1].content
    print("\nSearch results:\n", state["search_results"])


    # Step 2: Scraper / Reader
    print("\n" + "="*50)
    print("Step 2 - Scraper agent is working...")
    print("="*50)

    scraper_agent = build_scraper_agent()

    scraper_result = scraper_agent.invoke({
        "messages": [("user",
            f"""Select best URL for "{topic}"

    Criteria:
    - relevant
    - high value
    - no spam

    Search Results:
    {state['search_results'][:600]}

    Return:
    URL:
    Why: 1 line"""
        )]
    })

    state['scraped_content'] = scraper_result['messages'][-1].content
    print("\nScraped content:\n", state['scraped_content'])

    # writer agent
    print("\n" + "="*50)
    print("Step 3 - Writer agent is working...")
    print("="*50)

    research_combined = (
        f"SEARCH RESULTS: \n {state['search_results']}"
        f"\n\nSCRAPED CONTENT: \n {state['scraped_content']}"
    )
    
    
    
    
    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })
    print("\n Final Report:\n", state["report"])

    # critic report
    print("\n" + "="*50)
    print("Step 4 - Critic agent is working...")
    print("="*50)

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })
    print("\nFeedback:\n", state["feedback"])

    return state

if __name__ == "__main__":
    topic = input("Enter topic for extensive research: ")
    result = run_research_pipeline(topic)