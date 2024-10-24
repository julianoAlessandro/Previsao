import pandas as pd
from prophet import Prophet

class Prever:
    def __init__(self, produto):
        self.produto = produto

    def realizar_previsao(self):
        # Carregar dados do Excel
        df = pd.read_excel(r'C:\Users\Juliano\Downloads\ModeloPrevisao02\ModeloPrevisao\Dados.xlsx')
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
        df_fut = df_fut.rename(columns={'ds': 'Data', 'yhat': 'Previsao'})

        # Ajustando casas decimais
        df_fut['Previsao'] = round(df_fut['Previsao'], 2)
        
        #Convertendo para Data
        #df_fut['Data'] = pd.to_datetime(df_fut['Data'], format="%d/%m/%Y", unit='ms').dt.date
        df_fut['Data'] = df_fut['Data'].dt.strftime('%Y-%m-%d')

        # Transformar em JSON
        df_fut_json = df_fut.to_json(orient="records", index=False)
        print(type(df_fut_json))
             
        # Retornar as previsões como JSON
        return df_fut_json
