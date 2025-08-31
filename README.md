# SGHSS - Sistema de Gestão Hospitalar e de Serviços de Saúde

Este projeto foi desenvolvido como parte do **Projeto Multidisciplinar** do curso  
**CST em Análise e Desenvolvimento de Sistemas - EAD**.

O objetivo é implementar um **back-end RESTful em Flask** para o gerenciamento de pacientes, usuários e registros em uma clínica/hospital.

---

## 🚀 Tecnologias Utilizadas
- Python 3.10+
- Flask (API REST)
- Flask-JWT-Extended (Autenticação JWT)
- SQLAlchemy (ORM)
- MySQL (Banco de Dados)
- Bcrypt (Hash de senha)
- Dotenv (Configuração de variáveis de ambiente)

---

## 📂 Estrutura do Projeto
```
SGHSS_Project/
│── app.py              # Ponto de entrada da aplicação Flask
│── config.py           # Configurações (MySQL, JWT, etc.)
│── models.py           # Definição das entidades (Usuário, Paciente, Log)
│── utils.py            # Funções auxiliares (hash de senha, logs)
│── manage_db.py        # Criação do banco e usuário admin
│── requirements.txt    # Dependências do projeto
│── .env.sample         # Exemplo de variáveis de ambiente
│── routes/
│    ├── auth.py        # Rotas de autenticação
│    └── pacientes.py   # Rotas CRUD de pacientes
└── README.md           # Documentação do projeto
```

---

## ⚙️ Instalação e Configuração

1. Clone este repositório:
   ```bash
   git clone https://github.com/Rmatheus0803/Trabalho-multidisciplinar-hospitalar-.git
   cd Trabalho-multidisciplinar-hospitalar-
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente copiando o arquivo `.env.sample`:
   ```bash
   cp .env.sample .env
   ```

   No `.env`, ajuste o banco de dados MySQL:
   ```
   DATABASE_USER=root
   DATABASE_PASSWORD=suasenha
   DATABASE_HOST=localhost
   DATABASE_PORT=3306
   DATABASE_NAME=sghss
   JWT_SECRET_KEY=sua_chave_jwt
   SECRET_KEY=sua_chave_flask
   ```

5. Crie as tabelas e um usuário admin:
   ```bash
   python manage_db.py
   ```

6. Execute a aplicação:
   ```bash
   python app.py
   ```

A API ficará disponível em:  
👉 http://127.0.0.1:5000

---

## 🔑 Endpoints Principais

### 🔒 Autenticação
- `POST /api/register` → Registrar usuário
- `POST /api/login` → Login e retorno de token JWT
- `GET /api/me` → Dados do usuário autenticado

### 👩‍⚕️ Pacientes
- `POST /api/pacientes` → Criar paciente
- `GET /api/pacientes` → Listar pacientes
- `GET /api/pacientes/<id>` → Buscar paciente por ID
- `PUT /api/pacientes/<id>` → Atualizar paciente
- `DELETE /api/pacientes/<id>` → Remover paciente

---

## 🧪 Testes

Foram realizados testes via **Postman**:
- Registro de usuário e login com JWT
- Cadastro, listagem, atualização e exclusão de pacientes
- Retorno adequado de erros (401, 404, 409)

Exemplo de teste de login:
```bash
curl -X POST http://127.0.0.1:5000/api/login      -H "Content-Type: application/json"      -d '{"email":"admin@localhost","senha":"admin123"}'
```

---

## 👨‍🎓 Autor
**Matheus da Luz Ribeiro**  
RU: **4469674**  
Polo: **Salvador - Iguatemi**  
Semestre: **2025/A1**  
Professor: **Prof. Winston Sen Lun Fung, Me.**

---

## 📜 Licença
Este projeto é acadêmico e não possui fins comerciais.

---

## 📎 Repositório Oficial
🔗 [Trabalho Multidisciplinar Hospitalar - GitHub](https://github.com/Rmatheus0803/Trabalho-multidisciplinar-hospitalar-)
