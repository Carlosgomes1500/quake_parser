from parser import QuakeLogParser
import json

#Instancia o parser passando o caminho do arquivo de log
leitor = QuakeLogParser("games.log")

#Processa o arquivo
jogos_encontrados = leitor.parse()

#Calcular quantos jogos são encontrados no total
print(f"Total de partidas encontradas: {len(jogos_encontrados)}\n")

#Imprimir os dados apenas do Jogo 1, para não poluir muito a tela
if jogos_encontrados:
    primeiro_jogo = jogos_encontrados[0].to_dict()
    print("=== DADOS DA PARTIDA 1 ===")
    print(json.dumps(primeiro_jogo, indent=2, ensure_ascii=False))