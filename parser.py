"""
Abre o games.log e lê linha por linha.

Se bate de frente com a palavra InitGame:,
cria um novo Game(id).

Se bate de frente com a palavra Kill:, 
usa o Regex para pegar os nomes 
e passa os nomes para a função register_kill no models.py
"""

import re
from models import Game

class QuakeLogParser:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.games = []
        # O Regex pega tudo entre os dois pontos e o "killed" 
        # e tudo entre o "killed" e o "by" (Vítima)
        self.kill_pattern = re.compile(r"Kill: \d+ \d+ \d+: (.*?) killed (.*?) by")

    def parse(self) -> list[Game]:
        current_game = None
        game_counter = 0

        # Abre o arquivo em modo de leitura ('r')
        with open(self.filepath, 'r', encoding='utf-8') as file:
            for line in file:
                # Se achar "InitGame:", significa que uma nova partida começou
                if "InitGame:" in line:
                    game_counter += 1
                    current_game = Game(game_counter)
                    self.games.append(current_game)
                
                # Se achar "Kill:" e já tiver um jogo rolando, registra a morte
                elif "Kill:" in line and current_game is not None:
                    match = self.kill_pattern.search(line)
                    if match:
                        killer = match.group(1).strip() # Extrai o assassino
                        victim = match.group(2).strip() # Extrai a vítima
                        current_game.register_kill(killer, victim)
                        
        return self.games