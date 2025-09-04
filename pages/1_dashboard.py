import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Dashboard Nutricional", layout="wide")

# Caminho do arquivo de pacientes
FILE_PATH = "pacientes.csv"

# Função para carregar dados
@st.cache_data

def load_data():
    if os.path.exists(FILE_PATH):
        return pd.read_csv(FILE_PATH)
    return pd.DataFrame(columns=[
        "Nome", "Idade", "Sexo", "Peso", "Altura", "IMC",
        "Objetivo", "Restricoes", "Condicoes", "Plano", "Observacoes"
    ])

# Função para calcular IMC
def calcular_imc(peso, altura):
    if altura > 0:
        return round(peso / (altura ** 2), 1)
    return 0

# Carregar dados
df = load_data()

# Cabeçalho
st.markdown("""
    <h1 style='text-align: center; color: green;'>🔍 Dashboard Nutricional</h1>
    <p style='text-align: center;'>Resumo geral das informações nutricionais.</p>
""", unsafe_allow_html=True)

# KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Pacientes Ativos", len(df))

with col2:
    st.metric("Consultas Hoje", 15)  # Exemplo estático

with col3:
    media_imc = df["IMC"].mean() if not df.empty else 0
    st.metric("Média IMC", round(media_imc, 1))

# Lista de pacientes
st.subheader("👥 Lista de Pacientes")

if df.empty:
    st.info("Nenhum paciente cadastrado ainda.")
else:
    selected_index = st.selectbox(
        "Selecione um paciente para detalhes ou exclusão:",
        options=df.index,
        format_func=lambda x: f"{df.loc[x, 'Nome']} (IMC: {df.loc[x, 'IMC']})"
    )

    paciente = df.loc[selected_index]

    st.write(f"**Nome:** {paciente['Nome']}")
    st.write(f"**Idade:** {paciente['Idade']} anos")
    st.write(f"**Sexo:** {paciente['Sexo']}")
    st.write(f"**Peso:** {paciente['Peso']} kg")
    st.write(f"**Altura:** {paciente['Altura']} m")
    st.write(f"**IMC:** {paciente['IMC']}")
    st.write(f"**Objetivo:** {paciente['Objetivo']}")
    st.write(f"**Restrições Alimentares:** {paciente['Restricoes']}")
    st.write(f"**Condições de Saúde:** {paciente['Condicoes']}")
    st.write(f"**Plano Nutricional:** {paciente['Plano']}")
    st.write(f"**Observações:** {paciente['Observacoes']}")

    if st.button("❌ Excluir Paciente"):
        df = df.drop(index=selected_index)
        df.to_csv(FILE_PATH, index=False)
        st.success("Paciente excluído com sucesso!")
        st.experimental_rerun()

# Observações gerais
st.subheader("📌 Observações Relevantes")
st.markdown("""
- Aumento no número de pacientes com sobrepeso.
- Alto consumo de ultraprocessados entre jovens.
- Maior adesão às dietas com baixo teor de carboidrato.
""")
