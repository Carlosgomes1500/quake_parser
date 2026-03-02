from fastapi import FastAPI, HTTPException
from parser import QuakeLogParser

#Inicializa o FastAPI
app = FastAPI(
    title="Quake Log API",
    description="API para consultar resultados das partidas de Quake 3 Arena",
    version="1.0.0"
)

#Processamos o log apenas UMA vez quando a API inicia
print("Processando arquivo de log...")
parser = QuakeLogParser("games.log")
parsed_games = parser.parse()

#Transformamos a lista de jogos em um dicionário usando o game_id como chave para busca rápida
games_db = {}
for game in parsed_games:
    game_dict = game.to_dict()
    games_db[game.game_id] = game_dict[game.game_id]


#Criando as Rotas (Endpoints) da API
@app.get("/")
def home():
    return {"message": "Quake Log API está online! Acesse http://127.0.0.1:8000/docs para ver a documentação interativa."}


#Retorna o relatório completo de todas as partidas.
@app.get("/api/games")
def list_all_games():
    return games_db

#Busca os dados de uma partida específica.
@app.get("/api/games/{game_id}")
def get_game(game_id: str):
    key = f"game_{game_id}" if not game_id.startswith("game_") else game_id
    
    if key in games_db:
        return games_db[key]
    
    #Se o jogo não existir, retorna um erro 404
    raise HTTPException(status_code=404, detail="Partida não encontrada no log")