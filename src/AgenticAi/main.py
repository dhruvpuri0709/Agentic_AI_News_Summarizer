from src.AgenticAI.UI.streamlit.loadui import LoadStreamlitUI
import streamlit as st

def load_agentic_ai_app():
    """
    Loads and runs the LangGraph agentic ai application with streamlit UI.
    This function initilaizes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness
    
    """
    
    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()
    
    if not user_input:
        st.error("Error: Failed to load user input section from the UI")
        return
    
    user_message = st.chat_input("Enter your message:")
    
    
            
    