import streamlit as st
import matplotlib.pyplot as plt

st.title("🥗 Análise Alimentar")
st.markdown("Gráfico exemplo da distribuição de macronutrientes.")

labels = ['Carboidratos', 'Proteínas', 'Gorduras']
sizes = [50, 30, 20]
colors = ['#ff9999','#66b3ff','#99ff99']

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
st.pyplot(fig1)
