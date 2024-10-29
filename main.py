from fastapi import FastAPI, HTTPException
from services.previsao import Prever

import uvicorn

app = FastAPI(title="TechFinance ML")

@app.get('/previsao')
def previsao(produto: str):
    if not produto:
        raise HTTPException(status_code=400, detail="Produto não informado")

    prever = Prever(produto)
    previsao = prever.realizar_previsao('data/dados.xlsx')

    return previsao

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
