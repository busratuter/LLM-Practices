import streamlit as st
from langchain.schema import SystemMessage, HumanMessage
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOllama

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.base import BaseCallbackHandler
from typing import Any

class StreamlitCallbackHandler(BaseCallbackHandler):
    def __init__(self, placeholder):
        self.placeholder = placeholder
        self.final_text = ""

    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        self.final_text += token
        self.placeholder.markdown(self.final_text + "  ")


memory = ConversationBufferMemory(return_messages=True)

st.set_page_config(page_title="Tourist Guide Bot", page_icon="🌍")
st.title(" 🌍 Tourist Guide Bot 🌍")
st.markdown("You can ask me about Turkey's rich history, cultural sites, local cuisine, traditions, transportation, and travel tips.")

#for taking user chat history

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)

user_input = st.text_input("You can ask me anything about Turkey:", key="user_input")

# we need to look all the messages in the chat history and print them

for message in st.session_state.memory.chat_memory.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    else:
        with st.chat_message("guide"):
            st.markdown(message.content)

if user_input:
    st.session_state.memory.chat_memory.add_user_message(user_input)
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("guide"):

        response_placeholder = st.empty()
        stream_handler = StreamlitCallbackHandler(response_placeholder)

        llm = ChatOllama(model="llama3.2:3b", streaming=True, callbacks=[stream_handler])


    messages = [
        SystemMessage(content="You are a helpful and knowledgeable AI travel assistant specialized in Turkey. Your goal is to guide users through Turkey's rich history, cultural sites, local cuisine, traditions, transportation, and travel tips. Always provide clear, friendly, and accurate information. Offer personalized suggestions based on user preferences when possible. If users ask about cities, landmarks, food, or travel plans within Turkey, respond with relevant, engaging, and useful guidance.")
    ] + st.session_state.memory.load_memory_variables({})["history"] + [HumanMessage(content=user_input)]

    response = llm(messages)

    st.session_state.memory.chat_memory.add_ai_message(response.content)

