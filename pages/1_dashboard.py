import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide")

st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>
        🔎 Dashboard Nutricional
    </h1>
    <p style='text-align: center;'>Resumo geral das informações nutricionais.</p>
    <hr>
""", unsafe_allow_html=True)

# Colunas para dados fictícios
col1, col2, col3 = st.columns(3)

col1.metric("Pacientes Ativos", "120")
col2.metric("Consultas Hoje", "15")
col3.metric("Média IMC", "23.4")

st.markdown("""
    <br>
    <h3>Observações Relevantes</h3>
    <ul>
        <li>Aumento no número de pacientes com sobrepeso.</li>
        <li>Alto consumo de ultraprocessados entre jovens.</li>
        <li>Maior adesão às dietas com baixo teor de carboidrato.</li>
    </ul>
""", unsafe_allow_html=True)
