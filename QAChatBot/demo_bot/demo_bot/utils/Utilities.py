## TODO Add imports
import json
from langchain.document_loaders import DirectoryLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
import streamlit as st



## TODO Add below:
# 1. errors/exception handling 
# 2. loggers

# This function loads markdown files from a specified directory, splits the text into chunks, and returns these chunks.
def get_markdown_chunks():
    markdown_path = "demo_bot/demo_bot_data"
    markdown_loader = DirectoryLoader(markdown_path, glob='**/*.md', loader_cls=UnstructuredMarkdownLoader)
    markdown_docs = markdown_loader.load()
    # print(markdown_docs)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
    chunks = text_splitter.split_documents(markdown_docs)
    return chunks

# This function initializes a vectorstore with the given embeddings and text chunks, and saves it to a specified path.
def initialize_vectorstore(vectorstore_path, embeddings, text_chunks):
    vectorstore = FAISS.from_documents(text_chunks, embeddings)
    vectorstore.save_local(vectorstore_path)
    return vectorstore

# This function loads a template from a specified path and returns it.
def get_templates(path):
    with open(f"{path}/sample.txt", "r") as f:
        prompt_template = f.read()
        PROMPT = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )
    return PROMPT
    
# This function prints the source documents and their content.
def get_top_documents(source_docs):
    print(source_docs)
    with st.expander("Document Similarity Search"):
        # Find the relevant chunks
        for i in source_docs:
            print(i.page_content)
            st.write(i.page_content)

# This function loads a configuration file and returns the configuration data.
def init_config():
    with open('demo_bot/demo_bot/data/metadata/config.json') as fobj:
        config_data = json.load(fobj)
    return config_data
