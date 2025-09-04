import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import os

st.set_page_config(page_title="Análise Alimentar", page_icon="🍽️")
st.title("🍽️ Análise Alimentar")

# Dados simulados de macronutrientes (em gramas)
macros = {
    "Carboidratos": 270,
    "Proteínas": 110,
    "Gorduras": 80,
    "Fibras": 25
}

# Gráfico de barras
st.subheader("📊 Distribuição dos Macronutrientes")
fig, ax = plt.subplots()
ax.bar(macros.keys(), macros.values(), color=['#F4A261', '#2A9D8F', '#E76F51', '#8AB17D'])
ax.set_ylabel("Gramas por dia")
ax.set_title("Consumo diário estimado")
st.pyplot(fig)

# Cálculo de calorias
calorias = macros['Carboidratos'] * 4 + macros['Proteínas'] * 4 + macros['Gorduras'] * 9
st.metric("Estimativa calórica diária", f"{calorias} kcal")

st.markdown("---")

st.subheader("💡 Recomendações")
st.markdown("""
- Reduzir o consumo de gorduras saturadas.
- Aumentar a ingestão de fibras (mínimo 30g/dia).
- Manter proporção equilibrada entre os macronutrientes.
""")
