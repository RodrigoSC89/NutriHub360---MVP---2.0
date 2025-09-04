import streamlit as st

st.set_page_config(page_title="Cardápio Recomendado", page_icon="🍱")

st.title("🍱 Cardápio Recomendado")
st.write("Sugestão diária baseada em hábitos saudáveis.")

cardapio = {
    "Café da Manhã": ["Ovos mexidos", "Pão integral", "Mamão", "Café sem açúcar"],
    "Lanche da Manhã": ["Iogurte natural", "1 colher de chia"],
    "Almoço": ["Arroz integral", "Feijão", "Frango grelhado", "Salada de folhas verdes", "Legumes cozidos"],
    "Lanche da Tarde": ["Banana", "1 colher de pasta de amendoim"],
    "Jantar": ["Sopa de legumes", "Peito de frango desfiado"],
    "Ceia": ["Chá de camomila", "Queijo branco"]
}

for refeicao, itens in cardapio.items():
    st.subheader(f"🍽️ {refeicao}")
    for item in itens:
        st.markdown(f"- {item}")

st.success("Esse cardápio é apenas uma sugestão. Consulte um nutricionista para ajustes personalizados.")
