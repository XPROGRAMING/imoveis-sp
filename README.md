# 🏘️ Previsão de Aluguel em São Paulo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://imoveis-sp-ubbxtoshtzr8j94t4euutz.streamlit.app)

> Dado um imóvel com determinadas características, qual deveria ser o valor justo do aluguel? Esse projeto responde essa pergunta com Machine Learning, uma API REST e um dashboard interativo.

---

## 🚀 Demo ao vivo

👉 [https://imoveis-sp-ubbxtoshtzr8j94t4euutz.streamlit.app](https://imoveis-sp-ubbxtoshtzr8j94t4euutz.streamlit.app)

---

## 📌 Sobre o projeto

O mercado imobiliário de São Paulo é complexo e cheio de variações — o aluguel de um apartamento de 60m² pode variar centenas de reais dependendo do bairro, do número de quartos ou da disponibilidade de garagem.

O objetivo desse projeto foi construir um pipeline completo de dados: desde a análise exploratória até uma aplicação funcionando em produção, capaz de estimar o valor de aluguel de um imóvel com base em suas características.

---

## 🗂️ Etapas do projeto

### 1. Análise Exploratória de Dados (EDA)

O dataset contém **11.657 registros** de imóveis para aluguel em São Paulo, com as seguintes variáveis:

| Variável | Descrição |
|---|---|
| `district` | Bairro do imóvel |
| `area` | Área em m² |
| `bedrooms` | Número de quartos |
| `garage` | Vagas de garagem |
| `type` | Tipo do imóvel |
| `rent` | Valor do aluguel (target) |

Principais descobertas da análise:

- A **mediana do aluguel** é R$ 2.415 — bem abaixo da média de R$ 3.250, o que indica a presença de imóveis muito caros puxando a média para cima
- Bairros como **Jardins, Itaim Bibi e Moema** concentram os aluguéis mais altos
- A **área** é a variável com maior correlação com o preço, seguida pelo número de quartos
- O dataset não apresentou valores nulos em nenhuma coluna

---

### 2. Limpeza e tratamento dos dados

- Remoção de outliers extremos via percentil 1% e 99%
- Eliminação de duplicatas
- Dataset final: **11.425 registros** prontos para modelagem

---

### 3. Feature Engineering e Modelagem

As variáveis categóricas `district` e `type` foram transformadas com `LabelEncoder`. O modelo escolhido foi o **Random Forest Regressor**, por lidar melhor com a não-linearidade dos dados de imóveis do que a regressão linear tradicional.

Divisão dos dados:
- **Treino:** 9.140 registros (80%)
- **Teste:** 2.285 registros (20%)

Resultados:

| Métrica | Valor |
|---|---|
| MAE | R$ 1.019 |
| R² | 0.55 |

O modelo explica 55% da variação dos preços, com erro médio de R$ 1.019 por previsão — base sólida para evoluções futuras com feature engineering mais avançado.

---

### 4. API REST com FastAPI

Uma API foi desenvolvida com **FastAPI**, expondo um endpoint que recebe os dados do imóvel e retorna a previsão de aluguel.

**Endpoint:**
```
POST /prever
```

**Exemplo de requisição:**
```json
{
  "area": 60,
  "bedrooms": 2,
  "garage": 1,
  "district": "Moema",
  "type": "Apartamento"
}
```

**Resposta:**
```json
{
  "aluguel_previsto": 3731.57
}
```

A documentação interativa da API está disponível em `/docs` via Swagger UI gerado automaticamente pelo FastAPI.

---

### 5. Dashboard interativo com Streamlit

Um dashboard foi desenvolvido com **Streamlit**, permitindo que qualquer pessoa consulte a previsão de aluguel de forma visual e intuitiva — sem precisar escrever nenhuma linha de código.

O usuário seleciona o bairro, tipo de imóvel, área, quartos e vagas, e recebe instantaneamente a estimativa de aluguel.

🔗 [Acessar o dashboard](https://imoveis-sp-ubbxtoshtzr8j94t4euutz.streamlit.app)

---

## 🛠️ Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

---

## 📁 Estrutura do projeto

```
imoveis-brasil/
│
├── data/
│   ├── imoveis.csv           ← dataset original
│   └── imoveis_clean.csv     ← dataset após limpeza
│
├── notebooks/
│   ├── 01_eda.ipynb          ← análise exploratória
│   └── 02_modelo.ipynb       ← feature engineering e modelagem
│
├── api/
│   └── main.py               ← API FastAPI
│
├── app/
│   └── dashboard.py          ← dashboard Streamlit
│
└── requirements.txt
```

---

## 📬 Contato

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/michael-de-oliveira-962471195/)
