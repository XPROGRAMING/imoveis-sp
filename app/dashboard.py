import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@st.cache_resource
def carregar_modelo():
    df = pd.read_csv(os.path.join(BASE_DIR, 'data', 'imoveis_clean.csv'))
    
    le_district = LabelEncoder()
    le_type = LabelEncoder()
    
    df['district_enc'] = le_district.fit_transform(df['district'])
    df['type_enc'] = le_type.fit_transform(df['type'])
    
    X = df[['area', 'bedrooms', 'garage', 'district_enc', 'type_enc']]
    y = df['rent']
    
    modelo = RandomForestRegressor(n_estimators=100, random_state=42)
    modelo.fit(X, y)
    
    return modelo, le_district, le_type, df

st.set_page_config(page_title='Previsão de Aluguel SP', page_icon='🏘️', layout='centered')
st.title('🏘️ Previsão de Aluguel em São Paulo')
st.markdown('Preencha as características do imóvel para estimar o valor do aluguel.')

with st.spinner('Carregando modelo...'):
    modelo, le_district, le_type, df = carregar_modelo()

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

if st.button('Estimar aluguel', type='primary', use_container_width=True):
    district_enc = le_district.transform([bairro])[0]
    type_enc = le_type.transform([tipo])[0]
    
    features = np.array([[area, bedrooms, garage, district_enc, type_enc]])
    aluguel = modelo.predict(features)[0]
    
    st.success(f'### Aluguel estimado: R$ {aluguel:,.2f} / mês')
    st.caption('Estimativa baseada em dados históricos de imóveis em São Paulo.')