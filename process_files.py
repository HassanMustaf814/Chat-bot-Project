from PyPDF2 import PdfReader
from docx import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_word_text(word_docs):
    text = ""
    for doc in word_docs:
        document = Document(doc)
        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def process_files(uploaded_files):
    raw_text = ""
    pdf_docs = [file for file in uploaded_files if file.name.endswith(".pdf")]
    word_docs = [file for file in uploaded_files if file.name.endswith(".docx")]

    if pdf_docs:
        raw_text += get_pdf_text(pdf_docs)
    if word_docs:
        raw_text += get_word_text(word_docs)

    text_chunks = get_text_chunks(raw_text)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")