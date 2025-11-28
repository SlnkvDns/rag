from retriever.vector_search import HybridRetriever
from retriever.rerank import rerank_docs

class BestDocsFinder:
    def __init__(self, num_bm25_docs, num_faiss_docs, top_n):
        self.retriever = HybridRetriever(
        num_bm25_docs=num_bm25_docs,
        num_faiss_docs=num_faiss_docs
    )
        self.top_n = top_n
        
    def find_best_docs(self, query):
        relevant_docs = self.retriever.get_relevant_docs(query)

        best_docs = rerank_docs(query, relevant_docs, top_n=self.top_n)
        return best_docs
