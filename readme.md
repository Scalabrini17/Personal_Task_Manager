# Personal Task Manager

Sistema web de gerenciamento de tarefas desenvolvido com Django, permitindo criar, editar, visualizar e excluir tarefas de forma simples e organizada.

## Objetivo

Este projeto foi desenvolvido com o objetivo de praticar conceitos de desenvolvimento web utilizando Django, incluindo:

- Modelos (Models)
- Formulários (Forms)
- Templates
- CRUD completo
- URLs e Views
- Banco de dados SQLite
- Bootstrap para estilização

---

## Funcionalidades

- Criar tarefas
- Listar tarefas
- Editar tarefas
- Excluir tarefas
- Definir prioridade da tarefa
- Definir status da tarefa
- Definir prazo de conclusão
- Interface web amigável

---

## Tecnologias Utilizadas

- Python 3
- Django
- SQLite3
- HTML5
- CSS3
- Bootstrap 5

---

## Estrutura do Projeto

```text
Personal_Task_Manager/
│
├── apps/
│   ├── GTP/
│       ├── admin.py
│       ├── apps.py
│       ├── forms.py
│       ├── models.py
│       ├── urls.py
│       ├── validator.py
│       └── views.py
│   └── Users
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       └── views.py
│
├── templates/
│   ├── base/
│       ├── base.html
│       ├── footer.html
│       ├── mensagens.html
│       ├── nav_bar.html
│       └── scripts.html
│   └── task/
│       ├── addTask.html
│       ├── editar_task.html
│       ├── home.html
│       ├── login.html
│       └── task.html 
│
├── static/
│   └── CSS
│       └── style.css
│
├── manage.py
├── requirements.txt
└── db.sqlite3
```

---

## Modelo da Aplicação

Cada tarefa possui:

- Nome
- Descrição
- Prazo
- Prioridade
  - Baixa
  - Média
  - Alta
  - Urgente
- Status
  - Em espera
  - Iniciado
  - Finalizado

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/Scalabrini17/Personal_Task_Manager.git
```

Entre na pasta do projeto:

```bash
cd Personal_Task_Manager
```

Crie um ambiente virtual:

### Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crir uma nova Secret Key para o core:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Depois crie um arquivo .env e digite:

```bash
SECRET_KEY = *Cole a chave gerada no terminal aqui
```

Execute as migrações:

```bash
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

Acesse:

```text
http://127.0.0.1:8000
```

---

## Melhorias Futuras

- Sistema de autenticação
- Tarefas por usuário
- Filtros por status
- Busca por tarefas
- Paginação
<!-- - API REST com Django REST Framework -->
- Deploy em nuvem

---

<!-- ## Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos importantes de Django como:

- CRUD completo
- ModelForms
- Templates
- Herança de templates
- Sistema de mensagens
- Organização em apps
- Relacionamento entre Views, URLs e Templates -->

---

## Autor

**Scalabrini**