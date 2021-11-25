Criar conta
POST /accounts/

```json
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

Retorno

```json
{
  "id": 1,
  "username": "user",
  "first_name": "Joze",
  "last_name": "souza",
  "is_superuser": false
}
```

POST /login

```json
{
  "username": "user",
  "password": "1234"
}
```

Retorno

```json
{
  "token": "cda8275086e08547b3c26f2fe2c703b8845c8e1f"
}
```

Header -> Authorization: Token -> token-do-partner

Cadastrar Stor
POST /api/stor

```json
{
  "name": "Hamburgão",
  "category": "Hamburgueria",
  "street": "R. são jose",
  "district": "jardim america",
  "number": 2266
}
```

Retorno

```json
{
  "id": 1,
  "name": "Hamburgão",
  "category": "Hamburgueria",
  "woner": {
    "id": 1,
    "first_name": "Jose",
    "last_name": "souza"
  },
  "street": "R. são jose",
  "district": "jardim america",
  "number": 2266
}
```

Header -> Authorization: Token -> token-do-partner

Criar Produtos
POST /api/product/

```json
{
  "name": "X-Burguer",
  "price": 17.99,
  "category": "food"
}
```

Header -> Authorization: Token -> token-do-client

Criar Orders
POST /api/orders/

```json
{}
```

Listar order por Id

Header -> Authorization: Token -> token-do-partner-or-client

` GET /api/order/<int:pk>`

Listar order

Header -> Authorization: Token -> token-do-partner-or-client

` GET /api/order/`

Listar Stor

Header -> Authorization: Token -> token-do-client

`GET /api/stor/`

Buscar Stor por id

Header -> Authorization: Token -> token-do-client

`GET /api/stor/<int:pk>`

Atualizar Stor

Header -> Authorization: Token -> token-do-partner

`PUT /api/stor/<int:pk>`

Deletar Stor

Header -> Authorization: Token -> token-do-partner

`DELETE /api/stor/<int:pk>`

Listar lojas por Categorias

Header -> Authorization: Token -> token-do-client

`GET /api/stor?category=pizzaria/`

Listar produtos por Loja

Header -> Authorization: Token -> token-do-partner-or-client

`GET /api/stor/products/`

Atualizar Produto Stor

Header -> Authorization: Token -> token-do-partner

`PUT /api/products/<int:pk>`

Delete Produto Stor

Header -> Authorization: Token -> token-do-partner

`DELETE /api/products/<int:pk>`

Listar produtos por categoria Loja

Header -> Authorization: Token -> token-do-partner-or-client

`GET /api/stor/products/?category=drink`

Listar lojas proximas

Header -> Authorization: Token -> token-do-client

`GET /api/category?category=pizzaria`
