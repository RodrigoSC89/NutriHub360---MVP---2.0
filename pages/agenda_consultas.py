import streamlit as st
import pandas as pd
import os
from datetime import datetime

DATA_PATH = "data/agendamentos.csv"

# Função para carregar dados existentes
def carregar_agendamentos():
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH, parse_dates=['data'])
    else:
        return pd.DataFrame(columns=["nome", "data", "hora", "motivo"])

# Função para salvar agendamento
def salvar_agendamento(agendamento):
    agendamentos = carregar_agendamentos()
    agendamentos = pd.concat([agendamentos, pd.DataFrame([agendamento])], ignore_index=True)
    agendamentos.to_csv(DATA_PATH, index=False)

# Interface Streamlit
st.set_page_config(page_title="Agenda de Consultas", layout="centered")
st.title("📅 Agenda de Consultas")

aba = st.radio("Escolha uma opção:", ["Agendar Consulta", "Ver Consultas"])

if aba == "Agendar Consulta":
    st.subheader("Agendamento de nova consulta")
    nome = st.text_input("Nome do paciente")
    data = st.date_input("Data da consulta", min_value=datetime.today())
    hora = st.time_input("Hora da consulta")
    motivo = st.text_area("Motivo da consulta")

    if st.button("Agendar"):
        if nome:
            salvar_agendamento({
                "nome": nome,
                "data": data,
                "hora": hora,
                "motivo": motivo
            })
            st.success(f"Consulta agendada para {nome} em {data} às {hora}.")
        else:
            st.warning("Por favor, preencha o nome do paciente.")

else:
    st.subheader("Consultas Agendadas")
    agendamentos = carregar_agendamentos()

    if agendamentos.empty:
        st.info("Nenhuma consulta agendada ainda.")
    else:
        agendamentos = agendamentos.sort_values(by=["data", "hora"])
        st.dataframe(agendamentos, use_container_width=True)
