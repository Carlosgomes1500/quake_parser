from collections import defaultdict

class Game:
    def __init__(self, game_id: int):
        self.game_id = f"game_{game_id}"
        self.total_kills = 0
        self.players = set() # Para evitar nomes duplicados
        self.kills = defaultdict(int) # Para iniciar a contagem de kills inicialmente em 0

    def _add_player(self, player_name: str):
        # Adiciona o jogador à partida
        # Ignorando o <world>
        if player_name != "<world>":
            self.players.add(player_name)
            # Para garantir que o jogador apareça no dicionário de kills mesmo com 0
            if player_name not in self.kills:
                self.kills[player_name] = 0

    def register_kill(self, killer: str, victim: str):
        #Registra uma morte aplicando a regra de que <world> tira 1 kill.
        self.total_kills += 1
        self._add_player(victim)

        if killer == "<world>":
            self.kills[victim] -= 1
        else:
            self._add_player(killer)
            self.kills[killer] += 1

    def to_dict(self) -> dict:
    #Retorna os dados no formato de dicionário exigido pelo desafio
        return {
            self.game_id: {
                "total_kills": self.total_kills,
                "players": list(self.players),
                "kills": dict(self.kills)
            }
        }