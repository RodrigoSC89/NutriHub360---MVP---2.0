import streamlit as st

st.set_page_config(page_title="Cardápio Recomendado", page_icon="🍱")

st.title("🍱 Cardápio Recomendado")
st.write("Sugestão de alimentação diária com base no plano nutricional do paciente.")

refeicoes = {
    "Café da Manhã": "Ovos mexidos, pão integral, mamão e café sem açúcar",
    "Lanche da Manhã": "Iogurte natural com chia",
    "Almoço": "Arroz integral, feijão, frango grelhado, salada de folhas e legumes cozidos",
    "Lanche da Tarde": "Banana com pasta de amendoim",
    "Jantar": "Sopa de legumes com carne magra",
    "Ceia": "Chá de camomila e uma fatia de queijo branco"
}

st.markdown("---")

for refeicao, descricao in refeicoes.items():
    st.subheader(f"🍽️ {refeicao}")
    st.markdown(f"- {descricao}")

st.success("Cardápio exibido com sucesso!")
