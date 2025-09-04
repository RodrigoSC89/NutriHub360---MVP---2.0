import streamlit as st
import pandas as pd
import os
from datetime import date

st.set_page_config(page_title="Registro de Consulta", page_icon="📝")
st.title("📝 Registro de Consulta")

# Caminho dos arquivos
dados_path = "pacientes.json"
consultas_path = "consultas.csv"

# Carregar pacientes
def carregar_pacientes():
    if os.path.exists(dados_path):
        import json
        with open(dados_path, "r") as f:
            return [p["nome"] for p in json.load(f)]
    return []

# Carregar consultas
def carregar_consultas():
    if os.path.exists(consultas_path):
        return pd.read_csv(consultas_path)
    return pd.DataFrame(columns=["Paciente", "Data", "Sintomas", "Diagnostico", "Prescricao"])

# Salvar consultas
def salvar_consulta(df):
    df.to_csv(consultas_path, index=False)

pacientes = carregar_pacientes()

if not pacientes:
    st.warning("Nenhum paciente cadastrado. Cadastre pacientes primeiro.")
    st.stop()

with st.form("form_consulta"):
    paciente = st.selectbox("Paciente", pacientes)
    data_consulta = st.date_input("Data da consulta", value=date.today())
    sintomas = st.text_area("Sintomas/Queixas")
    diagnostico = st.text_area("Diagnóstico Clínico")
    prescricao = st.text_area("Prescrição Nutricional")
    enviado = st.form_submit_button("Salvar Consulta")

if enviado:
    nova = pd.DataFrame([[paciente, data_consulta, sintomas, diagnostico, prescricao]],
                        columns=["Paciente", "Data", "Sintomas", "Diagnostico", "Prescricao"])
    df_consultas = carregar_consultas()
    df_consultas = pd.concat([df_consultas, nova], ignore_index=True)
    salvar_consulta(df_consultas)
    st.success(f"Consulta de {paciente} registrada com sucesso!")

# Histórico
st.subheader("📋 Histórico de Consultas")
consultas = carregar_consultas()
if not consultas.empty:
    st.dataframe(consultas.sort_values(by="Data", ascending=False), use_container_width=True)
else:
    st.info("Nenhuma consulta registrada ainda.")
