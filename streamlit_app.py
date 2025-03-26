import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = ""  # 🔒 Replace this with your actual API key

# Function to get bot response using OpenAI
def get_bot_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can also use "gpt-4" if available
        messages=[
            {"role": "system", "content": "You are a friendly fast food chatbot. Help users with questions, recommendations, and orders."},
            {"role": "user", "content": user_input}
        ]
    )
    return response['choices'][0]['message']['content']

# Streamlit App UI
st.title("AI Chatbot")

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = ""

# Display the chat history
st.text_area("Chat History", st.session_state['chat_history'], height=300, key="chat_display")

# Input for new message
new_message = st.text_input("You:", "")

# Handle the send button
if st.button("Send"):
    if new_message:
        # Add user message
        st.session_state['chat_history'] += f"\nYou: {new_message}"

        # Get bot response
        bot_response = get_bot_response(new_message)

        # Add bot response
        st.session_state['chat_history'] += f"\nBot: {bot_response}"

        # Refresh UI to show new messages
        st.experimental_rerun()

# Reset chat
if st.button("Reset Chat"):
    st.session_state['chat_history'] = ""
    st.experimental_rerun()
