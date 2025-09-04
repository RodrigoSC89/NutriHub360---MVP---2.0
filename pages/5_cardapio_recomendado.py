import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cardápio Recomendado", layout="wide")

st.title("🍱 Cardápio Recomendado")
st.markdown("Sugestão de alimentação diária com base no plano nutricional do paciente.")

# Carrega os pacientes
try:
    pacientes = pd.read_csv("data/pacientes.csv")
    cardapios = pd.read_csv("data/cardapios.csv")
    nomes_pacientes = pacientes["nome"].tolist()

    nome_selecionado = st.selectbox("Selecione um paciente:", nomes_pacientes)
    paciente_id = pacientes[pacientes["nome"] == nome_selecionado]["id"].values[0]

    cardapio_paciente = cardapios[cardapios["paciente_id"] == paciente_id]

    if not cardapio_paciente.empty:
        for idx, row in cardapio_paciente.iterrows():
            st.subheader(f"🍽️ {row['refeicao']}")
            st.markdown(f"- {row['descricao']}")
    else:
        st.info("Nenhum cardápio encontrado para este paciente.")

except FileNotFoundError:
    st.error("Base de dados de pacientes ou cardápios não encontrada.")
