from fastapi import FastAPI, HTTPException

from services.previsao import Prever

app = FastAPI(title="TechFinance ML")

@app.get('/previsao')
def previsao(produto: str):
    if not produto:
        raise HTTPException(status_code=400, detail="Produto não informado")

    prever = Prever(produto)
    previsao = prever.realizar_previsao('data/dados.xlsx')

    return previsao
