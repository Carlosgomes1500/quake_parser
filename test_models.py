from models import Game
import json

#Criando uma nova partida com ID 1
jogo = Game(1)

#Simular algumas mortes
print("-> Isgalamido matou Dono da Bola")
jogo.register_kill(killer="Isgalamido", victim="Dono da Bola")

print("-> <world> matou Isgalamido (caiu no vazio)")
jogo.register_kill(killer="<world>", victim="Isgalamido")

print("-> Zeh matou Dono da Bola")
jogo.register_kill(killer="Zeh", victim="Dono da Bola")

print("-> Isgalamido matou Zeh")
jogo.register_kill(killer="Isgalamido", victim="Zeh")

#Pegamos o resultado e usamos o json para imprimir na tela
resultado = jogo.to_dict()
print("\n=== RESULTADO FINAL DA PARTIDA ===")
print(json.dumps(resultado, indent=2, ensure_ascii=False))