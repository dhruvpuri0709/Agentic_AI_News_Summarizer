from langchain_groq import ChatGroq
from src.AgenticAI.State.State import State

class ChatbotWithTools:
    """
    Chatbot logic enhanced with too integrations
    """
    
    def __init__(self,llm:ChatGroq,tools):
        self.llm = llm
        self.tools = tools
    
    def create_chatbot(self):
        """
        Creates a chatbot with tools
        """
        llm_with_tools = self.llm.bind_tools(self.tools)
        
        def chatbot_node(state:State):
            """
            Chatbot logic for processing the input state and returning a response

            Args:
                state (State): The state of the graph
            """
            return {"messages":[llm_with_tools.invoke(state["messages"])]}
        
        return chatbot_node
        