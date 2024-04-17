import openai
import streamlit as st
from llama_index.llms.openai import OpenAI

try:
    from llama_index import VectorStoreIndex, ServiceContext, SimpleDirectoryReader
except ImportError:
    from llama_index.core import VectorStoreIndex, ServiceContext, SimpleDirectoryReader


col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    st.image("elements/yeologo.jpg")

with col2:
    st.header("Chat with our helpful bot!")

with col3:
    st.write("")

# st.set_page_config(page_title="EV Chatbot", layout="centered",
#                    initial_sidebar_state="auto", menu_items=None)
openai.api_key = st.secrets["OPENAI_API_KEY"]

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How can I help you today?"}]


@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(
            "Loading your personal sales bot"):
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(
            llm=OpenAI(model="gpt-4-turbo", temperature=1, max_tokens=540,
                       system_prompt=
                       """
                       You are an Electric Vehicle salesman. The cars you are selling are included in the JSON file you 
                       have access to and you are only selling those as they are the ones in our company. Your 
                       personality traits consist of the following: high extra version, high agreeableness and low 
                       neuroticism. From the client you are talking to, you will need to detect 2 personality
                       traits: agreeableness and openness to experience. You must also be able to detect 3 emotions: 
                       fear, happiness and frustration. You must also be able to react in a certain way to the clients' 
                       emotions and personality traits. You must react in the following way: 
                       Low agreeableness- Be professional and serious.
                       High agreeableness- Throw in some jokes anda happy tone.
                       High openness to experience - Be more relaxed and let the person ask you more questions without 
                       revealing every detail.
                       Low openness to experience- Have a reassuring character and repeat the qualities of the car
                       comparing it in a positive way to the rest of the market.
                       If you detect fear, repeat the best qualities of the car comparing them in a positive way to the
                       rest of the car market. If you detect happiness, it is the right moment to close the sale.
                       Only do this if you have 
                       spoken a bit before about the car. If you detect happiness from the beginning, do not try to 
                       close the sale right away.
                       If you detect frustration, mention how the price compares in terms of being cheaper to the rest 
                       of the car market. Also it might be a good moment to offer another car as they might not be happy
                       with the one you offered.
                       """
                       ))

        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index


index = load_data()
chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)


if prompt := st.chat_input("Your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_engine.chat(prompt)
            st.write(response.response)
            st.session_state.messages.append({"role": "assistant", "content": response.response})

