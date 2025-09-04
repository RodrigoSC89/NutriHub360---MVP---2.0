import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Análise Alimentar", layout="wide")
st.title("🍽 Análise Alimentar")
st.markdown("Visualize e interprete a ingestão alimentar do paciente.")

# Carregar dados dos pacientes cadastrados
try:
    pacientes_df = pd.read_csv("data/pacientes.csv")
    nomes_pacientes = pacientes_df['Nome'].tolist()
except FileNotFoundError:
    st.error("Arquivo de pacientes não encontrado.")
    st.stop()

# Selecionar paciente
paciente = st.selectbox("Selecione o paciente para visualizar a análise alimentar:", nomes_pacientes)

# Carregar dados de análise alimentar (macronutrientes)
try:
    analises_df = pd.read_csv("data/analises_alimentares.csv")
except FileNotFoundError:
    st.error("Arquivo de análises alimentares não encontrado.")
    st.stop()

# Filtrar dados do paciente selecionado
analise_paciente = analises_df[analises_df['Nome'] == paciente]

if analise_paciente.empty:
    st.warning("Nenhuma análise alimentar encontrada para este paciente.")
else:
    carboidratos = analise_paciente['Carboidratos'].values[0]
    proteinas = analise_paciente['Proteinas'].values[0]
    gorduras = analise_paciente['Gorduras'].values[0]
    fibras = analise_paciente['Fibras'].values[0]

    labels = ['Carboidratos', 'Proteínas', 'Gorduras', 'Fibras']
    values = [carboidratos, proteinas, gorduras, fibras]
    colors = ['#FFD700', '#FF8C00', '#DC143C', '#32CD32']

    fig, ax = plt.subplots()
    bars = ax.bar(labels, values, color=colors)
    ax.set_title("Distribuição dos Macronutrientes")
    ax.set_ylabel("Gramas")

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, height, f'{int(height)}', ha='center', va='bottom')

    st.pyplot(fig)
