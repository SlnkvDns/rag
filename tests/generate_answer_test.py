from llm.llm import LLM


def generate_answer_test():
    llm = LLM(
        num_bm25_docs=10,
        num_faiss_docs=10,
        top_n=5)
    while True:
        query = input('Вопрос: ')
        print(llm.generate_answer(query))


if __name__ == '__main__':
    generate_answer_test()
