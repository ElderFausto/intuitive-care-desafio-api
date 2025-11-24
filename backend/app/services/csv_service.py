import pandas as pd
from rapidfuzz import process, fuzz, utils
import os
import re

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

    def _format_response(self, row):
        """Helper para formatar a linha do DF para o nosso objeto JSON (evita repetição)"""
        ddd = str(row.get("DDD", "")).strip()
        tel = str(row.get("Telefone", "")).strip()
        telefone_completo = f"({ddd}) {tel}" if ddd and tel else tel

        return {
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

    def search(self, query: str, limit: int = 20):
        """
        Busca Fuzzy refinada para priorizar matches parciais exatos.
        """
        if self.df.empty:
            return []

        response_data = []

        # BUSCA POR CNPJ
        # Regex que remove tudo que não for número da busca pontos e traços
        query_only_nums = re.sub(r'[^0-9]', '', query)

        # Se o usuário digitar 3 números prioriza a busca por CNPJ
        if len(query_only_nums) >= 3:
            # Filtra o DataFrame onde a coluna CNPJ contém os números digitados
            cnpj_matches = self.df[self.df['CNPJ'].str.contains(query_only_nums, na=False)]
            
            if not cnpj_matches.empty:
                # Se achou por CNPJ, retorna logo esses resultados com prioridade máxima
                for _, row in cnpj_matches.head(limit).iterrows():
                    response_data.append(self._format_response(row))
                
                return response_data

        # BUSCA POR NOME
        choices = self.df['Razao_Social'].tolist()
        
        # troca o WRatio por partial_token_sort_ratio
        results = process.extract(
            query, 
            choices, 
            scorer=fuzz.partial_token_sort_ratio,
            limit=limit,
            processor=utils.default_process
        )
        
        for _, score, index in results:
            if score > 60: 
                row = self.df.iloc[index]
                
                # Formata a resposta
                item = self._format_response(row)
                
                # Evita duplicatas se já tiver achado algo
                if item not in response_data:
                    response_data.append(item)
                
        return response_data

# Instância Singleton
csv_service = CsvService("data/operadoras.csv")