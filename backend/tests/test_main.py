from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    """Testa se a rota raiz responde 200 OK"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "API Intuitive Care rodando! Acesse /docs para documentação."}

def test_search_operadora_success():
    """Testa uma busca que deve retornar resultados (Ex: Unimed)"""
    response = client.get("/operadoras/search?q=unimed")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list) # Verifica se é uma lista
    assert len(data) > 0          # Verifica se veio algo
    
    # Verifica se o primeiro resultado faz sentido
    # (Converte para minúsculo para garantir a comparação)
    primeiro_resultado = data[0]["razao_social"].lower()
    assert "unimed" in primeiro_resultado

def test_search_operadora_empty():
    """Testa uma busca que não deve retornar nada"""
    response = client.get("/operadoras/search?q=xzywkqpw123")
    assert response.status_code == 200
    data = response.json()
    
    # Deve ser uma lista vazia
    assert isinstance(data, list)
    assert len(data) == 0

def test_search_validation_min_length():
    """Testa se a API bloqueia buscas com menos de 3 letras"""
    response = client.get("/operadoras/search?q=ab")
    # O FastAPI retorna 422 Unprocessable Entity para validações de Query
    assert response.status_code == 422

def test_limit_results():
    """Testa se o parâmetro limit está funcionando"""
    # Pede apenas 5 itens
    response = client.get("/operadoras/search?q=saude&limit=5")
    assert response.status_code == 200
    data = response.json()
    
    assert isinstance(data, list)
    assert len(data) <= 5 # Garante que não veio mais que 5