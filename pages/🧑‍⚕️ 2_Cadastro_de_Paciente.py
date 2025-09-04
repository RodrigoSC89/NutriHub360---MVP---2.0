import streamlit as st
import json
import os

st.set_page_config(page_title="Cadastro de Paciente", page_icon="🧑‍⚕️")

st.title("🧑‍⚕️ Cadastro de Paciente")
st.write("Preencha os dados abaixo para adicionar um novo paciente.")

PACIENTES_FILE = "pacientes.json"

# Carregar pacientes
def carregar_pacientes():
    if os.path.exists(PACIENTES_FILE):
        with open(PACIENTES_FILE, "r") as f:
            return json.load(f)
    return []

# Salvar pacientes
def salvar_pacientes(pacientes):
    with open(PACIENTES_FILE, "w") as f:
        json.dump(pacientes, f, indent=4)

pacientes = carregar_pacientes()

with st.form("form_cadastro"):
    nome = st.text_input("Nome completo")
    idade = st.number_input("Idade", min_value=0, max_value=120)
    genero = st.selectbox("Gênero", ["Masculino", "Feminino", "Outro"])
    peso = st.number_input("Peso (kg)", min_value=0.0)
    altura = st.number_input("Altura (m)", min_value=0.0, step=0.01)
    enviado = st.form_submit_button("Cadastrar")

if enviado:
    if nome and peso > 0 and altura > 0:
        imc = round(peso / (altura ** 2), 1)
        novo_paciente = {
            "nome": nome,
            "idade": idade,
            "genero": genero,
            "peso": peso,
            "altura": altura,
            "imc": imc
        }
        pacientes.append(novo_paciente)
        salvar_pacientes(pacientes)
        st.success(f"Paciente {nome} cadastrado com sucesso! IMC: {imc}")
    else:
        st.warning("Por favor, preencha todos os campos corretamente.")

# Mostrar pacientes cadastrados
if pacientes:
    st.subheader("📋 Pacientes Cadastrados")
    for p in pacientes:
        st.markdown(f"**{p['nome']}** - {p['idade']} anos - IMC: {p['imc']}")
else:
    st.info("Nenhum paciente cadastrado ainda.")
