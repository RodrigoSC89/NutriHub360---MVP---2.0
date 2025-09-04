import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Agenda de Consultas", page_icon="📅", layout="centered")

AGENDA_PATH = "agenda_consultas.json"

# Função para carregar agendamentos
def carregar_agenda():
    if os.path.exists(AGENDA_PATH):
        return pd.read_json(AGENDA_PATH)
    else:
        return pd.DataFrame(columns=["Paciente", "Data", "Hora", "Motivo"])

# Função para salvar agendamento
def salvar_agenda(df):
    df.to_json(AGENDA_PATH, orient="records", indent=4)

# Carrega agenda
agenda_df = carregar_agenda()

st.title("🗕️ Agenda de Consultas")

# Abas para agendar e ver consultas
aba = st.radio("Opções", ["📌 Agendar Consulta", "📖 Consultas Marcadas"])

if aba == "📌 Agendar Consulta":
    with st.form("form_agendamento"):
        paciente = st.text_input("Nome do Paciente")
        data = st.date_input("Data", min_value=datetime.today())
        hora = st.time_input("Hora")
        motivo = st.text_area("Motivo")
        enviar = st.form_submit_button("Salvar Agendamento")

        if enviar:
            if paciente:
                novo = pd.DataFrame([{
                    "Paciente": paciente,
                    "Data": str(data),
                    "Hora": str(hora),
                    "Motivo": motivo
                }])
                agenda_df = pd.concat([agenda_df, novo], ignore_index=True)
                salvar_agenda(agenda_df)
                st.success(f"Consulta agendada para {paciente} em {data} às {hora}.")
            else:
                st.warning("Por favor, preencha o nome do paciente.")

elif aba == "📖 Consultas Marcadas":
    if agenda_df.empty:
        st.info("Nenhuma consulta agendada.")
    else:
        agenda_df = agenda_df.sort_values(by=["Data", "Hora"])
        st.dataframe(agenda_df, use_container_width=True)

        st.subheader("❌ Excluir Consulta")
        paciente_excluir = st.selectbox("Selecione um paciente para remover todas as consultas:", agenda_df["Paciente"].unique())
        if st.button("Excluir Consultas do Paciente"):
            agenda_df = agenda_df[agenda_df["Paciente"] != paciente_excluir]
            salvar_agenda(agenda_df)
            st.success(f"Consultas de {paciente_excluir} excluídas.")
