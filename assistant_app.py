import openai
import streamlit as st
from prompts import WELCOME_PROMPT
from streamlit_chat import message
import os

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]


def generate_response(prompt, chat_history):
    try:
        # Use the system prompt for generating the response, but do not show it in the chat history
        messages = [{"role": "system", "content": WELCOME_PROMPT}] + chat_history + [{"role": "user", "content": prompt}]
        
        # Call the OpenAI API to generate a response based on the current chat context
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        # Extract the assistant's response from the OpenAI response
        assistant_response = response['choices'][0]['message']['content']
        
        # Update the chat history, including the user's message and the assistant's response
        updated_history = chat_history + [{"role": "user", "content": prompt}, {"role": "assistant", "content": assistant_response}]
        
        return assistant_response, updated_history
    
    except Exception as e:
        return f"Error: {e}", chat_history

# Streamlit UI to display chat history
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

# Create custom CSS to fix the input box at the bottom
st.markdown("""
    <style>
        .css-1s3wz2u {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 10px;
            background-color: white;
            z-index: 1000;
        }
        .css-1s3wz2u input {
            width: 100%;
        }
        .chat-container {
            max-height: 70vh;
            overflow-y: auto;
            padding-bottom: 80px;
        }
    </style>
""", unsafe_allow_html=True)

# Display chat history using Streamlit's chat_message for better UX
for message_item in st.session_state.chat_history:
    if message_item['role'] == "user":
        st.chat_message("user").markdown(message_item['content'])
    else:
        st.chat_message("assistant").markdown(message_item['content'])

# Create a placeholder for the input field (it will be fixed at the bottom)
input_placeholder = st.empty()

# Display the text input widget inside the placeholder (this keeps the input at the bottom)
with input_placeholder:
    user_input = st.text_input("Your message:", key="user_input", on_change=submit_message)

# Handle chat submission and response generation
if st.session_state.submit_chat:
    if user_input.strip():
        with st.spinner("Generating response..."):
            # Assuming generate_response is a function that returns a response and updated chat history
            response, updated_history = generate_response(user_input, st.session_state.chat_history)
        
        # Display the user input and assistant response in the chat UI
        st.session_state.chat_history = updated_history  # Update chat history
        st.session_state.submit_chat = False  # Reset submit flag