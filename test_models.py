from models import Game
import json

# 1. Criamos um "molde" de uma nova partida com ID 1
jogo = Game(1)

# 2. Vamos simular algumas mortes (kills)
print("-> Isgalamido matou Dono da Bola")
jogo.register_kill(killer="Isgalamido", victim="Dono da Bola")

print("-> <world> matou Isgalamido (caiu no vazio)")
jogo.register_kill(killer="<world>", victim="Isgalamido")

print("-> Zeh matou Dono da Bola")
jogo.register_kill(killer="Zeh", victim="Dono da Bola")

print("-> Isgalamido matou Zeh")
jogo.register_kill(killer="Isgalamido", victim="Zeh")

# 3. Pegamos o resultado e usamos o json para imprimir bonito na tela
resultado = jogo.to_dict()
print("\n=== RESULTADO FINAL DA PARTIDA ===")
print(json.dumps(resultado, indent=2, ensure_ascii=False))