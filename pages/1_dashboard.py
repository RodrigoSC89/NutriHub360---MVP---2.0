import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Nutricional", layout="wide")

st.markdown("<h1 style='text-align: center; color: #2e8b57;'>🔍 Dashboard Nutricional</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Resumo geral das informações nutricionais.</p>", unsafe_allow_html=True)
st.markdown("---")

# Função para carregar os dados da sessão
def load_data():
    if 'pacientes' not in st.session_state:
        st.session_state.pacientes = []
    return st.session_state.pacientes

# Função para excluir paciente
def excluir_paciente(index):
    if 0 <= index < len(st.session_state.pacientes):
        del st.session_state.pacientes[index]

# Carregar dados
pacientes = load_data()

# Mostrar lista de pacientes com opção de excluir
st.subheader("👥 Pacientes Cadastrados")
if pacientes:
    for i, p in enumerate(pacientes):
        col1, col2 = st.columns([6, 1])
        with col1:
            st.markdown(f"**{p['nome']}** - {p['idade']} anos - {p['sexo']} - Altura: {p['altura']} m - Peso: {p['peso']} kg - IMC: {p['imc']:.2f}")
        with col2:
            if st.button("🗑️", key=f"del_{i}"):
                excluir_paciente(i)
                st.experimental_rerun()
else:
    st.info("Nenhum paciente cadastrado.")

st.markdown("---")

# Atualizar métricas
qtd_pacientes = len(pacientes)
imc_medio = sum(p['imc'] for p in pacientes) / qtd_pacientes if pacientes else 0
consultas_hoje = 15  # Simulação

col1, col2, col3 = st.columns(3)
col1.metric("Pacientes Ativos", qtd_pacientes)
col2.metric("Consultas Hoje", consultas_hoje)
col3.metric("Média IMC", f"{imc_medio:.1f}")

st.markdown("---")

st.subheader("📝 Observações Relevantes")
st.markdown("""
- Aumento no número de pacientes com sobrepeso.
- Alto consumo de ultraprocessados entre jovens.
- Maior adesão às dietas com baixo teor de carboidrato.
""")
