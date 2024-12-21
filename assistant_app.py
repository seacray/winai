import openai
import gradio as gr



openai.api_key = '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'


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
def start_new_chat():
    """Function to reset the chat history for a new session."""
    return "", []  # Return empty response and reset history

# Define the Gradio interface
with gr.Blocks() as chat_app:
    gr.Markdown("""# Chat Completion App
Interact with OpenAI's GPT-based model in a chat format.
""")

    chat_history = gr.State([])  # To store chat history

    with gr.Row():
        with gr.Column():
            user_input = gr.Textbox(
                placeholder="Type your message here...",
                label="Your Message"
            )
            submit_btn = gr.Button("Send")
            new_chat_btn = gr.Button("New Chat", variant="secondary")

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

    new_chat_btn.click(
        fn=start_new_chat,
        inputs=[],
        outputs=[output_box, chat_history]
    )

if __name__ == "__main__":
    chat_app.launch()