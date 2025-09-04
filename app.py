import streamlit as st
import os

st.set_page_config(
    page_title="NutriHub360",
    page_icon="🥗",
    layout="wide"
)

st.image("logo.png", width=180)

st.title("🥗 NutriHub360")

st.markdown("""
### Bem-vindo ao NutriHub360! 

Sistema completo para nutricionistas gerenciarem pacientes, consultas e planos alimentares de forma simples e eficiente. Use o menu lateral para acessar:

- 📊 Dashboard com visão geral dos pacientes
- 👤 Cadastro de pacientes
- 📝 Registro de consultas
- 🍽️ Análise alimentar e plano nutricional
- 📅 Agenda de consultas
- 📚 Biblioteca nutricional

---
**Dica:** Cadastre um paciente antes de acessar outras áreas.
""")
