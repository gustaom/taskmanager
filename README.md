# Task Manager API

Este projeto é uma API RESTful para gerenciamento de tarefas, desenvolvida em Django e Django REST Framework. A API permite criar, ler, atualizar e excluir tarefas, além de utilizar autenticação via Token.

## Funcionalidades

- **Criar Tarefas**: Adicione novas tarefas com título, descrição e status.
- **Ler Tarefas**: Liste todas as tarefas ou consulte uma tarefa específica.
- **Atualizar Tarefas**: Edite o título, descrição ou status de uma tarefa existente.
- **Excluir Tarefas**: Remova tarefas do sistema.
- **Autenticação via Token**: Proteja a API com autenticação de token.

## Tecnologias Utilizadas

- **Django**: Framework web principal para construção da API.
- **Django REST Framework**: Extensão para Django, usada para construir a API RESTful.
- **SQLite**: Banco de dados utilizado no desenvolvimento local.
- **drf-yasg**: Usado para documentação interativa da API.

## Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento local:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seuusuario/taskmanager.git
   cd taskmanager
   ```

2. **Crie um ambiente virtual e ative-o:**

   ```bash
   python -m venv env
   source env/bin/activate  # No Windows: env\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações do banco de dados:**

   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário para acessar o admin do Django:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento:**

   ```bash
   python manage.py runserver
   ```

## Documentação da API

Acesse a documentação interativa da API no endereço abaixo após iniciar o servidor:

```
http://127.0.0.1:8000/swagger/
```

## Uso

### **Autenticação**

Para acessar as rotas protegidas da API, você precisa incluir o token de autenticação no header das requisições. Primeiro, faça login para obter o token:

```
POST /api/token/
```

### **Endpoints Principais**

- **Criar Tarefa**: `POST /api/tasks/`
- **Listar Tarefas**: `GET /api/tasks/`
- **Detalhar Tarefa**: `GET /api/tasks/{id}/`
- **Atualizar Tarefa**: `PUT /api/tasks/{id}/`
- **Excluir Tarefa**: `DELETE /api/tasks/{id}/`

## Testes

Para executar os testes, use o comando:

```bash
python manage.py test
```

## Contribuição

Sinta-se à vontade para enviar pull requests ou abrir issues para melhorias e correções.
