## TODO Add imports
## TODO Add below:
# 1. errors/exception handling 
# 2. loggers
from utils.Utilities import get_templates, init_config
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from operator import itemgetter
from langchain.vectorstores import FAISS

global memory
def getResponse(vectorstore, query):
    global memory
    config_data = init_config()
    prompt_template_path = itemgetter('prompt_template_path')(config_data)

    PROMPT = get_templates(prompt_template_path)
    chain_type_kwargs = { "prompt" : PROMPT }

    #LLM

    # llm=ChatOpenAI(
    # model="gpt-4o",
    # temperature=0,
    # max_tokens=None,
    # timeout=None,
    # max_retries=2)
    llm= ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True, output_key='answer')
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever= vectorstore.as_retriever(),
        memory = memory,
        combine_docs_chain_kwargs=chain_type_kwargs,
        return_source_documents=True
    )

    response  = conversation_chain({"question": query})
    source_docs = response.get("source_documents")

    return(response.get("answer"), source_docs)
    
