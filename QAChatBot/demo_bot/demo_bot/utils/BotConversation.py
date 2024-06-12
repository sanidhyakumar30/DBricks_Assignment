from utils.Retrieval import getResponse
from utils.Utilities import get_top_documents
from operator import itemgetter
import streamlit as st
from langchain.memory import ConversationBufferMemory

@st.cache_data
@st.cache_resource
class BotConversation:

    def start_conversation(self):
        global memory
        print("Starting new conversation ...\n\n") 
        # Clear the session state messages, cache data, cache resource, and session state
        st.session_state.messages = None 
        st.cache_data.clear()
        st.cache_resource.clear()
        st.session_state.clear()
        memory= ConversationBufferMemory(memory_key='chat_history',output_key='answer' )
        # st.rerun()

    def continue_conversation(store):
        print("Continuing current conversation.\n\n")
        user_query =  st.chat_input("Ask a Question")

        # If no messages in the session state, initialize the messages with a greeting from the assistant
        if "messages" not in st.session_state.keys():
            st.session_state["messages"] = [{"role": "assistant",
                                            "content": "Ubuntu Support Bot is ready to assist you. How can I help you today?"}]

        # If there are messages in the session state, display them in the chat
        if "messages" in st.session_state.keys():
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.write(message["content"])

        # If the user has asked a question, add it to the session state messages and display it in the chat
        if user_query is not None:
            st.session_state.messages.append({
                "role":"user",
                "content":user_query
            })
            with st.chat_message("user"):
                st.write(user_query)

        # If the last message in the session state messages is not from the assistant, get a response from the assistant
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Loading"):
                    output, source_docs = getResponse(store, user_query)
                    ai_response = output
                    st.write(ai_response)
            
             # Add the assistant's response to the session state messages
            new_ai_message = {"role":"assistant","content": ai_response}
            st.session_state.messages.append(new_ai_message)
            get_top_documents(source_docs)
            print(source_docs)


        
        
