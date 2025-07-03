
import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Free Pregnancy Diabetes Chatbot", layout="centered")

st.title("🤖 Glucose & Grace (Free Edition)")
st.markdown("Powered by Hugging Face - No API Key Needed")

@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-base")

model = load_model()

st.markdown("Ask a question about diabetes in pregnancy:")

user_input = st.text_input("You:", "")

if user_input:
    with st.spinner("Thinking..."):
        prompt = f"Answer this as a kind and helpful assistant for pregnant women with diabetes: {user_input}"
        result = model(prompt, max_length=200)
        answer = result[0]['generated_text']
        st.markdown("### 🤱 Answer:")
        st.write(answer)

st.markdown("---")
st.caption("This is a prototype. Please consult your healthcare provider for personalised advice.")
