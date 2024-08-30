# Sistema de Gestão de Produtos - Nunes Sports

## Visão Geral
Este projeto foi desenvolvido como parte de um desafio de programação para criar um sistema de gestão de produtos para a empresa fictícia Nunes Sports. O objetivo era demonstrar criatividade, habilidades de resolução de problemas, qualidade de código, seguindo as melhores práticas como Clean Code e princípios SOLID.

## Funcionalidades
- **Operações CRUD**: Criação, leitura, atualização e deleção de produtos no banco de dados.
- **Gestão de Produtos**: Gerencie os detalhes dos produtos, como nome, código, descrição e preço.
- **Integração com Banco de Dados**: Todas as ações na interface refletem diretamente no banco de dados.
- **Interface Web**: Página web interativa para exibição e gestão dos produtos.

## Tecnologias Utilizadas
- **Backend**: FastAPI, Python
- **Frontend**: HTML, CSS, JavaScript, Jinja2
- **Banco de Dados**: SQLite

## Estrutura do Projeto

**nunes_sports/** 

- **app/** - Contém os arquivos principais da aplicação.
  - **routers/** - Rotas da aplicação.
  - **static/** - Arquivos CSS e JavaScript
  - **templates/** - Arquivos HTML renderizados com Jinja2 para a interface web.
  - **crud.py** - Operações CRUD para a gestão dos produtos.
  - **database.py** - Configuração do banco de dados SQLite.
  - **main.py** - Ponto de entrada da aplicação.
  - **models.py** - Definição dos modelos de dados.
  - **schemas.py** - Esquemas de dados.


## Como Executar o Projeto

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/V1vianes/nunes_sports.git

2. **Crie um ambiente virtual:**
   ``` bash
   cd nunes_sports

3. **Navegue até o diretório do projeto:**
   ```bash
   python -m venv env

4. **Ative o ambiente virtual:**
   ```bash
   *No Windows:
   .\env\Scripts\activate
   
   *No macOS/Linux:
   source env/bin/activate
   
5. **Instale as dependências:** 
   ```bash
   pip install -r requirements.txt```
   
6. **Inicie a aplicação:**
   ```bash
   uvicorn app.main:app --reload```
   
7. **Acesse a aplicação em:** [http://localhost:8000](http://localhost:8000)
