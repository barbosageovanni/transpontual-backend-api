# Transpontual Backend API

FastAPI backend para o sistema de gestão de frotas da Transpontual.

## Tecnologias
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic

## Deploy
Este repositório é automaticamente deployado no Railway como backend API.

## Endpoints
- `/health` - Health check
- `/docs` - Documentação Swagger
- `/api/v1/auth/` - Autenticação
- `/api/v1/vehicles/` - Gestão de veículos
- `/api/v1/drivers/` - Gestão de motoristas

## Desenvolvimento Local
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
