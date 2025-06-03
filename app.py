import streamlit as st
from style_utils import detect_traditional_elements, suggest_fusion_styles
from fusion_agent import talk_to_agent
from PIL import Image

st.set_page_config(page_title="TradTrend AI", layout="wide")
st.title("👘🧥 TradTrend AI – Where Tradition Meets Trend")
st.markdown("Upload your traditional outfit image and get AI-powered trendy suggestions.")

uploaded_file = st.file_uploader("Upload a Traditional Outfit Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Outfit", use_column_width=True)

    st.subheader("🔍 Traditional Elements Detected:")
    elements = detect_traditional_elements(image)
    st.success(", ".join(elements))

    st.subheader("✨ Fusion Style Suggestions:")
    suggestions = suggest_fusion_styles(elements)
    st.markdown(suggestions)

    st.subheader("🧠 Ask the Fashion AI Agent")
    user_prompt = st.text_input("Type your fashion question")
    if user_prompt:
        response = talk_to_agent(user_prompt)
        st.markdown(response)
