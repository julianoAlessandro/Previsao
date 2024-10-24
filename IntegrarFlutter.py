import pandas as pd
from prophet import Prophet
from flask import Flask, request, jsonify

app = Flask(__name__)

class Prever:
    def __init__(self, produto):
        self.produto = produto

    def realizar_previsao(self):
        # Carregar dados do Excel
        df = pd.read_excel(r'C:\Users\guilh\Documents\ModeloPrevisao\Dados.xlsx')
        df = df.drop(columns=['Unnamed: 0'])
        df = df.drop(index=4)

        # Filtrar os dados para o produto escolhido
        df_produto = df[df['produto'] == self.produto].copy()

        # Renomear colunas para o formato do Prophet
        df_produto = df_produto.rename(columns={'Mes': 'ds', 'total': 'y'})
        df_produto['ds'] = pd.to_datetime('2024-' + df_produto['ds'].astype(str) + '-01')

        # Criar e ajustar o modelo Prophet
        modelo = Prophet()
        modelo.fit(df_produto[['ds', 'y']])

        # Criar dataframe de datas futuras para prever
        dados_futuros = modelo.make_future_dataframe(periods=4, freq='M')  # Prever para os próximos 4 meses

        # Fazer previsões
        previsao = modelo.predict(dados_futuros)

        # Guardando em um DataFrame
        df_fut = previsao[['ds', 'yhat']].tail(4)  # Obter as últimas 4 previsões

        # Renomeando colunas
        df_fut = df_fut.rename(columns={'ds': 'Data', 'yhat': 'Previsão'})

        # Ajustando casas decimais
        df_fut['Previsão'] = round(df_fut['Previsão'], 2)

        return df_fut.to_dict(orient='records')  # Retorna como uma lista de dicionários

@app.route('/previsao', methods=['POST'])
def previsao_api():
    data = request.json
    produto = data.get('produto')

    if not produto:
        return jsonify({'error': 'Produto não fornecido'}), 400

    prever = Prever(produto)
    previsao = prever.realizar_previsao()

    return jsonify(previsao)

if __name__ == '__main__':
    app.run(debug=True)
