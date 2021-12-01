### `POST /api/accounts/` - Rota de criação de novos usuários.

```json
<!-- REQUEST --> 
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
<!-- RESPONSE STATUS -> HTTP 201 CREATED -->
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
<!-- REQUEST -->
{
  "username": "user",
  "password": "1234"
}
```

```json
<!-- RESPONSE STATUS -> HTTP 200 OK -->
{
  "token": "cda8275086e08547b3c26f2fe2c703b8845c8e1f"
}
```

### `POST /api/stor/` - Cadastrar Stor

```json
<!-- REQUEST -->
** Header -> Authorization: Token <token-do-partner>
{
  "name": "Hamburgão",
  "category": "Hamburgueria",
  "street": "R. são jose",
  "district": "jardim america",
  "number": 2266
}
```

```json
<!-- RESPONSE STATUS -> HTTP 201 CREATED -->
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

### `GET /api/stor/` - Listar Stor

```json
<!-- REQUEST -->
** Header -> Authorization: Token <token-do-partner>
```

```json
<!-- RESPONSE STATUS -> HTTP 200 OK -->
{}
```

### `GET /api/stor/<int:pk>/` - Buscar Stor poi ID

```json
<!-- REQUEST -->
** Header -> Authorization: Token <token-do-partner>
```

```json
<!-- RESPONSE STATUS -> HTTP 200 OK -->
{}
```

### `PUT /api/stor/<int:pk>/` - Atualizar Stor

```json
<!-- REQUEST -->
** Header -> Authorization: Token <token-do-partner>
```

```json
<!-- RESPONSE STATUS -> HTTP 200 OK -->
{}
```

### `DELETE /api/stor/<int:pk>/` - Deletar Stor

```json
<!-- REQUEST -->
** Header -> Authorization: Token <token-do-partner>
```

```json
<!-- RESPONSE STATUS -> HTTP 204 NO CONTENT -->
```

### `GET /api/stor?category=pizzaria/` - Listar Stor por categoria

```json
<!-- REQUEST -->
** Header -> Authorization: Token <token-do-partner>
```

```json
<!-- RESPONSE STATUS -> HTTP 200 OK -->
{}
```

### `GET /api/stor/products/` - Listar produtos de uma Stor

```json
<!-- REQUEST -->
** Header -> Authorization: Token <token-do-partner-or-client>
```

```json
<!-- RESPONSE STATUS -> HTTP 200 OK -->
{}
```

### `POST /api/<stor_id>/product/` - Cadastrar Produto

```json
<!-- REQUEST -->
** Header -> Authorization: Token <token-do-partner>
{
  "name": "X-Burguer",
  "price": 17.99,
  "category": "food"
}
```

```json
<!-- RESPONSE STATUS -> HTTP 201 CREATED -->
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
<!-- REQUEST -->
** Header -> Authorization: Token <token-do-partner>
{
  "name": "X-Tudo",
  "price": 14.99,
  "category": "food"
}
```

```json
<!-- RESPONSE STATUS -> HTTP 200 OK -->
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
<!-- REQUEST -->
** Header -> Authorization: Token <token-do-partner>
```

```json
<!-- RESPONSE STATUS -> HTTP 204 NO CONTENT -->
{}
```

### `GET /api/stor/products/?category=drink` - Listar produtos por categoria

```json
<!-- REQUEST -->
** Header -> Authorization: Token <token-do-partner-or-client>
```

```json
<!-- RESPONSE STATUS -> HTTP 200 OK -->
{}
```

### `POST /api/orders/` - Criar Orders

```json
<!-- REQUEST -->
** Header -> Authorization: Token <token-do-client>
{}
```

```json
<!-- RESPONSE STATUS -> HTTP 201 CREATED -->
{}
```

### `GET /api/order/<int:pk>/` - Listar Order por ID

```json
<!-- REQUEST -->
** Header -> Authorization: Token <token-do-partner-or-clientt>
{}
```

```json
<!-- RESPONSE STATUS -> HTTP 200 OK -->
{}
```

### `GET /api/order/` - Listar Order

```json
<!-- REQUEST -->
** Header -> Authorization: Token <token-do-partner-or-clientt>
```

```json
<!-- RESPONSE STATUS -> HTTP 200 OK -->
{}
```

### `GET /api/order/` - Listar lojas próximas

```json
<!-- REQUEST -->
** Header -> Authorization: Token <token-do-clientt>
```

```json
<!-- RESPONSE STATUS -> HTTP 200 OK -->
{}
```