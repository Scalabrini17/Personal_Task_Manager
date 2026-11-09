# Iniciando Atulização (Maior implementação)
dia 09/11

Para essas implementações montei um pequeno esquema a ser seguido, primeiro preciso implementar o registro e autenticação dos usuário e em seguida o isolamento de tarefas por usuário. Segue a baixo o esquema 

Dicionário: ✅ significa que o passo foi concluido

# 1º Parte Implementação de um sistema de autenticação e registro de usuários.

## Fase 1 — Habilitar o app de usuários
- **Conceito:** `INSTALLED_APPS` e `AppConfig`.
- **Arquivos:** `core/settings.py`, `apps/users/apps.py`.
- **Atenção:** o `apps.py` de `users` está com `name = 'users'`, mas o caminho real é `apps.users`. Isso precisa ser corrigido antes de ativar o app.
- **Você fará:** adicionar `'apps.users'` ao `INSTALLED_APPS` e corrigir o `name`.

## Fase 2 — Ligar Task ao usuário (o coração da feature)
- **Conceito:** `ForeignKey`, `AUTH_USER_MODEL`, `on_delete=CASCADE`, `related_name`.
- **Arquivo:** `apps/GTP/models.py`.
- **Você fará:** adicionar o campo `usuario` na `Task`.
- **Migration delicada (3 passos):** como já existem tarefas sem dono, não dá para criar o campo obrigatório direto. O fluxo será:
  1. Adicionar o campo `null=True` (permitir vazio temporariamente).
  2. Criar uma **data migration** que atribui todas as tarefas antigas a um usuário existente (preciso do `username` desse usuário).
  3. Alterar o campo para obrigatório (`null=False`).

## Fase 3 — Registro, Login e Logout
- **Conceito:** `django.contrib.auth`, `UserCreationForm`, `LoginView`/`LogoutView`, `LOGIN_URL`/`LOGIN_REDIRECT_URL`.
- **Arquivos:** `apps/users/views.py`, `apps/users/urls.py` (novo), `core/urls.py`, `core/settings.py`, templates.
- **Você fará:** criar a view de cadastro, configurar as rotas de login/logout e montar os templates `login.html` e `register.html`.

## Fase 4 — Proteger as views
- **Conceito:** `@login_required`.
- **Arquivo:** `apps/GTP/views.py`.
- **Você fará:** aplicar o decorator em todas as views do GTP (home, task, dashboard, lixeira etc.).

# 2º Isolamento de tarefas por usuário (cada usuário vê apenas suas próprias tarefas).

## Fase 5 — Filtrar e criar tarefas por usuário
- **Conceito:** `request.user` + `QuerySet.filter()`.
- **Arquivo:** `apps/GTP/views.py`.
- **Você fará:**
  - `view_task`, `lixeira_task`, `dashboard` → filtrar por `usuario=request.user`.
  - `add_task` → `form.save(commit=False)`, setar `task.usuario = request.user`, depois `save()`.
- **Ponto-chave:** o campo `usuario` **não** entra no `ModelForm` (nunca confie no usuário vindo do formulário).

## Fase 6 — Segurança nas ações por id (anti-IDOR)
- **Conceito:** `get_object_or_404(Model, id=id, usuario=request.user)`.
- **Arquivo:** `apps/GTP/views.py`.
- **Você fará:** trocar os `Task.objects.get(id=id)` de `editar`, `excluir`, `visualizar`, `finalizar`, `mandar_task_lixo` e `restaurar` por `get_object_or_404` **com o filtro de usuário**. Sem isso, alguém pode acessar tarefa de outro só trocando o id na URL.
- **Bônus:** corrigir `excluir_task`, que hoje usa `.get()` (gera erro 500 se o id não existir).

## Fase 7 — Templates
- **Arquivos:** `templates/base/nav_bar.html`, `templates/base/sideBar.html`, `templates/task/login.html`, novo `register.html`.
- **Você fará:** mostrar o nome do usuário logado, botão de sair, e construir os formulários de login/cadastro reaproveitando o CSS de notificações existente.

## Verificação final
- Criar 2 usuários, logar em cada um e confirmar que cada um só vê/edita suas próprias tarefas.
- Testar acesso a URL de tarefa de outro usuário (deve dar 404).

