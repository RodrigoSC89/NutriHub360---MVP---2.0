import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.set_page_config(page_title="Evolução do Paciente", page_icon="📈")
st.title("📈 Evolução do Paciente")

# Verifica se há dados de pacientes e consultas
if not os.path.exists("consultas.csv"):
    st.warning("Nenhuma consulta registrada ainda.")
    st.stop()

consultas = pd.read_csv("consultas.csv")

if consultas.empty:
    st.warning("Nenhuma consulta registrada.")
    st.stop()

# Selecionar paciente
pacientes = consultas["Paciente"].unique()
paciente = st.selectbox("Selecione o paciente:", pacientes)
df_paciente = consultas[consultas["Paciente"] == paciente]

# Simulação de evolução de peso e IMC
# Recomendado: substituir por dados reais posteriormente
df_paciente = df_paciente.copy()
df_paciente = df_paciente.sort_values("Data")
df_paciente["Peso"] = 65 + (df_paciente.index * 0.8)  # Simulação

# Calcula IMC simulado se altura fosse 1.70m
altura = 1.70
df_paciente["IMC"] = df_paciente["Peso"] / (altura**2)

st.subheader("📊 Gráfico de Peso")
fig_peso = px.line(df_paciente, x="Data", y="Peso", markers=True, title=f"Evolução de Peso - {paciente}")
st.plotly_chart(fig_peso, use_container_width=True)

st.subheader("📊 Gráfico de IMC")
fig_imc = px.line(df_paciente, x="Data", y="IMC", markers=True, title=f"Evolução de IMC - {paciente}")
st.plotly_chart(fig_imc, use_container_width=True)
