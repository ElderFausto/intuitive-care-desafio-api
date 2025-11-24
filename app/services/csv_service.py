import pandas as pd
from rapidfuzz import process, fuzz, utils
import os

class CsvService:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self._load_data()

    def _load_data(self):
        """
        Carrega o CSV na memória ao iniciar.
        Tenta UTF-8 primeiro e usa o fallback para Latin1.
        """
        if not os.path.exists(self.file_path):
            print(f"ALERTA: Arquivo não encontrado em {self.file_path}")
            self.df = pd.DataFrame()
            return

        try:
            # Tenta ler como UTF-8 primeiro
            self.df = pd.read_csv(self.file_path, sep=';', encoding='utf-8', dtype=str)
            self.df = self.df.fillna("")
            print("Sucesso: CSV carregado!")
        except UnicodeDecodeError:
            # Se falhar tenta o latin1 
            try:
                self.df = pd.read_csv(self.file_path, sep=';', encoding='latin1', dtype=str)
                self.df = self.df.fillna("")
                print("Sucesso: CSV carregado!")
            except Exception as e:
                print(f"Erro de encoding: {e}")
        except Exception as e:
            print(f"Erro crítico ao ler CSV: {e}")
            self.df = pd.DataFrame()

    def search(self, query: str, limit: int = 10):
        """
        Busca Fuzzy por Razão Social.
        """
        if self.df.empty:
            return []

        choices = self.df['Razao_Social'].tolist()
        
        # Extrai os melhores matches
        results = process.extract(
            query, 
            choices, 
            scorer=fuzz.WRatio, 
            limit=limit,
            processor=utils.default_process  # Ignora acentuação
        )
        
        response_data = []
        for _, score, index in results:
            if score > 50: # filtro de relevancia mínima
                row = self.df.iloc[index]
                
                # telefone ddd + numero
                ddd = str(row.get("DDD", "")).strip()
                tel = str(row.get("Telefone", "")).strip()
                telefone_completo = f"({ddd}) {tel}" if ddd and tel else tel

                # colunas do CSV mapeadas
                item = {
                    "registro_ans": row.get("REGISTRO_OPERADORA", ""),
                    "cnpj": row.get("CNPJ", ""),
                    "razao_social": row.get("Razao_Social", ""),
                    "nome_fantasia": row.get("Nome_Fantasia", ""),
                    "modalidade": row.get("Modalidade", ""),
                    "logradouro": row.get("Logradouro", ""),
                    "numero": row.get("Numero", ""),
                    "complemento": row.get("Complemento", ""),
                    "bairro": row.get("Bairro", ""),
                    "cidade": row.get("Cidade", ""),
                    "uf": row.get("UF", ""),
                    "cep": row.get("CEP", ""),
                    "telefone": telefone_completo,
                    "email": row.get("Endereco_eletronico", "")
                }
                response_data.append(item)
                
        return response_data

# Instância Singleton
csv_service = CsvService("data/operadoras.csv")