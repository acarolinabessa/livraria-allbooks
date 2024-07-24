# Livraria AllBooks

## Sobre o Projeto
Aplicação sobre a Livraria virtual Allbooks.

## Sumário
   * [Instalação](#instalacao)
   * [Instalação via Docker](#docker)

## Instalação
```bash
# Clone o repositório
git clone <https://github.com/acarolinabessa/livraria-allbooks.git>

# Acesse a pasta do projeto no terminal/cmd
cd preprocessing/legal_text_preprocessing

# Instale as dependências
pip install requirements.txt

# Aplique as migrações
python manage.py migrate

# Execute a aplicação
python manage.py runserver
```

## Instalação via Docker
```bash
# Inicie o compose
docker-compose up -d
```
