import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import json

st.set_page_config(page_title="Análise Alimentar", layout="wide")
st.title("🍽 Análise Alimentar")
st.markdown("Visualize e interprete a ingestão alimentar do paciente.")

# Carrega os pacientes
if os.path.exists("pacientes.json"):
    with open("pacientes.json", "r") as f:
        pacientes = json.load(f)
else:
    pacientes = []

nomes = [p["nome"] for p in pacientes]

if not nomes:
    st.warning("Nenhum paciente cadastrado.")
    st.stop()

selecionado = st.selectbox("Selecione o paciente:", nomes)
paciente = next(p for p in pacientes if p["nome"] == selecionado)

st.subheader("Macronutrientes (valores simulados)")
# Simula macros - ideal: usar dados reais futuramente
macros = {
    "Carboidratos": round(paciente["peso"] * 4),
    "Proteínas": round(paciente["peso"] * 2),
    "Gorduras": round(paciente["peso"] * 1),
    "Fibras": 25
}

df = pd.DataFrame(macros.items(), columns=["Nutriente", "Gramas"])
fig, ax = plt.subplots()
colors = ["#FFD700", "#FF8C00", "#DC143C", "#32CD32"]
ax.bar(df["Nutriente"], df["Gramas"], color=colors)
ax.set_ylabel("Gramas")
ax.set_title("Distribuição dos Macronutrientes")
for i, v in enumerate(df["Gramas"]):
    ax.text(i, v + 1, str(v), ha='center')
st.pyplot(fig)

# Calorias
cal = macros["Carboidratos"]*4 + macros["Proteínas"]*4 + macros["Gorduras"]*9
st.metric("Estimativa calórica", f"{cal} kcal")
