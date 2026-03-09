# 🍕 Pizza Delivery API

Este projeto é uma API robusta para gerenciamento de pedidos de uma pizzaria, desenvolvida para fins de estudo e prática de arquitetura de software moderna.

## 🚀 Tecnologias Utilizadas

O projeto utiliza as seguintes tecnologias e bibliotecas:

* **[FastAPI](https://fastapi.tiangolo.com/)**: Framework web moderno e rápido.
* **[SQLAlchemy](https://www.sqlalchemy.org/)**: ORM para manipulação do banco de dados.
* **[Alembic](https://alembic.sqlalchemy.org/)**: Ferramenta para migrações de banco de dados.
* **[SQLite](https://www.sqlite.org/)**: Banco de dados relacional leve.
* **[Pydantic](https://docs.pydantic.dev/)**: Validação de dados e esquemas.

### 📦 Estrutura do Projeto

```
src/
├── dependencies/  # Injeção de dependências (ex: auth, db)
├── models/        # Modelos do banco de dados (SQLAlchemy)
├── routes/        # Definição dos endpoints (auth, orders, etc)
├── schemas/       # Esquemas de validação (Pydantic)
└── main.py        # Ponto de entrada da aplicação
🛠️ Como executar o projeto
1. Clonar o repositório
Bash
git clone [https://github.com/EduardoDev-spec/API_PIZZA.git](https://github.com/EduardoDev-spec/API_PIZZA.git)
cd API_PIZZA
2. Configurar o Ambiente Virtual
Bash
python -m venv .venv
# No Windows:
.venv\Scripts\activate
# No Linux/Mac:
source .venv/bin/activate
3. Instalar dependências
Bash
pip install -r requirements.txt
4. Configurar Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto seguindo o modelo:

Plaintext
DATABASE_URL=sqlite:///./banco.db
SECRET_KEY=sua_chave_secreta_aqui
5. Rodar as Migrações
Bash
alembic upgrade head
6. Iniciar a API
Bash
fastapi dev src/main.py
A API estará disponível em http://127.0.0.1:8000.
Acesse a documentação interativa em http://127.0.0.1:8000/docs.

Desenvolvido por Eduardo ✨
