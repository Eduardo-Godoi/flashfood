# FLASHFOOD 🍟

FlashFood é um sistema desenvolvido para que pessoas possam encontrar Restaurantes, Pizzarias Hamburguerias... proximo ao seu endereço, e assim realizar um pedido no estabelecimento desejado.

O sistema possui 2 tipos de usuarios, sendo eles:

- Partner
- Customer

PARTNER:
tem permissão para listar suas lojas, cadastrar uma loja e atualizar ou deletar uma loja específica

CUSTOMER:
tem permissão para listar as lojas próximas a seu endereço realizar um pedido e deixar um feedback em uma loja parceira após ter realizado um pedido

## **_Como Instalar?_**

- Para instalar, é necessário clonar o projeto e fazer instalação das dependências.

### Clonando o Projeto:

```
git clone https://gitlab.com/eduardogodoi/flashfood
```

### Depois de clonado entre na pasta do projeto:

```
cd flashfood
```

### Crie um ambiente virtual venv:

```
python -m veen venv
```

Depois de criado o ambiente virtual basta entrar

```
source venv/bin/activate
```

### Instalando as Dependências:

```
pip install -r requirements.txt
```

### Para Iniciar a aplicação rode o comando abaixo:

```
python manage.py runserver

ou

./manage.py runserver
```

# Rotas da Aplicação:

### `POST /api/accounts/` - Rota de criação de novos usuários.

```json
// REQUEST
{
  "username": "user",
  "password": "1234",
  "first_name": "Joze",
  "last_name": "souza",
  "is_superuser": false,
  "street": "R. morumbi",
  "district": "Bela Vista",
  "number": 2266
}
```

```json
// RESPONSE STATUS -> HTTP 201 CREATED
{
  "id": 1,
  "username": "user",
  "first_name": "Joze",
  "last_name": "souza",
  "is_superuser": false
}
```

### `POST /api/login/` - Rota de login

```json
// REQUEST
{
  "username": "user",
  "password": "1234"
}
```

```json
// RESPONSE STATUS -> HTTP 200 OK
{
  "token": "cda8275086e08547b3c26f2fe2c703b8845c8e1f"
}
```

### `POST /api/stor/` - Cadastrar Stor

```json
// REQUEST
// Header -> Authorization: Token <token-do-partner>
{
  "name": "Casa do Peixe",
  "category": "Peixaria",
  "street": "Av. das Figueiras",
  "district": "St. Comercial",
  "number": 329,
  "city": "Sinop",
  "state": "MT",
  "cep": "78550-000"
}
```

```json
// RESPONSE STATUS -> HTTP 201 CREATED
{
  "id": 15,
  "name": "Casa do Peixe",
  "category": {
    "id": 4,
    "name": "Peixaria"
  },
  "owner": {
    "id": 12,
    "username": "partner99",
    "first_name": "João",
    "last_name": "Veiga",
    "is_superuser": true
  },
  "adress": {
    "id": 28,
    "street": "Av. das Figueiras",
    "district": "St. Comercial",
    "number": 329,
    "city": "Sinop",
    "state": "MT",
    "cep": "78550-000"
  }
}
```

### `GET /api/stor/` - Listar Stor

- Caso o Partner esteja autenticado, será listado todas as sua lojas

```json
// REQUEST
// Header -> Authorization: Token <token-do-partner>
  {
    "id": 9,
    "name": "Restaurante lua",
    "category": {
      "id": 1,
      "name": "Restaurante"
    },
    "adress": {
      "id": 22,
      "street": "Rua João Pedro Moreira de Carvalho",
      "district": "St. Industrial",
      "number": 165,
      "city": "Sinop",
      "state": "MT",
      "cep": "78557-527"
    }
  },
  {
    "id": 14,
    "name": "Restaurante Itaubas",
    "category": {
      "id": 1,
      "name": "Restaurante"
    },
    "adress": {
      "id": 27,
      "street": "Av. das Itúbas",
      "district": "St. Comercial",
      "number": 4001,
      "city": "Sinop",
      "state": "MT",
      "cep": "78550-170"
    }
  }

```

- Caso a requisição seja feita sem autenticação será retornado todas as lojas parceiras

```json
// RESPONSE STATUS -> HTTP 200 OK

  {
    "id": 9,
    "name": "Restaurante lua",
    "category": {
      "id": 1,
      "name": "Restaurante"
    },
    "owner": {
      "id": 12,
      "username": "partner99",
      "first_name": "João",
      "last_name": "Veiga",
      "is_superuser": true
    },
    "adress": {
      "id": 22,
      "street": "Rua João Pedro Moreira de Carvalho",
      "district": "St. Industrial",
      "number": 165,
      "city": "Sinop",
      "state": "MT",
      "cep": "78557-527"
    }
  },
  {
    "id": 14,
    "name": "Restaurante Itaubas",
    "category": {
      "id": 1,
      "name": "Restaurante"
    },
    "owner": {
      "id": 12,
      "username": "partner99",
      "first_name": "João",
      "last_name": "Veiga",
      "is_superuser": true
    },
    "adress": {
      "id": 27,
      "street": "Av. das Itúbas",
      "district": "St. Comercial",
      "number": 4001,
      "city": "Sinop",
      "state": "MT",
      "cep": "78550-170"
    }
  },
  {
    "id": 15,
    "name": "Casa do Peixe",
    "category": {
      "id": 4,
      "name": "Peixaria"
    },
    "owner": {
      "id": 12,
      "username": "partner01",
      "first_name": "Nilton",
      "last_name": "Veiga",
      "is_superuser": true
    },
    "adress": {
      "id": 28,
      "street": "Av. das Nacional",
      "district": "St. Comercial",
      "number": 3229,
      "city": "Sinop",
      "state": "MT",
      "cep": "78550-777"
    }
  }
```

### `GET /api/stor/<int:pk>/` - Buscar Stor poi ID

```json
// REQUEST
// Header -> Authorization: Token <token-do-partner>

```

```json
// RESPONSE STATUS -> HTTP 200 OK
{
  "id": 9,
  "name": "Restaurante lua",
  "category": {
    "id": 1,
    "name": "Restaurante"
  },
  "owner": {
    "id": 12,
    "username": "partner99",
    "first_name": "João",
    "last_name": "Veiga",
    "is_superuser": true
  },
  "adress": {
    "id": 22,
    "street": "Rua João Pedro Moreira de Carvalho",
    "district": "St. Industrial",
    "number": 165,
    "city": "Sinop",
    "state": "MT",
    "cep": "78557-527"
  }
}
```

### `PUT /api/stor/<int:pk>/` - Atualizar Stor

```json
// REQUEST
// Header -> Authorization: Token <token-do-partner>
{
  "name": "Casa do Peixe 1",
  "category": "Peixaria",
  "street": "Av. das Figueiras",
  "district": "St. Comercial",
  "number": 329,
  "city": "Sinop",
  "state": "MT",
  "cep": "78550-000"
}
```

```json
// RESPONSE STATUS -> HTTP 200 OK
{
  "id": 9,
  "name": "Casa do Peixe",
  "category": {
    "id": 4,
    "name": "Peixaria"
  },
  "owner": {
    "id": 12,
    "username": "partner99",
    "first_name": "João",
    "last_name": "Veiga",
    "is_superuser": true
  },
  "adress": {
    "id": 22,
    "street": "Av. das Figueiras",
    "district": "St. Comercial",
    "number": 329,
    "city": "Sinop",
    "state": "MT",
    "cep": "78550-000"
  }
}
```

### `DELETE /api/stor/<int:pk>/` - Deletar Stor

```json
// REQUEST
// Header -> Authorization: Token <token-do-partner>
```

```json
// RESPONSE STATUS -> HTTP 204 NO CONTENT
```

### `GET /api/stor?category=pizzaria/` - Listar Stor por categoria

```json
// REQUEST
// Header -> Authorization: Token <token-do-partner>
```

```json
// RESPONSE STATUS -> HTTP 200 OK
{
  "id": 14,
  "name": "Pizzaria Itaubas",
  "category": {
    "id": 1,
    "name": "Pizzaria"
  },
  "owner": {
    "id": 12,
    "username": "partner99",
    "first_name": "João",
    "last_name": "Veiga",
    "is_superuser": true
  },
  "adress": {
    "id": 27,
    "street": "Av. das Itúbas",
    "district": "St. Comercial",
    "number": 4001,
    "city": "Sinop",
    "state": "MT",
    "cep": "78550-170"
  }
}
```

### `GET /api/stor/<stor_id>/products/` - Listar produtos de uma Stor

```json
// REQUEST
// Header -> Authorization: Token <token-do-partner-or-client>
```

```json
// RESPONSE STATUS -> HTTP 200 OK
  {
    "id": 1,
    "name": "Pastel de frango",
    "price": 7.99,
    "category":{
      "name": "Food"
    }
  },
  {
    "id": 5,
    "name": "Pastel de Carne",
    "price": 8.99,
    "category":{
      "name": "Food"
    }
  }
```

### `POST /api/<stor_id>/product/` - Cadastrar Produto

```json
// REQUEST
// Header -> Authorization: Token <token-do-partner>
{
  "name": "X-Burguer",
  "price": 17.99,
  "category": "food"
}
```

```json
// RESPONSE STATUS -> HTTP 201 CREATED
{
  "id": 1,
  "name": "X-Burguer",
  "price": 17.99,
  "category": {
    "name": "Food"
  }
}
```

### `PUT /api/<stor_id>/product/<product_id>/` - Atualizar Produto

```json
// REQUEST
// Header -> Authorization: Token <token-do-partner>
{
  "name": "X-Tudo",
  "price": 14.99,
  "category": "food"
}
```

```json
// RESPONSE STATUS -> HTTP 200 OK
{
  "id": 1,
  "name": "X-Tudo",
  "price": 14.99,
  "category": {
    "name": "Food"
  }
}
```

### `DELETE /api/<stor_id>/product/<product_id>/` - Deletar produto

```json
// REQUEST
// Header -> Authorization: Token <token-do-partner>
```

```json
// RESPONSE STATUS -> HTTP 204 NO CONTENT

```

### `GET /api/stor/<stor_id>/products/?category=drink` - Listar produtos por categoria

```json
// REQUEST
// Header -> Authorization: Token <token-do-partner-or-client>
```

```json
// RESPONSE STATUS -> HTTP 200 OK
  {
    "id": 1,
    "name": "Fanta Laranja",
    "price": 4.99
  },
  {
    "id": 3,
    "name": "Coca-cola",
    "price": 8.99
  }
```

### `POST /api/orders/` - Criar Orders

```json
// REQUEST
// Header -> Authorization: Token <token-do-client>
{
  "products": [{ "id": 11, "quantity": 2 }]
}
```

```json
// RESPONSE STATUS -> HTTP 201 CREATED
{
  "id": 18,
  "order_products": [
    {
      "product": 11,
      "unit_price": 10.99,
      "quantity": 2
    }
  ],
  "date": "2021-12-02T19:56:29.527655Z",
  "total_price": 21.98
}
```

### `GET /api/order/<int:pk>/` - Listar Order por ID

```json
// REQUEST
// Header -> Authorization: Token <token-do-partner-or-clientt>
```

```json
// RESPONSE STATUS -> HTTP 200 OK
{
  "id": 18,
  "order_products": [
    {
      "product": 11,
      "unit_price": 10.99,
      "quantity": 2
    }
  ],
  "date": "2021-12-02T19:56:29.527655Z",
  "total_price": 21.98
}
```

### `GET /api/order/` - Listar Order

```json
// REQUEST
// Header -> Authorization: Token <token-do-partner-or-clientt>
```

```json
// RESPONSE STATUS -> HTTP 200 OK
{
  "id": 18,
  "order_products": [
    {
      "product": 11,
      "unit_price": 10.99,
      "quantity": 2
    }
  ],
  "date": "2021-12-02T19:56:29.527655Z",
  "total_price": 21.98
},
{
  "id": 19,
  "order_products": [
    {
      "product": 12,
      "unit_price": 10.99,
      "quantity": 1
    }
  ],
  "date": "2021-12-02T19:56:29.527655Z",
  "total_price": 10.99
}
```

### `GET /api/category/?category=hamburgueria` - Listar lojas próximas

```json
// REQUEST
// Header -> Authorization: Token <token-do-clientt>
```

```json
// RESPONSE STATUS -> HTTP 200 OK
[
  {
    "id": 4,
    "name": "Burguer Nice",
    "lengthInMeters": 2002
  },
  {
    "id": 3,
    "name": "Burguer Pinheiros",
    "lengthInMeters": 2650
  },
  {
    "id": 2,
    "name": "Burguer Texas",
    "lengthInMeters": 3977
  }
]
```
