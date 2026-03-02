# Quake Parser

## Resumo do Projeto
Este projeto é um parser construído para processar o arquivo de log `games.log` gerado pelo servidor de Quake 3 Arena. O sistema lê o arquivo, agrupa os dados de cada partida e contabiliza as mortes (kills) de cada jogador. 

O parser aplica regras de negócio específicas exigidas pelo desafio, como a penalidade de -1 kill quando um jogador morre para o ambiente (`<world>`), e ignora o `<world>` da lista final de jogadores. Os resultados podem ser visualizados via terminal ou consumidos através de uma API RESTful.

## Decisões Arquiteturais

O código foi desenhado aplicando princípios de **Orientação a Objetos (POO)** e **SOLID**, para assegurar o **Princípio da Responsabilidade Única (SRP)**:

* **Separação de Domínio e Infraestrutura:** A classe `Game` (`models.py`) cuida exclusivamente do estado da partida e das regras de pontuação. Ela não sabe ler arquivos. Já a classe `QuakeLogParser` (`parser.py`) foca apenas em ler o arquivo de texto e usar Expressões Regulares (Regex) para extrair os dados. Isso torna o código fácil de testar e de manter.
* **Uso de Regex:** Garante precisão ao capturar quem matou e quem morreu, mesmo que os nicks dos jogadores contenham espaços ou caracteres especiais.
* **FastAPI para a Task 3:** O FastAPI foi adotado por ser um dos frameworks web mais rápidos e modernos do ecossistema Python. O suporte nativo a tipagem assíncrona do Python e a geração automática da documentação (Swagger UI) aceleram o desenvolvimento e garantem endpoints fáceis de testar.

## Requisitos

* Python 3.10 ou superior.
* Bibliotecas listadas no arquivo `requirements.txt` (FastAPI, Uvicorn, etc).

## Como Executar (Setup)

### 1. Preparando o Ambiente
Faça o clone do repositório para a sua máquina e entre na pasta do projeto:
```bash
git clone https://github.com/Carlosgomes1500/quake_parser.git
cd quake_parser

```

Crie e ative um ambiente virtual (venv) para isolar as dependências do projeto:

#### Criando o ambiente virtual

```bash
python -m venv venv

```

#### Ativando no Windows:

```bash
venv\Scripts\activate

```

#### Ativando no Linux/Mac:

```bash
source venv/bin/activate

```

Com o ambiente ativado, instale as dependências:

```bash
pip install -r requirements.txt

```

### 2. Rodando o Parser no Terminal (Tasks 1 e 2)

Para processar o log e visualizar o relatório individual de cada jogo e o Ranking Geral direto no console, execute o orquestrador:

```bash
python main.py

```

### 3. Subindo a API Web (Task 3)

Para expor os dados via API, inicie o servidor local rodando:

```bash
uvicorn api:app --reload

```

A API estará rodando no endereço `http://127.0.0.1:8000`.

**Documentação Interativa (Swagger UI):**
Com o servidor rodando, acesse `http://127.0.0.1:8000/docs` no seu navegador para explorar, visualizar e testar todos os endpoints da API de forma interativa. Através dessa interface, você terá acesso às seguintes rotas:

* **`GET /`**: Rota raiz de boas-vindas, utilizada para verificar se a API está online (Health Check).
* **`GET /api/games`**: Retorna o relatório completo contendo todas as partidas do log agrupadas.
* **`GET /api/games/{game_id}`**: Busca os dados de uma partida específica. Você pode buscar passando apenas o número (ex: `2`) ou a chave completa (ex: `game_2`). Se o jogo não existir, a API retornará um erro 404 (Not Found).