# Digital Wallet API 

Este é um projeto de teste para uma API de carteira digital desenvolvida com Django e Django Rest Framework. O objetivo é criar e gerenciar usuários com saldo, além de permitir transferências entre eles.

## 🔧 Tecnologias Utilizadas

- Python 3.10+
- Django
- Django Rest Framework
- SQLite (banco de dados simples, usado para facilitar os testes e acelerar o desenvolvimento)
- NPM (para dependências frontend)
- ReactJS (frontend)

---

## 📁 Estrutura do Projeto

```
digital_wallet_api/
│
├── server/        # Backend com Django
│   ├── manage.py
│   ├── users/     # App de usuários
│   ├── requirements.txt
│   └── ...
│
├── cliente/        # Frontend com React
│   ├── package.json
│   └── ...
```

---

## 📦 Instalação e Uso

### 🔙 Backend (Django)

1. **Clone o repositório:**

```bash
git clone https://github.com/matheusvoliveira/digital_wallet_api.git
cd server
```

2. **Crie e ative o ambiente virtual:**

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale as dependências:**

As dependências estão no arquivo `requirements.txt`, então basta rodar:

```bash
pip install -r requirements.txt
```

4. **Realize as migrações:**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crie os usuários iniciais:**

Execute o seguinte comando após as migrações:

```bash
python manage.py shell
```

E cole o seguinte código:

```python
from users.initial_users import create_initial_users
create_initial_users()
exit()
```

6. **Execute o servidor:**

```bash
python manage.py runserver
```

---

### 🖥️ Frontend (ReactJS)

1. **Acesse a pasta do frontend:**

```bash
cd ../cliente
```

2. **Instale as dependências:**

```bash
npm install
```

3. **Inicie o frontend:**

```bash
npm start
```

---

## 📢 Rotas disponíveis (Backend)

- `POST /api/registrar/` → Cria novo usuário
- `POST /api/login/` → Realiza login
- `GET /api/me/` → Exibe dados do usuário autenticado
- `GET /api/usuarios/` → Lista todos os usuários
- `PATCH /api/usuarios/<id>/saldo/` → Atualiza saldo do usuário
- `POST /api/transferir/` → Transfere saldo entre usuários

---

## 📌 Notas Finais

- O banco de dados utilizado é SQLite, para facilitar os testes e acelerar o desenvolvimento.
- O projeto já vem com 5 usuários iniciais. Basta rodar o script após as migrações com o comando no shell.
- A senha de todos os usuários de teste é `senha123`.
- O arquivo `requirements.txt` está incluído no projeto. Basta baixá-lo e usar com `pip install -r requirements.txt`.

---

Desenvolvido com 💻 por Matheus Soares.
