from Previsao import Prever
from flask import Flask, jsonify
import json as j

app = Flask(__name__)

# Função de previsão
produto = "CANECAS"
previsao = Prever(produto)
resultado = previsao.realizar_previsao()
print(resultado)
@app.route('/Previsao')
def obterPrevisao():
    return jsonify(resultado) 

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)


