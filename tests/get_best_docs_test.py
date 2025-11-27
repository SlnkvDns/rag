from retriever.find_relevant_docs import BestDocsFinder
from scripts.format_docs import format_docs

def get_best_docs_test():
    df = BestDocsFinder(num_bm25_docs=10, num_faiss_docs=10)
    while True:
        query = input("Вопрос: ")
        relevant_docs = df.find_best_docs(query)
        formatted_docs = format_docs(relevant_docs)

        for i in range(len(formatted_docs)):
            print(f'Документ {i+1}\n-------------------------')
            print(formatted_docs[i].page_content)
        print('\n\n')


if __name__ == '__main__':
    get_best_docs_test()
