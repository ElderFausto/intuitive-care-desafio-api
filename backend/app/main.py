from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from app.services.csv_service import csv_service
from app.schemas.operadora import Operadora

app = FastAPI(
    title="Intuitive Care Teste de API",
    description="API de busca de operadoras ativas na ANS com busca textual (Fuzzy Search).",
    version="1.0.0"
)

# --- Configuração do CORS ---
# Permitir requisições do frontend para a API
origins = [
    "http://localhost:5173",  # Porta padrão do Vite/Vue
    "http://localhost:8080",  # Porta alternativa comum
    "*"                       # Apenas para dev *aceita tudo
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Health"])
def read_root():
    return {"status": "ok", "message": "API Intuitive Care rodando! Acesse /docs para documentação."}

@app.get("/operadoras/search", response_model=List[Operadora], tags=["Operadoras"])
def search_operadoras(
    q: str = Query(..., min_length=3, description="Termo para busca (Ex: 'Unimed', 'Bradesco')"),
    limit: int = Query(10, le=100, description="Resultados por página")
):
    """
    **Busca Inteligente de Operadoras**
    
    Realiza uma busca textual nos campos 'Razão Social'.
    Retorna os resultados ordenados por relevância (score de similaridade).
    """
    try:
        results = csv_service.search(q, limit)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))