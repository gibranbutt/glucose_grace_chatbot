
import streamlit as st
import difflib

st.set_page_config(page_title="Glucose & Grace FAQ Chatbot", layout="centered")
st.title("🤖 Glucose & Grace - Rule-Based FAQ Chatbot")
st.markdown("Supporting pregnant women with diabetes")

# Predefined FAQs and answers
faq_data = {
    "can i eat chocolate during pregnancy with diabetes": 
        "It’s okay in small amounts, but pair it with protein or fibre to reduce sugar spikes. Try yoghurt, nuts, or wholegrain snacks instead.",
    "why are my blood sugars high in the morning":
        "Morning highs can be caused by hormones or the dawn phenomenon. Try eating earlier the night before, or ask your care team about insulin adjustments.",
    "can i breastfeed if i have diabetes":
        "Yes, breastfeeding is encouraged. You may need to adjust your insulin or snack more often due to lower blood sugars during feeds.",
    "what snacks are safe if i feel hungry":
        "Great snacks include oatcakes, yoghurt, nuts, boiled eggs, or small fruit with cheese. Avoid sugary options when possible.",
    "is it normal to feel overwhelmed managing diabetes in pregnancy":
        "Yes — many women feel this way. You’re not alone. Speak to your midwife or diabetes nurse for support, and try to take it one day at a time.",
    "what should i do if i feel dizzy or low on energy":
        "Check your glucose if you can. If you’re low, have fast-acting sugar like juice or glucose tabs, then a balanced snack. Contact your care team if unsure."
}

# Match input to best FAQ
user_input = st.text_input("Ask a question about pregnancy and diabetes:", "").strip().lower()

if user_input:
    with st.spinner("Thinking..."):
        match = difflib.get_close_matches(user_input, faq_data.keys(), n=1, cutoff=0.5)
        if match:
            st.markdown("### 🤱 Answer:")
            st.write(faq_data[match[0]])
        else:
            st.warning("Sorry, I don't have an answer for that yet. Try asking something more general about pregnancy and diabetes.")

st.markdown("---")
st.caption("This tool is for general support. Please consult your healthcare team for personal advice.")
