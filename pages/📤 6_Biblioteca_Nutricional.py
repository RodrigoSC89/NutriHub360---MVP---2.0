import streamlit as st

st.set_page_config(page_title="Biblioteca Nutricional", page_icon="📚")

st.title("📚 Biblioteca Nutricional")

st.markdown("""
Explore conteúdos educativos sobre nutrição para você e seus pacientes.

### 📘 Materiais disponíveis:
- Guia Alimentar para a População Brasileira
- Tabela TACO de composição de alimentos
- Artigos científicos recentes
- E-books sobre dietas, emagrecimento, saúde e performance

---
**Dica:** Você pode adicionar arquivos PDF, links ou vídeos nesta página!
""")

# Área para uploads
st.subheader("📤 Upload de materiais próprios")
uploaded_file = st.file_uploader("Envie um material (PDF, imagem, etc)", type=["pdf", "png", "jpg"])
if uploaded_file is not None:
    st.success(f"Arquivo {uploaded_file.name} enviado com sucesso! (ainda não salvo permanentemente)")
    if uploaded_file.type == "application/pdf":
        st.download_button("📥 Baixar PDF", uploaded_file, file_name=uploaded_file.name)
    else:
        st.image(uploaded_file.read(), caption=uploaded_file.name)
