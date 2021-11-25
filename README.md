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

Criar Produtos
POST /api/product/

```json
{
  "name": "X-Burguer",
  "price": 17.99,
  "category": "food"
}
```

Criar Orders
POST /api/orders/

```json
{}
```

Listar order por Id

` GET /api/order/<int:pk>`

Listar order

` GET /api/order/`

Listar Stor

`GET /api/stor/`

Listar Stor por id

`GET /api/stor/<int:pk>`

Atualizar Stor

`PUT /api/stor/<int:pk>`

Deletar Stor

`DELETE /api/stor/<int:pk>`

Listar Categorias

`GET /api/stor?category=pizzaria/`

Listar produtos por Loja

`GET /api/stor/products/`

Atualizar Produto Stor

`PUT /api/products/<int:pk>`

Atualizar Produto Stor

`DELETE /api/products/<int:pk>`

Listar produtos por categoria Loja

`GET /api/stor/products/?category=drink`

Listar lojas proximas

`GET /api/category?category=pizzaria`
