from typing import List
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from scripts.chuncking import get_document_chunks_from_docx

def main():
    doc_path =  r'data/constitutionrf.docx'
    save_path = r'db/faiss_store'
    docs = get_document_chunks_from_docx(doc_path, chunk_size=3000, chunk_overlap=200)
    embeddings = HuggingFaceBgeEmbeddings(
        model_name="deepvk/USER-bge-m3"
    )
    create_vectore_store(docs, embeddings, save_path)


def create_vectore_store(docs: List[Document], emb_model, path):
    faiss_store = FAISS.from_documents(docs, emb_model)
    faiss_store.save_local(path)


if __name__ == '__main__':
    main()
