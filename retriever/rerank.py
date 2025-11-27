from langchain_community.cross_encoders import HuggingFaceCrossEncoder


def rerank_docs(query, docs, top_n=5):
    model = HuggingFaceCrossEncoder(
        model_name="qilowoq/bge-reranker-v2-m3-en-ru"
    )
    pairs = [(query, doc.page_content) for doc in docs]
    scores = model.score(pairs)

    docs_with_scores = list(zip(docs, scores))
    docs_with_scores.sort(key=lambda x: x[1], reverse=True)
    reranked_docs = [doc for doc, score in docs_with_scores[:top_n]]
    return reranked_docs
