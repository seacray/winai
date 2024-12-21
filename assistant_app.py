import openai
import gradio as gr
import os 
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 

openai.api_key = os.environ["OPENAI_API_KEY"]

system_prompt="""
ํYou are a professional Thai female financial assistant. Begin the conversation by introducing yourself and ask users following questions one by one in Thai.

คุณอายุเท่าไหร่

สไตล์การลงทุนที่ผ่านมาของคุณเป็นแบบไหน (ถ้ายังไม่เคยลงทุน ลองเลือกแบบที่ชอบดูสิ)

  1. กล้าได้กล้าเสีย ถึงเวลาต้องยอมตัดขาดทุน แล้วไปลุยใหม่ สร้างกำไรสูงๆ

  2. ช้าแต่ชัวร์ ได้น้อยดีกว่าไม่ได้ แต่ไม่อยากขาดทุน

  3. แล้วแต่จังหวะ แล้วแต่โอกาส บางทีก็เสี่ยงบ้าง มีกำไรพอประมาณ

ปัจจุบันคุณมีรายได้ต่อเดือนเท่าไหร่

ปัจจุบันคุณมีค่าใช้จ่ายต่อเดือนเท่าไหร่
"""

def chat_with_gpt(prompt, chat_history):
    # Append the user input to the chat history
    chat_history.append({"role": "user", "content": prompt})

    try:
        # Send the chat history to OpenAI for a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_history
        )

        # Extract the assistant's reply
        reply = response["choices"][0]["message"]["content"]

        # Append the assistant's reply to the chat history
        chat_history.append({"role": "assistant", "content": reply})

        return reply, chat_history

    except openai.error.OpenAIError as e:
        return f"Error: {str(e)}", chat_history


    # Define the Gradio interface
with gr.Blocks() as chat_app:
    gr.Markdown("""# Chat Completion App
Interact with OpenAI's GPT-based model in a chat format.
""")

    chat_history = gr.State([
        {"role": "system", "content": system_prompt}
    ])  # System prompt sets the context for the assistant

    with gr.Row():
        with gr.Column():
            user_input = gr.Textbox(
                placeholder="Type your message here...",
                label="Your Message"
            )
            submit_btn = gr.Button("Send")

        with gr.Column():
            output_box = gr.Textbox(
                placeholder="The model's response will appear here.",
                label="Response",
                lines=10,
                interactive=False
            )

    # Define the interaction between components
    submit_btn.click(
        fn=chat_with_gpt,
        inputs=[user_input, chat_history],
        outputs=[output_box, chat_history]
    )


if __name__ == "__main__":
    chat_app.launch()
