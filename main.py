import os
from openai import OpenAI
import gradio as gr
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with minimal configuration
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

# System prompt defining the assistant's role and behavior
SYSTEM_PROMPT = """
You are a professional Thai female financial assistant. Begin the conversation by introducing yourself and ask users the following questions one by one in Thai.

คุณอายุเท่าไหร่

สไตล์การลงทุนที่ผ่านมาของคุณเป็นแบบไหน (ถ้ายังไม่เคยลงทุน ลองเลือกแบบที่ชอบดูสิ)

  1. กล้าได้กล้าเสีย ถึงเวลาต้องยอมตัดขาดทุน แล้วไปลุยใหม่ สร้างกำไรสูงๆ

  2. ช้าแต่ชัวร์ ได้น้อยดีกว่าไม่ได้ แต่ไม่อยากขาดทุน

  3. แล้วแต่จังหวะ แล้วแต่โอกาส บางทีก็เสี่ยงบ้าง มีกำไรพอประมาณ

ปัจจุบันคุณมีรายได้ต่อเดือนเท่าไหร่

ปัจจุบันคุณมีค่าใช้จ่ายต่อเดือนเท่าไหร่
"""

def chat_with_gpt(prompt, chat_history):
    """
    Function to handle chat interaction with GPT model
    """
    # Add user's message to chat history
    chat_history.append({"role": "user", "content": prompt})
    
    try:
        # Get response from OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_history
        )
        
        # Extract the assistant's reply
        reply = response.choices[0].message.content
        
        # Add assistant's reply to chat history
        chat_history.append({"role": "assistant", "content": reply})
        
        return reply, chat_history
    
    except Exception as e:
        error_message = f"Error occurred: {str(e)}"
        print(error_message)  # Add logging
        return error_message, chat_history

def create_chat_interface():
    """
    Function to create and configure the Gradio interface
    """
    with gr.Blocks() as chat_app:
        gr.Markdown("""# Thai Financial Assistant Chat
Chat with your personal Thai financial advisor powered by GPT-3.5
""")
        
        # Initialize chat history with system prompt
        chat_history = gr.State([
            {"role": "system", "content": SYSTEM_PROMPT}
        ])
        
        with gr.Row():
            with gr.Column():
                user_input = gr.Textbox(
                    placeholder="พิมพ์ข้อความของคุณที่นี่...",
                    label="Your Message",
                    lines=2
                )
                submit_btn = gr.Button("Send", variant="primary")
            
            with gr.Column():
                output_box = gr.Textbox(
                    placeholder="คำตอบจะปรากฎที่นี่...",
                    label="Response",
                    lines=10,
                    interactive=False
                )
        
        # Set up event handler for the submit button
        submit_btn.click(
            fn=chat_with_gpt,
            inputs=[user_input, chat_history],
            outputs=[output_box, chat_history]
        )
        
        # Clear input after sending
        submit_btn.click(lambda: "", None, user_input)
    
    return chat_app

def main():
    """
    Main function to run the application
    """
    # Check for API key
    if not os.getenv('OPENAI_API_KEY'):
        raise EnvironmentError("OpenAI API key not found. Please set OPENAI_API_KEY in your .env file.")
    
    # Create and launch the interface
    chat_app = create_chat_interface()
    chat_app.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    main()