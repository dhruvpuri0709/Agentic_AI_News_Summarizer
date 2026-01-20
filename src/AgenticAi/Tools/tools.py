from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools import WikipediaQueryRun, ArxivQueryRun
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper
from langgraph.prebuilt import ToolNode

def get_tools() -> list:
    """
    Returns the list of tools to be used in the chatbot

    Returns:
        list: The list of tools
    """
    web_search = TavilySearchResults(max = 3)
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(top_k_results=3,doc_content_chars_max=3000))
    arxiv = ArxivQueryRun(api_wrapper=ArxivAPIWrapper(top_k_results=3, doc_content_chars_max=3000))
    
    return [web_search,wikipedia,arxiv]

def create_tool_node(tools:list) -> ToolNode:
    """
    Creates and returns a tool node for the graph

    Args:
        tools (list): The list of tools

    Returns:
        ToolNode: The newly created toolnode
    """
    return ToolNode(tools)

