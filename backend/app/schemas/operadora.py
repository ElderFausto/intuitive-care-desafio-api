# backend/app/schemas/operadora.py
from pydantic import BaseModel
from typing import Optional

class Operadora(BaseModel):
    registro_ans: str
    cnpj: str
    razao_social: str
    nome_fantasia: Optional[str] = ""
    modalidade: Optional[str] = ""
    logradouro: Optional[str] = ""
    numero: Optional[str] = ""
    complemento: Optional[str] = ""
    bairro: Optional[str] = ""
    cidade: Optional[str] = ""
    uf: Optional[str] = ""
    cep: Optional[str] = ""
    telefone: Optional[str] = ""
    email: Optional[str] = ""

    class Config:
        from_attributes = True