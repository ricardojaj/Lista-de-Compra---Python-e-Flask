# Lista de Compras - Python e Flask

Este é um projeto de uma API de Lista de Compras utilizando Python e Flask, com integração ao Supabase para gerenciamento de dados.

## Requisitos

- Python 3.12 ou superior
- Flask
- Supabase
- python-dotenv

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/ricardojaj/Lista-de-Compra---Python-e-Flask.git
   cd Lista-de-Compra---Python-e-Flask
   ```

2. Crie um ambiente virtual e ative-o:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Execute a aplicação:

   ```bash
   python app.py
   ```

2. Acesse a API

## Endpoints

### Visualizar Lista de Compras

- **URL:** `/shopping_list/view`
- **Método:** `GET`
- **Descrição:** Retorna todos os produtos na lista de compras.

### Adicionar Produto

- **URL:** `/shopping_list/add`
- **Método:** `POST`
- **Descrição:** Adicionar um produto na lista de compras pelo `product_id`.

### Deletar Produto

- **URL:** `/shopping_list/delete/<int:product_id>`
- **Método:** `DELETE`
- **Descrição:** Deleta um produto da lista de compras pelo `product_id`.

## Exemplo de Respostas

### Visualizar Lista de Compras

**Resposta de Sucesso:**

```json
[
  {
    "id": 1,
    "name": "Produto 1",
    "quantity": 2,
    "unitPrice": 3
  },
  {
    "id": 2,
    "name": "Produto 2",
    "quantity": 1,
    "unitPrice": 3.5
  }
]
```

# Testes

Este projeto inclui testes unitários para garantir o correto funcionamento das principais funcionalidades. Para executar os testes, siga os passos abaixo.

1. Execute os testes

   ```bash
   pytest
   ```

Os testes de API foram criados no Postman e estão disponíveis na pasta postman_tests/. Para executá-los:

1. Importe a coleção do Postman (postman_tests/shopping_list_collection.json) no Postman
2. Execute os testes pelo próprio Postman.
