# ToDo com Django

<img src="https://github.com/user-attachments/assets/d4345619-e942-4e04-801d-c5e98f245489" alt="Tela Principal" width="450" />

## 🖥️ Funcionalidades

- **Autenticação de usuário**
  
- **Criar uma tarefa**
  
- **Editar uma tarefa**
  
- **Excluir uma tarefa**
  
- **Sistema de paginação, busca e filtro para a lista**


  
## :rocket: Tecnologias Utilizadas

- **Front-end: Django Html, Css**

- **Back-end: Django**

- **Versionamento: Git e GitHub**
  
- **Banco de dados: Sqlite**

## Estrutura do projeto

Estrutura do repositorio:

* **Front-end**: Templates dentro das pastas de apps.

* **Back-end**: A pasta "todo" tem todas as configurações do projeto.

### Rodar o projeto

```
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
python manage.py runserver
```

### Configurações adicionais

```
criar pasta ".env"
ajustar as variáveis de ambiente
```

#### Criar static files

```
python manage.py collectstatic --noinput
```

### Migrations

#### Criar arquivos de migração

```
python manage.py makemigrations
```

#### Migrar base de dados

```
python manage.py migrate
```

### Dependencies

#### Criar superuser

```
python manage.py createsuperuser
```

### Base de dados

Base de dados usada:

```
Sqlite
```


