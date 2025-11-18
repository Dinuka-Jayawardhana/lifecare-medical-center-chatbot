from .embedding_model import embedding_model
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma



def create_pdf_retriever():

    pdf_path = r"app\rag\document\Lifecare Medical Center.pdf" 

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50
    )
    splits = text_splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(documents=splits, embedding=embedding_model)
    retriever = vectorstore.as_retriever()

    return retriever
