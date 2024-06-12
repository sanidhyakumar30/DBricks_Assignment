from utils.BotConversation import BotConversation as bot_conv
import streamlit as st
from utils.BotConversation import BotConversation

def start_app():
    st.set_page_config("Ubuntu Chatbot")
    st.header("Ubuntu QA Support Chatbot")
    st.button('Start New Chat', on_click= BotConversation.start_conversation, args=[''])

    print("Started Demo Bot.\n")
    ## TODO Complete the logic for managing the chatbot.
            






    
