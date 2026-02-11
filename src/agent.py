import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from tools import get_employee_details, check_leave_balance, generate_interview_questions


load_dotenv()


if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found in .env file")

#initialize the Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0
)

#define tools
#mapping
available_tools = {
    "get_employee_details": get_employee_details,
    "check_leave_balance": check_leave_balance,
    "generate_interview_questions": generate_interview_questions
}

# tools binding
llm_with_tools = llm.bind_tools(list(available_tools.values()))

SYSTEM_PROMPT = """
You are an intelligent HR Assistant.
1. Always check the conversation history for context.
2. If a user asks a question like "check leave balance" but doesn't provide an Employee ID, look at the previous messages to see if they already mentioned an ID (e.g., "E12345").
3. If you find the ID in the history, use it automatically. Do not ask for it again.
"""



#agent logic 
def run_agent(user_input: str, chat_history: list):
    """
    Processes user input, handles tool calls, and returns the final response.
    
    Args:
        user_input (str): The user's question.
        chat_history (list): List of previous messages in LangChain format.
        
    Returns:
        str: The assistant's final answer.
    """

    chat_history.insert(0, SystemMessage(content=SYSTEM_PROMPT))

    #add user message to history 
    chat_history.append(HumanMessage(content=user_input))
    
    #see if the model wants to call a tool 
    response = llm_with_tools.invoke(chat_history)
    chat_history.append(response)

    # check if there is any tool calls 
    if response.tool_calls:
        
        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]
            tool_call_id = tool_call["id"]
            
            # run the apropriate tool 
            tool_function = available_tools.get(tool_name)
            if tool_function:
                # capture the output 
                tool_result = tool_function(**tool_args)
                
                #feed the result to the model 
                tool_message = ToolMessage(
                    content=str(tool_result),
                    tool_call_id=tool_call_id,
                    name=tool_name
                )
                chat_history.append(tool_message)
            
        #get the natural language response 
        final_response = llm_with_tools.invoke(chat_history)
        chat_history.append(final_response)
        return final_response.content
    
    # if no tools are called return the text response 
    return response.content