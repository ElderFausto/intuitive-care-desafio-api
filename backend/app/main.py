from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional # <--- Adicione Optional
from app.services.csv_service import csv_service
from app.schemas.operadora import Operadora

app = FastAPI(
    title="Intuitive Care Teste de API",
    description="API de busca de operadoras ativas na ANS.",
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
    return {"status": "ok", "message": "API Intuitive Care rodando!"}

# Listar Estados
@app.get("/operadoras/ufs", tags=["Auxiliar"])
def get_ufs():
    """Retorna a lista de todos os estados (UFs) disponíveis no CSV"""
    return csv_service.get_all_ufs()

# Aceita parâmetro 'uf'
@app.get("/operadoras/search", response_model=List[Operadora], tags=["Operadoras"])
def search_operadoras(
    q: str = Query(..., min_length=3, description="Termo para busca"),
    uf: Optional[str] = Query(None, min_length=2, max_length=2, description="Sigla do Estado (Ex: SP, RJ)"),
    limit: int = Query(20, le=100)
):
    """
    **Busca Inteligente de Operadoras**
    
    Realiza uma busca textual nos campos 'Razão Social'.
    Retorna os resultados ordenados por relevância (score de similaridade).
    """
    try:
        # Passamos o UF para o serviço
        results = csv_service.search(q, limit, uf)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))