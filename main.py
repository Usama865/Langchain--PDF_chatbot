from pypdf import PdfReader
import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.llms import GooglePalm
from langchain.memory import ConversationBufferMemory
# from dotenv import load_dotenv

# load_dotenv()

r_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show
    separators=["\n\n",'\n','.'],
    chunk_size=500,
    chunk_overlap=50,
    length_function=len,
    keep_separator= False)
embeddings= HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def get_pdf_text(pdf_file):
    raw_text=""
    reader= PdfReader(pdf_file)
    for page in reader.pages:
        pages=page.extract_text()
        raw_text += pages
    return raw_text

def get_chunks(pdf_text):
    chunks=r_splitter.split_text(pdf_text)
    return chunks

def get_vector_db(text_chunks):
    db=FAISS.from_texts(texts=text_chunks,embedding=embeddings)
    return db

def get_conversation_chain(vector_db):
    llm= GooglePalm(GOOGLE_API_KEY ="AIzaSyDmSua6A-bn674fYK6e9mjB1rjvGv3kM6s",temperature=0.3,max_output_tokens=517)
    memory=ConversationBufferMemory()
    retriver=vector_db.as_retriever()
    chain=RetrievalQA.from_chain_type(llm=llm,retriever=retriver,memory=memory,verbose=True) 
    return(chain)


