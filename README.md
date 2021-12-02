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
{}
```

### `GET /api/stor/products/?category=drink` - Listar produtos por categoria

```json
// REQUEST
// Header -> Authorization: Token <token-do-partner-or-client>
```

```json
// RESPONSE STATUS -> HTTP 200 OK
{}
```

### `POST /api/orders/` - Criar Orders

```json
// REQUEST
// Header -> Authorization: Token <token-do-client>
{}
```

```json
// RESPONSE STATUS -> HTTP 201 CREATED
{}
```

### `GET /api/order/<int:pk>/` - Listar Order por ID

```json
// REQUEST
// Header -> Authorization: Token <token-do-partner-or-clientt>
{}
```

```json
// RESPONSE STATUS -> HTTP 200 OK
{}
```

### `GET /api/order/` - Listar Order

```json
// REQUEST
// Header -> Authorization: Token <token-do-partner-or-clientt>
```

```json
// RESPONSE STATUS -> HTTP 200 OK
{}
```

### `GET /api/order/` - Listar lojas próximas

```json
// REQUEST
// Header -> Authorization: Token <token-do-clientt>
```

```json
// RESPONSE STATUS -> HTTP 200 OK
{}
```
