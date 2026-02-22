import os
from typing import TypedDict, List
from tavily import TavilyClient
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, END

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)
tavily = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))

class ResearchState(TypedDict):
    topic: str
    search_queries: List[str]
    research_data: List[str]
    final_report: str

def planner_node(state: ResearchState):
    topic = state.get("topic", "Technology")
    prompt = [HumanMessage(content=f"Generate 3 search queries for: {topic}. Return ONLY queries separated by commas.")]
    response = llm.invoke(prompt)
    queries = [q.strip() for q in response.content.split(",")]
    return {"search_queries": queries if queries else [topic]}

def researcher_node(state: ResearchState):
    queries = state.get("search_queries", [])
    all_research = []
    for query in queries:
        try:
            response = tavily.search(query=query, search_depth="basic", max_results=3)
            content = "\n".join([r['content'] for r in response['results']])
            all_research.append(f"Query: {query}\nData: {content}")
        except Exception as e:
            all_research.append(f"Query: {query}\nError: {str(e)}")
    return {"research_data": all_research}

def writer_node(state: ResearchState):
    topic = state.get("topic")
    data_str = "\n\n".join(state.get("research_data", []))
    if not data_str.strip():
        data_str = "No specific web data found. Write based on general knowledge."
    final_prompt = [HumanMessage(content=f"Write a professional markdown report on {topic} using this info:\n{data_str}")]
    response = llm.invoke(final_prompt)
    return {"final_report": response.content}

workflow = StateGraph(ResearchState)
workflow.add_node("planner", planner_node)
workflow.add_node("researcher", researcher_node)
workflow.add_node("writer", writer_node)
workflow.set_entry_point("planner")
workflow.add_edge("planner", "researcher")
workflow.add_edge("researcher", "writer")
workflow.add_edge("writer", END)
research_app = workflow.compile()
