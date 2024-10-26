# TechFinance ML

TechFinance ML é uma aplicação desenvolvida com FastAPI para realizar previsões financeiras utilizando a biblioteca Prophet.

## Funcionalidades

- Previsão de vendas de produtos com base em dados históricos.

## Endpoints

### `GET /previsao`

Retorna a previsão de vendas para um produto específico.

**Parâmetros:**

- `produto` (str): Nome do produto para o qual a previsão será realizada.

**Exemplo de Requisição:**

```bash
curl -X 'GET' \
    'http://127.0.0.1:8000/previsao?produto=ProdutoX' \
    -H 'accept: application/json'
```

**Exemplo de Resposta:**

```json
[
    {
        "Data": "2024-05-01",
        "Previsão": 123.45
    },
    {
        "Data": "2024-06-01",
        "Previsão": 234.56
    },
    {
        "Data": "2024-07-01",
        "Previsão": 345.67
    },
    {
        "Data": "2024-08-01",
        "Previsão": 456.78
    }
]
```

## Estrutura do Projeto

- `main.py`: Contém a definição da API e o endpoint `/previsao`.
- `services/previsao.py`: Contém a classe `Prever` responsável por carregar os dados, ajustar o modelo Prophet e realizar as previsões.

## Como Executar

1. Clone o repositório:
        ```bash
        git clone https://github.com/seu-usuario/techfinance-ml.git
        cd techfinance-ml
        ```

2. Crie um ambiente virtual e instale as dependências:
        ```bash
        python -m venv venv
        source venv/bin/activate  # No Windows use `venv\Scripts\activate`
        pip install -r requirements.txt
        ```

3. Execute a aplicação:
        ```bash
        uvicorn main:app --reload
        ```

4. Acesse a documentação interativa da API em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Dependências

- FastAPI
- pandas
- prophet
- openpyxl

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

