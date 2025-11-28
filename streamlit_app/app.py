import streamlit as st
import requests

st.title("ИИ ассистент по коституции РФ")


st.subheader("Настройки подключения")

ip_option = st.selectbox(
    "Выберите адрес сервера:",
    ["localhost (127.0.0.1)", "PC (192.168.0.245)", "Ввести вручную"]
)

if ip_option == "localhost (127.0.0.1:8000)":
    selected_ip = "127.0.0.1:8000"

elif ip_option == "PC (192.168.0.245:8000)":
    selected_ip = "192.168.0.245:8000"

else:
    selected_ip = st.text_input("Введите IP вручную:", value="192.168.0.245:8000")

API_URL = f"http://{selected_ip}/generate"


st.subheader("Чат с моделью")

query = st.text_input("Введите ваш вопрос:")

if st.button("Отправить"):
    if query.strip() == "":
        st.warning("Введите вопрос!")
    else:
        with st.spinner("Генерация ответа..."):
            try:
                response = requests.post(API_URL, json={"query": query})
                
                if response.status_code == 200:
                    answer = response.json().get("answer")
                    st.success(answer)
                else:
                    st.error(f"Ошибка сервера: {response.status_code}")

            except Exception as e:
                st.error(f"Ошибка запроса: {e}")
