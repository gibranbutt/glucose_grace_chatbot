
import streamlit as st
import openai
from googletrans import Translator
import os

# Set your OpenAI API key here or use environment variable
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Glucose & Grace Chatbot", layout="centered")

st.title("🤖 Glucose & Grace - Multilingual Voice Chatbot")
st.markdown("Supporting pregnant women with diabetes")

# Language selector
languages = {
    "English": "en", "Polish": "pl", "Ukrainian": "uk", "Somali": "so", "Hindi": "hi", "Arabic": "ar"
}
language = st.selectbox("Choose your language:", list(languages.keys()))
lang_code = languages[language]

# Input (typed for now; voice JS requires frontend integration)
user_input = st.text_input("Ask me anything about pregnancy and diabetes:", "")

if user_input:
    with st.spinner("Thinking..."):

        # Translate to English
        translator = Translator()
        translated_input = translator.translate(user_input, src=lang_code, dest='en').text

        # Query OpenAI
        prompt = f"You are a helpful assistant for pregnant women with diabetes. Answer in plain, supportive language.

Q: {translated_input}
A:"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )
        english_answer = response.choices[0].message['content'].strip()

        # Translate back to selected language
        translated_answer = translator.translate(english_answer, src='en', dest=lang_code).text

        # Show response
        st.markdown("### 🤱 Answer:")
        st.write(translated_answer)

        # Text-to-Speech (Browser TTS will be handled via frontend or JS widget)
        st.markdown(f"<audio controls autoplay src='https://translate.google.com/translate_tts?ie=UTF-8&q={translated_answer}&tl={lang_code}&client=tw-ob'></audio>", unsafe_allow_html=True)

st.markdown("---")
st.caption("This is a proof-of-concept. Always consult your midwife or diabetes team for personal advice.")
