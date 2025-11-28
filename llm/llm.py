import ollama
from retriever.find_relevant_docs import BestDocsFinder
from scripts.format_docs import format_docs

class LLM:
    def __init__(self, num_bm25_docs=10, num_faiss_docs=10, top_n=5, think=None):
        self.think = think
        self.df = BestDocsFinder(num_bm25_docs, num_faiss_docs, top_n)

    def generate_answer(self, query):
        relevant_docs = self.df.find_best_docs(query)
        formatted_docs = format_docs(relevant_docs)

        context = "\n\n".join([doc.page_content for doc in formatted_docs])
        prompt = f"""
Ты — специалист-юрист, консультирующий по Конституции Российской Федерации. 
Твоя задача — отвечать на вопросы, используя только предоставленный контекст.

КОНТЕКСТ:
{context}

ВОПРОС:
{query}

[Инструкции]
1. Отвечай максимально точно, используя информацию только из контекста.
2. При ссылках на статьи Конституции РФ обязательно указывай:
   Раздел → Глава → Статья (например, Раздел I, Глава 2, Статья 12).
3. Если информация отсутствует в контексте, отвечай: "На основе предоставленного контекста ответить невозможно."
4. Не добавляй собственные интерпретации вне контекста.
5. Структурируй ответ: сначала краткий ответ, затем, если нужно, подробное объяснение с точными ссылками.

Пример ответа:
Краткий ответ: [твой ответ]
Подробно: [текст с указанием Раздел → Глава → Статья]

Начинай ответ только после ВОПРОСА.
"""

        resp = ollama.generate(model="gpt-oss:20b", prompt=prompt, think=self.think)
        return resp["response"]
