import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/generate" 

st.title("LLM Chat (Streamlit + FastAPI)")

query = st.text_input("Введите ваш вопрос:")

if st.button("Отправить"):
    if query.strip() == "":
        st.warning("Введите вопрос!")
    else:
        try:
            response = requests.post(
                API_URL,
                json={"query": query}
            )
            if response.status_code == 200:
                answer = response.json().get("answer")
                st.success(answer)
            else:
                st.error(f"Ошибка сервера: {response.status_code}")
        except Exception as e:
            st.error(f"Ошибка запроса: {e}")
