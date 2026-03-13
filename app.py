import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage

from bot_logic import TalentScoutBot
from database import save_candidate_data
from prompts import INITIAL_GREETING_TRIGGER

load_dotenv()

st.set_page_config(
    page_title="TalentScout Hiring Assistant",
    page_icon="🤖",
    layout="centered",
)

st.title("TalentScout Hiring Assistant 🤖")
st.markdown(
    "Welcome to **TalentScout**! I'm your AI hiring assistant. "
    "I'll walk you through a short screening interview to get your profile started."
)

if "bot" not in st.session_state:
    st.session_state.bot = TalentScoutBot()

if "interview_completed" not in st.session_state:
    st.session_state.interview_completed = False

if "messages" not in st.session_state:
    st.session_state.messages = []
    initial_reply, _ = st.session_state.bot.get_response(
        INITIAL_GREETING_TRIGGER, chat_history=[]
    )
    st.session_state.messages.append(AIMessage(content=initial_reply))

for msg in st.session_state.messages:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(msg.content)

if st.session_state.interview_completed:
    st.balloons()
    st.success(
        "Thank you for your time! Your profile has been submitted to the TalentScout team. "
        "We'll be in touch shortly."
    )
    if st.button("Start New Interview"):
        del st.session_state.messages
        st.session_state.interview_completed = False
        st.rerun()

else:
    if user_input := st.chat_input("Type your response here…"):
        with st.chat_message("user"):
            st.markdown(user_input)

        history_snapshot = st.session_state.messages.copy()
        st.session_state.messages.append(HumanMessage(content=user_input))

        with st.chat_message("assistant"):
            with st.spinner("Thinking…"):
                reply, extracted_data = st.session_state.bot.get_response(
                    user_input, chat_history=history_snapshot
                )
            st.markdown(reply)

        st.session_state.messages.append(AIMessage(content=reply))

        if extracted_data:
            save_candidate_data(extracted_data)
            st.session_state.interview_completed = True
            st.rerun()
