import streamlit as st
import pandas as pd
import os
from fpdf import FPDF

st.set_page_config(page_title="Gerar Relatório PDF", page_icon="📤")
st.title("📤 Gerar Relatório da Consulta (PDF)")

CONSULTAS_PATH = "consultas.csv"

# Função para carregar consultas
def carregar_consultas():
    if os.path.exists(CONSULTAS_PATH):
        return pd.read_csv(CONSULTAS_PATH)
    else:
        return pd.DataFrame(columns=["Paciente", "Data", "Sintomas", "Diagnostico", "Prescricao"])

consultas_df = carregar_consultas()

if consultas_df.empty:
    st.warning("Nenhuma consulta encontrada.")
    st.stop()

# Seleção de paciente
pacientes = consultas_df["Paciente"].unique()
selecionado = st.selectbox("Selecione um paciente:", pacientes)

paciente_df = consultas_df[consultas_df["Paciente"] == selecionado].sort_values(by="Data", ascending=False)

st.subheader("📋 Última Consulta")
ultima = paciente_df.iloc[0]
st.write(f"**Data:** {ultima['Data']}")
st.write(f"**Sintomas:** {ultima['Sintomas']}")
st.write(f"**Diagnóstico:** {ultima['Diagnostico']}")
st.write(f"**Prescrição:** {ultima['Prescricao']}")

# Função para gerar PDF
def gerar_pdf(dados):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, f"Relatório Nutricional - {dados['Paciente']}", ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    for k, v in dados.items():
        pdf.multi_cell(0, 10, f"{k}: {v}")
    caminho = f"relatorio_{dados['Paciente'].replace(' ', '_')}.pdf"
    pdf.output(caminho)
    return caminho

if st.button("📄 Gerar PDF da Última Consulta"):
    caminho_pdf = gerar_pdf(ultima)
    with open(caminho_pdf, "rb") as file:
        st.download_button("📥 Baixar Relatório PDF", data=file, file_name=caminho_pdf, mime="application/pdf")
