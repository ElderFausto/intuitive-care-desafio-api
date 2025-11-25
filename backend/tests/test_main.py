from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    """Testa se a rota raiz responde 200 OK"""
    response = client.get("/")
    assert response.status_code == 200
    # CORREÇÃO: Texto atualizado para bater com o seu main.py atual
    assert response.json() == {"status": "ok", "message": "API Intuitive Care rodando!"}

def test_search_operadora_success():
    """Testa uma busca que deve retornar resultados (Ex: Unimed)"""
    response = client.get("/operadoras/search?q=unimed")
    assert response.status_code == 200
    data = response.json()
    
    assert isinstance(data, list)
    assert len(data) > 0
    
    # Garante que o primeiro resultado tem Unimed no nome
    razao_social = str(data[0]["razao_social"]).lower()
    assert "unimed" in razao_social

def test_search_by_cnpj():
    """Testa a nova busca por CNPJ"""
    # CNPJ com mais de 6 dígitos para testar a nova lógica
    response = client.get("/operadoras/search?q=38211476") 
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_search_with_uf_filter():
    """Testa o filtro por Estado (UF)"""
    response = client.get("/operadoras/search?q=unimed&uf=RJ")
    assert response.status_code == 200
    data = response.json()
    
    assert isinstance(data, list)
    if len(data) > 0:
        for operadora in data:
            assert operadora["uf"] == "RJ"

def test_search_operadora_empty():
    """Testa uma busca que não deve retornar nada"""
    # CORREÇÃO: Usamos uma string sem números para testar apenas o Fuzzy
    response = client.get("/operadoras/search?q=xyzstringinexistente")
    assert response.status_code == 200
    data = response.json()
    
    assert isinstance(data, list)
    assert len(data) == 0

def test_search_validation_min_length():
    """Testa se a API bloqueia buscas com menos de 3 letras"""
    response = client.get("/operadoras/search?q=ab")
    assert response.status_code == 422

def test_limit_results():
    """Testa se o limite de resultados funciona"""
    response = client.get("/operadoras/search?q=saude&limit=5")
    assert response.status_code == 200
    data = response.json()
    
    assert isinstance(data, list)
    assert len(data) <= 5