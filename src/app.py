import gradio as gr
from agent import run_agent
from langchain_core.messages import HumanMessage, AIMessage

def interact_with_agent(message, history):
    """
    Adapter function: Converts Gradio's history format to LangChain's format
    and calls the agent. Handles variable-length history items safely.
    """
    chat_history = []
    
    
    for turn in history:
        
        if isinstance(turn, (list, tuple)) and len(turn) >= 2:
            human_text = turn[0]
            ai_text = turn[1]
            
            if human_text:
                chat_history.append(HumanMessage(content=str(human_text)))
            if ai_text:
                chat_history.append(AIMessage(content=str(ai_text)))
            
    #get response
    response = run_agent(message, chat_history)
    
    return response

#UI
with gr.Blocks(theme=gr.themes.Base()) as demo:
    gr.Markdown("# 🤖 AI-Powered HR Assistant")
    gr.Markdown("Ask about employee details, leave balances, or interview questions.")
    
    #chat interface
    gr.ChatInterface(
        fn=interact_with_agent,
        examples=[
            "What is the leave balance for E12345?",
            "Generate interview questions for a Data Scientist.",
            "Who is employee E67890?"
        ]
    )

if __name__ == "__main__":
    demo.launch()