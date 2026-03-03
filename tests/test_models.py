from models import Game

def test_jogador_mata_jogador_soma_um_ponto():
    jogo = Game(game_id="game_1")
    jogo._add_player("Isgalamido")
    jogo._add_player("Mocinha")
    
    jogo.register_kill("Isgalamido", "Mocinha")
    
    assert jogo.kills["Isgalamido"] == 1
    assert jogo.total_kills == 1

def test_world_mata_jogador_subtrai_um_ponto():
    jogo = Game(game_id="game_2")
    jogo._add_player("Isgalamido")
    jogo.kills["Isgalamido"] = 5 
    
    jogo.register_kill("<world>", "Isgalamido")
    
    assert jogo.kills["Isgalamido"] == 4
    assert "<world>" not in jogo.players