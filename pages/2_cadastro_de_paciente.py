import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Cadastro de Paciente", page_icon="🧑‍⚕️")

st.title("🧑‍⚕️ Cadastro de Paciente")
st.write("Adicione novos pacientes ao sistema.")

# Caminho do arquivo CSV
dados_path = "pacientes.csv"

# Função para carregar os dados
def carregar_dados():
    if os.path.exists(dados_path):
        return pd.read_csv(dados_path)
    return pd.DataFrame(columns=["Nome", "Idade", "Sexo", "Peso", "Altura", "IMC"])

# Função para salvar os dados
def salvar_dados(df):
    df.to_csv(dados_path, index=False)

# Formulário de cadastro
with st.form("form_paciente"):
    nome = st.text_input("Nome completo")
    idade = st.number_input("Idade", min_value=0, max_value=120, step=1)
    sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
    peso = st.number_input("Peso (kg)", min_value=0.0, step=0.1)
    altura = st.number_input("Altura (m)", min_value=0.0, step=0.01)
    enviado = st.form_submit_button("Cadastrar Paciente")

# Lógica para salvar o paciente
if enviado:
    if nome and idade and peso > 0 and altura > 0:
        imc = round(peso / (altura ** 2), 1)
        novo = pd.DataFrame([[nome, idade, sexo, peso, altura, imc]], columns=["Nome", "Idade", "Sexo", "Peso", "Altura", "IMC"])
        df = carregar_dados()
        df = pd.concat([df, novo], ignore_index=True)
        salvar_dados(df)
        st.success(f"Paciente {nome} cadastrado com sucesso! IMC: {imc}")
    else:
        st.error("Por favor, preencha todos os campos corretamente.")

# Exibir pacientes já cadastrados
st.subheader("📋 Pacientes Cadastrados")
df = carregar_dados()
st.dataframe(df, use_container_width=True)
