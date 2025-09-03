import streamlit as st
from datetime import date

st.set_page_config(page_title="Registro de Consultas", page_icon="📝")

st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
        }
        .stTextArea>div>textarea {
            border-radius: 10px;
        }
        .stButton>button {
            border-radius: 10px;
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📝 Registro de Consultas")
st.subheader("Registre consultas, diagnósticos e prescrições")

with st.form("form_consulta"):
    st.write("Preencha os dados da consulta abaixo:")

    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome do paciente")
        idade = st.number_input("Idade", min_value=0, max_value=120, step=1)
    with col2:
        data_consulta = st.date_input("Data da consulta", value=date.today())

    sintomas = st.text_area("Sintomas")
    diagnostico = st.text_area("Diagnóstico")
    prescricao = st.text_area("Prescrição")

    enviado = st.form_submit_button("Salvar Consulta")

if enviado:
    st.success(f"✅ Consulta de **{nome}** registrada com sucesso!")
