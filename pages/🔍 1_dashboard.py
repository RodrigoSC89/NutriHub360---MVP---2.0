import streamlit as st
import json
import os
import datetime

st.set_page_config(page_title="Dashboard Nutricional", page_icon="🔍", layout="wide")

st.markdown("<h1 style='text-align: center; color: green;'>🔍 Dashboard Nutricional</h1>", unsafe_allow_html=True)
st.write("### Resumo geral das informações nutricionais.")

# Função para contar pacientes
def contar_pacientes():
    if os.path.exists("pacientes.json"):
        with open("pacientes.json", "r") as file:
            pacientes = json.load(file)
        return len(pacientes)
    return 0

# Função para contar consultas de hoje
def contar_consultas_hoje():
    if os.path.exists("agenda_consultas.json"):
        with open("agenda_consultas.json", "r") as file:
            consultas = json.load(file)
        hoje = datetime.date.today().strftime("%Y-%m-%d")
        return sum(1 for c in consultas if c["data"] == hoje)
    return 0

# Função para calcular média de IMC
def calcular_media_imc():
    if os.path.exists("pacientes.json"):
        with open("pacientes.json", "r") as file:
            pacientes = json.load(file)
        imcs = [p["imc"] for p in pacientes if "imc" in p and isinstance(p["imc"], (int, float))]
        if imcs:
            return round(sum(imcs)/len(imcs), 1)
    return 0

col1, col2, col3 = st.columns(3)
col1.metric("Pacientes Ativos", contar_pacientes())
col2.metric("Consultas Hoje", contar_consultas_hoje())
col3.metric("Média IMC", calcular_media_imc())

# Lista de Pacientes
st.write("""
### 👥 Lista de Pacientes
""")

if os.path.exists("pacientes.json"):
    with open("pacientes.json", "r") as file:
        pacientes = json.load(file)
    if pacientes:
        for p in pacientes:
            with st.expander(f"{p['nome']} - IMC: {p.get('imc', 'N/A')}"):
                st.write(f"**Idade:** {p.get('idade', 'N/A')}")
                st.write(f"**Peso:** {p.get('peso', 'N/A')} kg")
                st.write(f"**Altura:** {p.get('altura', 'N/A')} m")
                st.write(f"**Gênero:** {p.get('genero', 'N/A')}")
                if st.button(f"Excluir {p['nome']}", key=p['nome']):
                    pacientes = [pac for pac in pacientes if pac['nome'] != p['nome']]
                    with open("pacientes.json", "w") as f:
                        json.dump(pacientes, f, indent=4)
                    st.experimental_rerun()
    else:
        st.info("Nenhum paciente cadastrado ainda.")
else:
    st.info("Nenhum paciente cadastrado ainda.")

# Observações Relevantes
st.write("""
### 📌 Observações Relevantes
- Aumento no número de pacientes com sobrepeso.
- Alto consumo de ultraprocessados entre jovens.
- Maior adesão às dietas com baixo teor de carboidrato.
""")
