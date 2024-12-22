import openai
import streamlit as st
from prompts import WELCOME_PROMPT
from streamlit_chat import message
import os

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]


def generate_response(prompt, chat_history):
    # try:
        # Create the complete chat messages including the system prompt and user's message
    messages = [{"role": "system", "content": WELCOME_PROMPT}] + chat_history + [{"role": "user", "content": prompt}]
    
    # Call the OpenAI API to generate a response based on the current chat context
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    # Extract the assistant's response from the OpenAI response
    assistant_response = response['choices'][0]['message']['content']
    
    # Append the assistant's response to the chat history
    updated_history = messages + [{"role": "assistant", "content": assistant_response}]
    
    return assistant_response, updated_history
    
    # except Exception as e:
    #     return f"Error: {e}", chat_history

# Initialize Streamlit app
st.title("💡 Winai Robo-Advisor for K-Wealth Plus")
st.write("Your personalized financial planning assistant.")

# Initialize chat history and input field in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if 'submit_chat' not in st.session_state:
    st.session_state.submit_chat = False

# Function to handle submission
def submit_message():
    st.session_state.submit_chat = True

# Display the text input widget
user_input = st.text_input("Your message:", key="user_input", on_change=submit_message)

# Handle chat submission and response generation
if st.session_state.submit_chat:
    if user_input.strip():
        with st.spinner("Generating response..."):
            # Assuming generate_response is a function that returns a response and updated chat history
            response, updated_history = generate_response(user_input, st.session_state.chat_history)
        
        # Update session state with the new chat history and reset the input field
        st.session_state.chat_history = updated_history
        st.session_state.submit_chat = False  # Reset submit flag

# Display chat history
for message_item in st.session_state.chat_history:
    if message_item['role'] == "user":
        st.write(f"User: {message_item['content']}")
    else:
        st.write(f"Bot: {message_item['content']}")