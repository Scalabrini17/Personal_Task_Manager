# Personal Task Manager

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Django-6.0.6-092E20.svg" alt="Django Version">
  <img src="https://img.shields.io/badge/Bootstrap-5-563D7C.svg" alt="Bootstrap Version">
  <img src="https://img.shields.io/badge/Database-SQLite3-003B57.svg" alt="Database">
</p>

O **Personal Task Manager** é um sistema web intuitivo e organizado para gerenciamento de tarefas, desenvolvido com o framework Django. O projeto permite aos usuários criar, visualizar, editar e excluir tarefas de maneira eficiente, ajudando na organização diária.

---

## 🎯 Objetivo do Projeto

Este projeto foi concebido com o intuito de aplicar e aprofundar conhecimentos em desenvolvimento web utilizando Django. Durante o desenvolvimento, foram explorados conceitos fundamentais como:

- **Modelagem de Dados (Models):** Estruturação do banco de dados para armazenar as tarefas.
- **Formulários (Forms):** Criação e validação de formulários utilizando `ModelForm`.
- **Templates e Views:** Renderização de páginas dinâmicas e controle de fluxo com herança de templates.
- **Operações CRUD:** Implementação completa de Create, Read, Update e Delete.
- **Roteamento (URLs):** Configuração de rotas amigáveis para navegação no sistema.
- **Validações Customizadas:** Prevenção de duplicação de tarefas com validações específicas.

---
## 🔄 Últimas Atualizações

- Implementado sistema de lixeira completa, podendo excluir permanetemente e restaurar as tasks mandadas para a lixeira
- Adicionado template de Home: Tela de Bem Vindo
---

## ✨ Funcionalidades

O sistema oferece um conjunto completo de ferramentas para o gerenciamento de tarefas:

- **Criação de Tarefas:** Adicione novas tarefas informando nome, descrição, prazo, prioridade e status.
- **Listagem Organizada:** Visualize todas as tarefas cadastradas em uma interface clara.
- **Edição de Tarefas:** Atualize informações de tarefas existentes a qualquer momento.
- **Exclusão de Tarefas:** Remova tarefas que não são mais necessárias.
- **Validação Inteligente:** O sistema impede a criação de tarefas com nomes duplicados, garantindo a integridade dos dados.
- **Feedback Visual:** Sistema de mensagens integrado para confirmar ações como criação, edição e exclusão de tarefas.

---

## 🛠️ Tecnologias e Ferramentas

O projeto foi construído utilizando as seguintes tecnologias:

- **Backend:** Python 3, Django (v6.0.6)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Banco de Dados:** SQLite3 (Padrão do Django)
- **Outras Bibliotecas:** `python-decouple` (para gerenciamento de variáveis de ambiente), `asgiref`, `sqlparse`.

---

## 🏗️ Estrutura do Modelo de Dados

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
│       ├── task.html
│       ├── taskFinalizada.html
│       └── visualizartask.html 
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

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

### Pré-requisitos

Certifique-se de ter o [Python](https://www.python.org/downloads/) e o [Git](https://git-scm.com/) instalados em sua máquina.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Scalabrini17/Personal_Task_Manager.git
   ```

2. **Acesse o diretório do projeto:**
   ```bash
   cd Personal_Task_Manager
   ```

3. **Crie e ative um ambiente virtual:**
   - No Linux/macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - No Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

4. **Instale as dependências do projeto:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure as Variáveis de Ambiente:**
   Gere uma nova chave secreta (Secret Key) executando o comando abaixo:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
   Crie um arquivo chamado `.env` na raiz do projeto e adicione a chave gerada:
   ```env
   SECRET_KEY=cole_a_chave_gerada_aqui
   ```

6. **Execute as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

7. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

8. **Acesse a aplicação:**
   Abra o seu navegador e acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔮 Updates Futuros

- Reorganizar alguns campos que estão faltando na edição das tasks

<!-- O projeto está em evolução. Algumas das melhorias planejadas incluem:

- Implementação de um sistema de autenticação e registro de usuários.
- Isolamento de tarefas por usuário (cada usuário vê apenas suas próprias tarefas).
- Adição de filtros (por status, prioridade) e barra de busca.
- Implementação de paginação na listagem de tarefas.
- Criação de uma API REST utilizando o Django REST Framework.
- Realização do deploy da aplicação em uma plataforma de nuvem. -->

---

## 👨‍💻 Autor

Desenvolvido por **[Scalabrini](https://github.com/Scalabrini17)**.