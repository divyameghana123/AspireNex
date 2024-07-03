import streamlit as st

data = {
    "hi": "Hi there! I'm a friendly chatbot here to assist you!",
    "hello": "Hello! How can I help you today?",
    "what is your name": "I'm just a chatbot, so I don't have a name, but you can call me ChatBot.",
    "where are you from": "I'm from the digital world, always ready to chat!",
    "how are you": "I'm just a chatbot, but I'm here to assist you.",
    "do you have any hobbies or interests?": "I'm always busy helping users, so my hobby is chatting with people like you!",
    "what did you eat today?": "I don't eat, but I can help you find delicious recipes and food-related information.",
    "what's your favorite color?": "I'm a chatbot, so I don't have personal preferences for colors.",
    "do you enjoy listening to music?": "I can't listen to music, but I'm here to chat about it!",
    "bye": "Bye! Take care and have a great day!",
}

def get_response(user_input):
    for pattern, response in data.items():
        if pattern in user_input.lower():
            return response
    return "I'm sorry, I didn't understand that. Can you please rephrase your sentence?"

st.title("Simple Chatbot")
st.write("Hi! I'm a simple chatbot. I'm here to assist you!")

if 'messages' not in st.session_state:
    st.session_state.messages = []

with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("You: ")
    submit_button = st.form_submit_button(label='Send')

if submit_button and user_input:
    response = get_response(user_input)
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Chatbot", response))

for sender, message in st.session_state.messages:
    if sender == "You":
        st.write(f"**{sender}**: {message}")
    else:
        st.write(f"**{sender}**: {message}")
        
if user_input.lower() == 'bye':
    st.session_state.messages = []
    st.write("Chatbot: Goodbye! Have a great day!")
