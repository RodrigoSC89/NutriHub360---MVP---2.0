import streamlit as st
import json
import os

st.set_page_config(page_title="Cardápio Recomendado", page_icon="🍱")
st.title("🍱 Cardápio Recomendado")

st.markdown("Sugestão de alimentação diária com base no perfil do paciente.")

# Carrega pacientes
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

# Cardápio baseado em IMC
imc = paciente.get("imc", 0)
st.subheader(f"Cardápio para {paciente['nome']} - IMC: {imc}")

if imc < 18.5:
    objetivo = "Ganho de peso"
    refeicoes = [
        ("Café da Manhã", "Vitamina com banana + pão integral com pasta de amendoim"),
        ("Almoço", "Arroz, feijão, carne vermelha, legumes refogados e abacate"),
        ("Lanche da Tarde", "Tapioca com queijo e suco natural"),
        ("Jantar", "Massa com frango, legumes e azeite")
    ]
elif imc < 25:
    objetivo = "Manutenção"
    refeicoes = [
        ("Café da Manhã", "Iogurte natural com granola e frutas vermelhas"),
        ("Almoço", "Arroz integral, feijão, frango grelhado, salada"),
        ("Lanche da Tarde", "Fruta + castanhas"),
        ("Jantar", "Sopa de legumes + ovo cozido")
    ]
else:
    objetivo = "Redução de peso"
    refeicoes = [
        ("Café da Manhã", "Ovos mexidos com espinafre + chá verde"),
        ("Almoço", "Frango grelhado, brócolis, quinoa, salada verde"),
        ("Lanche da Tarde", "Pepino + hummus"),
        ("Jantar", "Sopa detox + chá de camomila")
    ]

st.success(f"Objetivo nutricional: {objetivo}")

for titulo, descricao in refeicoes:
    st.markdown(f"### {titulo}")
    st.markdown(f"{descricao}")
