from __future__ import print_function
from utils.Start import start_app
import openai
from langchain.embeddings import OpenAIEmbeddings
from utils.Utilities import get_markdown_chunks, initialize_vectorstore, \
    get_templates, init_config
from operator import itemgetter
import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.BotConversation import BotConversation


if __name__ == "__main__":
    try:
        print('Starting Demo Bot ...\n')
        openai.api_key = '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'
        openai.api_base = 'https://api.openai.com/v1'
        config_data = init_config()
        vectorstore_path, prompt_template_path = itemgetter('vectorstore_path', 'prompt_template_path')(config_data)
        # embeddings = OpenAIEmbeddings(openai_api_key=openai.api_key) 
        # Initialize the embeddings using GoogleGenerativeAIEmbeddings
        embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")

        # Start the app
        start_app()

        #Get the markdown chunks
        chunks = get_markdown_chunks()
        # Initialize the vectorstore
        store = initialize_vectorstore(vectorstore_path, embeddings, chunks)  
        BotConversation.continue_conversation(store) 

        # Get the templates
        templates = get_templates(prompt_template_path)


    except Exception as err:
        print(f"Error encountered in function: [main]: {str(err)}")

 

