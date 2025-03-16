# User Management API

Esta API fornece funcionalidades para gerenciar usuários, permitindo operações como listar, buscar, criar, atualizar e excluir usuários.

## Tecnologias Utilizadas
- Python
- Django
- Django REST Framework (DRF)
- Poetry (Gerenciador de dependências)

## Instalação

1. Clone o repositório:
   ```sh
   git clone <URL_DO_REPOSITORIO>
   ```

2. Acesse o diretório do projeto:
   ```sh
   cd nome_do_projeto
   ```

3. Instale o Poetry, se ainda não tiver:
   ```sh
   pip install poetry
   ```

4. Instale as dependências do projeto:
   ```sh
   poetry install
   ```

5. Ative o ambiente virtual do Poetry:
   ```sh
   poetry shell
   ```

6. Execute as migrações do banco de dados:
   ```sh
   python manage.py migrate
   ```

7. Inicie o servidor:
   ```sh
   python manage.py runserver
   ```

## Endpoints

### 1. Listar todos os usuários
   **GET /api/users/**
   - Retorna uma lista de todos os usuários cadastrados.

### 2. Buscar usuário por nickname
   **GET /api/users/{nick}/**
   - Parâmetro: `nick` (string) - O nickname do usuário.
   - Retorna os dados do usuário correspondente.

### 3. Atualizar usuário por nickname
   **PUT /api/users/{nick}/**
   - Parâmetro: `nick` (string) - O nickname do usuário.
   - Corpo da requisição: JSON contendo os novos dados do usuário.
   - Retorna os dados atualizados do usuário.

### 4. Gerenciamento de usuários
   **GET /api/user_manager/**
   - Parâmetro opcional `user` (string) - O nickname do usuário.
   - Se fornecido, retorna os dados do usuário correspondente.
   - Se não fornecido, retorna erro 400.

   **POST /api/user_manager/**
   - Corpo da requisição: JSON contendo os dados do novo usuário.
   - Retorna os dados do usuário criado.

   **PUT /api/user_manager/**
   - Corpo da requisição: JSON contendo `user_nickname` e os novos dados do usuário.
   - Retorna os dados atualizados do usuário.

   **DELETE /api/user_manager/**
   - Corpo da requisição: JSON contendo `user_nickname` do usuário a ser excluído.
   - Retorna status 202 se excluído com sucesso.

## Exemplo de Requisição

### Criar um novo usuário
```json
POST /api/user_manager/
{
    "user_nickname": "johndoe",
    "name": "John Doe",
    "email": "johndoe@example.com"
}
```

### Resposta de Sucesso
```json
{
    "user_nickname": "johndoe",
    "name": "John Doe",
    "email": "johndoe@example.com"
}
```

## Contribuição
Se quiser contribuir para este projeto, sinta-se à vontade para abrir um Pull Request.
