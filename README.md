# Quake Log Parser

## Resumo do Projeto
Este projeto é um parser construído para processar o arquivo de log `games.log` gerado pelo servidor de Quake 3 Arena. O sistema lê o arquivo, agrupa os dados de cada partida e contabiliza as mortes (kills) de cada jogador. 

O parser aplica regras de negócio específicas exigidas pelo desafio, como a penalidade de -1 kill quando um jogador morre para o ambiente (`<world>`), e ignora o `<world>` da lista final de jogadores. Os resultados podem ser visualizados via terminal ou consumidos através de uma API RESTful.

## Decisões Arquiteturais

O código foi desenhado aplicando princípios de **Orientação a Objetos (POO)** e **SOLID**, com foco especial no **Princípio da Responsabilidade Única (SRP)**:

* **Separação de Domínio e Infraestrutura:** A classe `Game` (`models.py`) cuida exclusivamente do estado da partida e das regras de pontuação. Ela não sabe ler arquivos. Já a classe `QuakeLogParser` (`parser.py`) foca apenas em ler o arquivo de texto e usar Expressões Regulares (Regex) para extrair os dados. Isso torna o código fácil de testar e de manter.
* **Uso de Regex:** Garante precisão ao capturar quem matou e quem morreu, mesmo que os nicks dos jogadores contenham espaços ou caracteres especiais.
* **FastAPI para a Task 3:** A escolha do framework FastAPI se deu pela sua alta performance, suporte nativo a tipagem assíncrona do Python e geração automática da documentação (Swagger UI), o que facilita imensamente os testes da API.

## Requisitos

* Python 3.10 ou superior.
* Bibliotecas listadas no arquivo `requirements.txt` (FastAPI, Uvicorn, etc).

## Como Executar (Setup)

### 1. Preparando o Ambiente
Faça o clone do repositório para a sua máquina e entre na pasta do projeto:
```bash
git clone [https://github.com/Carlosgomes1500/quake_parser.git](https://github.com/Carlosgomes1500/quake_parser.git)
cd quake_parser





O objetivo desta atividade foi costruir um parser para o arquivo de log games.log.

Crie e ative um ambiente virtual (venv) para isolar as dependências do projeto:

Com o ambiente ativado, instale as dependências:

Rodando o Parser no Terminal (Tasks 1 e 2)
Para processar o log e visualizar o relatório individual de cada jogo e o Ranking Geral direto no console, execute o orquestrador:

Subindo a API Web (Task 3)
Para expor os dados via API, inicie o servidor local rodando:

A API estará rodando no endereço http://127.0.0.1:8000.