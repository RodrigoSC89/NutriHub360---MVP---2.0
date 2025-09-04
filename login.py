import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import os

st.set_page_config(page_title="Login | NutriHub360", page_icon="🔐", layout="centered")

# Carrega as credenciais do arquivo config.yaml
with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["preauthorized"]
)

# Login
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    st.success(f"Bem-vindo(a), {name}! 👋")
    st.markdown("""
        ### Acesse o menu lateral para utilizar o sistema NutriHub360:
        - 📊 Dashboard
        - 👤 Cadastro de pacientes
        - 📝 Registro de consultas
        - 🍽️ Análise alimentar
        - 📅 Agenda de consultas
        - 📚 Biblioteca nutricional
    """)
    authenticator.logout("Sair", "sidebar")

elif authentication_status is False:
    st.error("Usuário ou senha inválidos. Tente novamente.")

elif authentication_status is None:
    st.warning("Por favor, insira seu usuário e senha.")
