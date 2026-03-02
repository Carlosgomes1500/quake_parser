from parser import QuakeLogParser
import json

# 1. Instanciamos o nosso parser passando o caminho do arquivo de log
leitor = QuakeLogParser("games.log")

# 2. Mandamos ele processar o arquivo
jogos_encontrados = leitor.parse()

# 3. Vamos ver quantos jogos ele encontrou no total
print(f"Total de partidas encontradas: {len(jogos_encontrados)}\n")

# 4. Para não poluir a tela, vamos imprimir os dados apenas do Jogo 1
if jogos_encontrados:
    primeiro_jogo = jogos_encontrados[0].to_dict()
    print("=== DADOS DA PARTIDA 1 ===")
    print(json.dumps(primeiro_jogo, indent=2, ensure_ascii=False))