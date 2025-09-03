import streamlit as st

st.set_page_config(page_title="Cadastro de Paciente", page_icon="🧑‍⚕️")

st.title("🧑‍⚕️ Cadastro de Paciente")
st.write("Preencha os dados do paciente abaixo.")

with st.form("form_paciente"):
    nome = st.text_input("Nome completo")
    idade = st.number_input("Idade", min_value=0, max_value=120, step=1)
    sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
    peso = st.number_input("Peso (kg)", min_value=0.0, format="%.2f")
    altura = st.number_input("Altura (cm)", min_value=0.0, format="%.2f")
    objetivo = st.text_area("Objetivo nutricional")
    enviado = st.form_submit_button("Salvar paciente")

if enviado:
    st.success(f"✅ Paciente {nome} cadastrado com sucesso!")
