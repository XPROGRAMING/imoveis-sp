from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

with open('../data/modelo.pkl', 'rb') as f:
    modelo = pickle.load(f)

with open('../data/le_district.pkl', 'rb') as f:
    le_district = pickle.load(f)

with open('../data/le_type.pkl', 'rb') as f:
    le_type = pickle.load(f)

app = FastAPI(title='Previsão de Aluguel SP')


class Imovel(BaseModel):
    area: int
    bedrooms: int
    garage: int
    district: str
    type: str

@app.get('/')
def home():
    return {'status': 'API funcionando!'}

@app.post('/prever')
def prever(imovel: Imovel):
    district_enc = le_district.transform([imovel.district])[0]
    type_enc = le_type.transform([imovel.type])[0]

    features = np.array([[
        imovel.area,
        imovel.bedrooms,
        imovel.garage,
        district_enc,
        type_enc
    ]])

    aluguel = modelo.predict(features)[0]

    return {'aluguel_previsto': round(float(aluguel), 2)}