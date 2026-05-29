import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Carrega o modelo e os encoders
with open('../data/modelo.pkl', 'rb') as f:
    modelo = pickle.load(f)

with open('../data/le_district.pkl', 'rb') as f:
    le_district = pickle.load(f)

with open('../data/le_type.pkl', 'rb') as f:
    le_type = pickle.load(f)


df = pd.read_csv('../data/imoveis_clean.csv')


st.set_page_config(page_title='Previsão de Aluguel SP', page_icon='🏘️', layout='centered')

st.title('🏘️ Previsão de Aluguel em São Paulo')
st.markdown('Preencha as características do imóvel para estimar o valor do aluguel.')
st.divider()

col1, col2 = st.columns(2)

with col1:
    area = st.number_input('Área (m²)', min_value=10, max_value=600, value=60)
    bedrooms = st.number_input('Quartos', min_value=0, max_value=6, value=2)

with col2:
    garage = st.number_input('Vagas de garagem', min_value=0, max_value=6, value=1)
    tipo = st.selectbox('Tipo do imóvel', sorted(df['type'].unique().tolist()))

bairro = st.selectbox('Bairro', sorted(df['district'].unique().tolist()))

st.divider()

#
if st.button('Estimar aluguel', type='primary', use_container_width=True):
    district_enc = le_district.transform([bairro])[0]
    type_enc = le_type.transform([tipo])[0]

    features = np.array([[area, bedrooms, garage, district_enc, type_enc]])
    aluguel = modelo.predict(features)[0]

    st.success(f'### Aluguel estimado: R$ {aluguel:,.2f} / mês')
    st.caption('Estimativa baseada em dados históricos de imóveis em São Paulo.')