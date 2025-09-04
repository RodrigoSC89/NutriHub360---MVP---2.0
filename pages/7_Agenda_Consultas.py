# melhorias_nutrihub360.py

import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Cria pasta de dados, se não existir
if not os.path.exists("data"):
    os.makedirs("data")

# Caminho do arquivo de agenda
AGENDA_PATH = "data/agenda.csv"

# Função para carregar ou criar a agenda
def load_agenda():
    if os.path.exists(AGENDA_PATH):
        return pd.read_csv(AGENDA_PATH)
    else:
        return pd.DataFrame(columns=["Paciente", "Data", "Hora", "Motivo"])

# Função para salvar agenda
def save_agenda(df):
    df.to_csv(AGENDA_PATH, index=False)

# Layout
st.set_page_config(page_title="Agenda Nutricional", page_icon="📅")
st.title("📅 Agenda de Consultas")

# Carrega agenda existente
agenda_df = load_agenda()

# Formulário para nova consulta
with st.form("form_agenda"):
    st.subheader("Marcar nova consulta")
    paciente = st.text_input("Nome do paciente")
    data = st.date_input("Data")
    hora = st.time_input("Hora")
    motivo = st.text_area("Motivo")
    submitted = st.form_submit_button("Salvar")

    if submitted:
        nova = pd.DataFrame([[paciente, str(data), str(hora), motivo]], columns=agenda_df.columns)
        agenda_df = pd.concat([agenda_df, nova], ignore_index=True)
        save_agenda(agenda_df)
        st.success("Consulta marcada com sucesso!")

# Mostrar agenda
st.subheader("📖 Consultas marcadas")

if agenda_df.empty:
    st.info("Nenhuma consulta marcada ainda.")
else:
    agenda_df = agenda_df.sort_values(by=["Data", "Hora"])
    st.dataframe(agenda_df, use_container_width=True)

    # Excluir consulta
    st.subheader("🗑️ Excluir Consulta")
    paciente_selecionado = st.selectbox("Selecione um paciente para excluir:", agenda_df["Paciente"].unique())
    if st.button("Excluir consulta(s)"):
        agenda_df = agenda_df[agenda_df["Paciente"] != paciente_selecionado]
        save_agenda(agenda_df)
        st.success(f"Consultas de {paciente_selecionado} removidas com sucesso!")
