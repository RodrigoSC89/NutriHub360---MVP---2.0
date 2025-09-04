# NutriHub360 — Sistema de Gestão Nutricional

Este é um sistema completo para nutricionistas, desenvolvido com Streamlit, para gerenciar pacientes, registrar consultas, acompanhar evolução nutricional, montar cardápios e gerar relatórios profissionais. O sistema também permite o agendamento de consultas, controle de login e geração de PDFs.

## ✅ Funcionalidades Principais

### 1. Login de Usuário
- Tela de autenticação para segurança do sistema.
- Acesso restrito às funcionalidades para usuários autorizados.
- Autenticação simples via arquivo `usuarios.json` (ou similar).

### 2. Dashboard Nutricional
- Visão geral com:
  - Total de pacientes ativos (dados reais)
  - Número de consultas agendadas no dia
  - Média do IMC dos pacientes cadastrados
- Lista de pacientes com botões para exclusão
- Observações automáticas com base em tendências do banco de dados

### 3. Cadastro de Pacientes
- Registro de informações pessoais (nome, idade, peso, altura, etc.)
- Cálculo automático do IMC
- Armazenamento em banco de dados local (`pacientes.json`)

### 4. Registro de Consultas
- Seleção de paciente já cadastrado
- Registro de:
  - Queixa principal
  - Diagnóstico
  - Conduta nutricional
  - Observações e recomendações
- Registro da data e hora atual

### 5. Agendamento de Consultas
- Agenda integrada por paciente
- Marcação de data e horário para futuras consultas
- Visualização da agenda no dashboard
- Armazenamento no arquivo `agenda.json`

### 6. Análise Alimentar
- Visualização de ingestão de macronutrientes por paciente:
  - Carboidratos, proteínas, gorduras, fibras
- Gráficos de barras coloridos com `matplotlib`

### 7. Cardápio Recomendado
- Sugestão de plano alimentar diário baseado no perfil do paciente
- Separação por refeições: café da manhã, almoço, jantar, etc.
- Adaptação automática conforme o IMC ou restrições

### 8. Biblioteca Nutricional
- Artigos, dicas e links úteis para pacientes
- Materiais educativos salvos diretamente na interface
- Expansível com novos conteúdos

### 9. Evolução do Paciente
- Gráficos com evolução de peso e IMC ao longo do tempo
- Registro histórico automático após cada consulta
- Visualização interativa com `plotly`

### 10. Geração de Relatórios
- Geração de PDFs com dados completos do paciente
- Inclui histórico, diagnósticos e plano alimentar
- Utiliza biblioteca `fpdf`

## 📁 Estrutura de Pastas
```
├── Home.py
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Cadastro_de_Paciente.py
│   ├── 3_Registro_Consulta.py
│   ├── 4_Analise_Alimentar.py
│   ├── 5_Cardapio_Recomendado.py
│   ├── 6_Biblioteca_Nutricional.py
│   ├── 7_Agenda_Consultas.py
│   ├── 8_Gerar_Relatorio.py
│   └── 9_Evolucao_Paciente.py
├── database/
│   ├── pacientes.json
│   ├── consultas.json
│   ├── agenda.json
│   └── usuarios.json
├── requirements.txt
├── README.md
└── logo.png
```

## ▶️ Como Executar Localmente
```bash
# Clone o repositório
git clone https://github.com/seuusuario/nutrihub360.git
cd nutrihub360

# Instale as dependências
pip install -r requirements.txt

# Rode o app com Streamlit
streamlit run Home.py
```

## ☁️ Publicação no Streamlit Cloud
1. Crie um repositório no GitHub com todos os arquivos.
2. Vá para [https://streamlit.io/cloud](https://streamlit.io/cloud).
3. Clique em "Deploy an app" e selecione seu repositório.
4. Escolha `Home.py` como arquivo principal.

## 🧩 Requisitos
- Python 3.10+
- Streamlit >= 1.35.0
- matplotlib, pandas, numpy, plotly, fpdf, watchdog

## 📝 Licença
Este projeto é livre para uso pessoal e educacional.

