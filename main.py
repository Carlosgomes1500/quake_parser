from parser import QuakeLogParser
from collections import defaultdict
import json

def print_game_reports(games):
    """Imprime o relatório individual de cada partida."""
    for game in games:
        print(json.dumps(game.to_dict(), indent=2, ensure_ascii=False))

def print_global_ranking(games):
    """Calcula e imprime o ranking geral de kills de todas as partidas."""
    ranking = defaultdict(int)
    
    for game in games:
        for player, kills in game.kills.items():
            ranking[player] += kills

    sorted_ranking = sorted(ranking.items(), key=lambda item: item[1], reverse=True)
    
    print("\n")
    print("---RANKING GERAL---")
    for position, (player, kills) in enumerate(sorted_ranking, start=1):
        print(f"{position}º | {player}: {kills} kills")

if __name__ == "__main__":
    #Lê o arquivo de log
    leitor = QuakeLogParser("games.log")
    jogos_processados = leitor.parse()
    
    #Imprime os relatórios
    print_game_reports(jogos_processados)
    print_global_ranking(jogos_processados)