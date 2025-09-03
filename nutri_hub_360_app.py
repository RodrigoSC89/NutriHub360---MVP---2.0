import streamlit as st
from PIL import Image

st.set_page_config(page_title="NutriHub360", layout="wide")

# Logo (certifique-se de que o arquivo logo.png está no repositório)
try:
    st.sidebar.image("logo.png", width=140)
except:
    st.sidebar.markdown("![logo](https://via.placeholder.com/140x60.png?text=NutriHub360)")

st.sidebar.title("NutriHub360")
st.sidebar.caption("Sistema Inteligente de Apoio Nutricional 💚")

st.markdown("""
    # 🏡 Bem-vindo ao NutriHub360
    ### Seu assistente digital para transformar a nutrição no Brasil 🇧🇷
    Escolha uma funcionalidade no menu lateral para começar.
""")
