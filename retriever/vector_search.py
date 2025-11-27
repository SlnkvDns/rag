from langchain_community.vectorstores import FAISS
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from langchain_community.embeddings import HuggingFaceBgeEmbeddings


class HybridRetriever:
    def __init__(self, store_path: str = 'db/faiss_store', 
                 num_bm25_docs: int = 10, 
                 num_faiss_docs: int = 10,
                 bm25_weight: float = 0.5,
                 faiss_weight: float = 0.5):
        self.num_bm25_docs = num_bm25_docs
        self.num_faiss_docs = num_faiss_docs
        
        self.embeddings = HuggingFaceBgeEmbeddings(
            model_name="deepvk/USER-bge-m3"
        )
        
        self.faiss_store = FAISS.load_local(store_path, self.embeddings, allow_dangerous_deserialization=True)
        docs = list(self.faiss_store.docstore._dict.values())
        
        self.bm25_retriever = BM25Retriever.from_documents(docs)
        self.bm25_retriever.k = num_bm25_docs
        
        self.faiss_retriever = self.faiss_store.as_retriever(
            search_kwargs={"k": num_faiss_docs}
        )
        
        self.ensemble_retriever = EnsembleRetriever(
            retrievers=[self.bm25_retriever, self.faiss_retriever],
            weights=[bm25_weight, faiss_weight]
        )
    
    def get_relevant_docs(self, query: str):
        return self.ensemble_retriever.get_relevant_documents(query)
