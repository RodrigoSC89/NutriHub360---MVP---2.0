[readme.md](https://github.com/user-attachments/files/22129474/readme.md)
# 🥗 NutriHub360

Sistema completo para nutricionistas gerenciarem pacientes, consultas e planos alimentares de forma simples e eficiente.

## ✅ Funcionalidades

- 📊 Dashboard com resumo geral
- 👤 Cadastro de pacientes com cálculo de IMC
- 📝 Registro de consultas e histórico
- 🍽️ Análise alimentar com gráficos
- 🍱 Cardápio recomendado com base no IMC
- 📅 Agenda de consultas com exclusão
- 📚 Biblioteca com uploads de materiais

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/nutrihub360.git
cd nutrihub360
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Rode o app com Streamlit
```bash
streamlit run app.py
```

---

## 📁 Estrutura do projeto
```
📦 nutrihub360
├── app.py                  # Arquivo principal
├── logo.png                # Logo exibida na home
├── requirements.txt        # Dependências
├── README.md               # Instruções e informações
├── pacientes.json          # Cadastro de pacientes
├── agenda_consultas.json   # Agenda de consultas (auto gerado)
├── consultas.csv           # Histórico de consultas
└── pages/                  # Páginas do Streamlit
    ├── 1_Dashboard.py
    ├── 2_Cadastro_de_Paciente.py
    ├── 3_Registro_Consulta.py
    ├── 4_Analise_Alimentar.py
    ├── 5_Cardapio_Recomendado.py
    └── 6_Biblioteca_Nutricional.py
```

---

## 💡 Sugestões futuras
- Login com autenticação segura
- Área do paciente com acesso restrito
- Exportação de relatórios em PDF
- Integração com APIs de alimentos e calendários

---

## 👨‍⚕️ Desenvolvido por
NutriXpert 360° – seu parceiro digital na nutrição! 🍎

---

### 📢 Compartilhe e contribua!
Se esse projeto te ajudou, ⭐ no repositório e compartilhe com colegas da nutrição!

---

*Versão MVP 1.0 – atualize conforme evoluir o sistema.*

