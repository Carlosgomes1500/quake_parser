from parser import QuakeLogParser
import json

leitor = QuakeLogParser("games.log")

jogos_encontrados = leitor.parse()

print(f"Total de partidas encontradas: {len(jogos_encontrados)}\n")

if jogos_encontrados:
    primeiro_jogo = jogos_encontrados[0].to_dict()
    print("=== DADOS DA PARTIDA 1 ===")
    print(json.dumps(primeiro_jogo, indent=2, ensure_ascii=False))