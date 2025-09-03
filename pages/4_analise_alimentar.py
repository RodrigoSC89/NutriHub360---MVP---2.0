import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Análise Alimentar", layout="wide")
st.title("🍽️ Análise Alimentar")
st.write("Visualize e interprete a ingestão alimentar do paciente.")

# Simulação de dados alimentares
alimentos = ["Carboidratos", "Proteínas", "Gorduras", "Fibras"]
quantidades = [250, 100, 70, 30]  # em gramas

# Gráfico de barras
fig, ax = plt.subplots()
bars = ax.bar(alimentos, quantidades, color=['#FFD700', '#FF8C00', '#DC143C', '#32CD32'])
ax.set_ylabel("Gramas")
ax.set_title("Distribuição dos Macronutrientes")

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 2, yval, ha='center', va='bottom')

st.pyplot(fig)

# Análise textual simples
st.markdown("---")
st.subheader("📊 Interpretação")
st.info("A ingestão de proteínas está dentro do ideal, porém recomenda-se reduzir levemente o consumo de carboidratos e gorduras.")