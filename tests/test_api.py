from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_rota_principal_retorna_boas_vindas():
    response = client.get("/")
    assert response.status_code == 200
    assert "Quake Log API está online" in response.json()["message"]

def test_busca_jogo_inexistente_retorna_erro_404():
    response = client.get("/api/games/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Partida não encontrada no log"