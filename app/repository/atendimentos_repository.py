import pandas as pd
from ..models.exception.business_logic_exception import BusinessLogicException
from ..models.dto import AtendimentoDto
from datetime import datetime, timedelta

class AtendimentosRepository:
    def __init__(self):
        self.file_path = "static/atendimentos.csv"
        self.atendimentos_df = self.load_consultas_csv(self.file_path)

    def load_consultas_csv(self, file_path):
        try:
            atendimentos_df = pd.read_csv(file_path)
            return atendimentos_df
        except FileNotFoundError:
            raise BusinessLogicException("Error while trying do load CSV file.")
            return None

    def find_with_filter(self, filter):
        try:
            serie = pd.Series([True] * len(self.atendimentos_df))

            if filter.data_atendimento is not None:
                if not pd.api.types.is_datetime64_any_dtype(self.atendimentos_df['data_atendimento']):
                    self.atendimentos_df['data_atendimento'] = pd.to_datetime(self.atendimentos_df['data_atendimento'], errors='coerce')
                start_date = datetime.combine(filter.data_atendimento, datetime.min.time())
                end_date = start_date + timedelta(days=1)
                serie &= (pd.to_datetime(self.atendimentos_df['data_atendimento']) >= start_date) & (pd.to_datetime(self.atendimentos_df['data_atendimento']) < end_date)

            if filter.condicao_saude is not None:
                serie &= self.atendimentos_df['condicao_saude'] == filter.condicao_saude

            if filter.unidade is not None:
                serie &= self.atendimentos_df['UNIDADE'] == filter.unidade

            atendimentos_filtrados = []
            for index, row in self.atendimentos_df[serie].iterrows():
                atendimento_dto = AtendimentoDto(
                    id=row['ID'],
                    nome=row['Nome'],
                    nascimento=row['Nascimento'],
                    cns=row['CNS'],
                    cpf=row['CPF'],
                    unidade=row['UNIDADE'],
                    data_atendimento=row['data_atendimento'],
                    condicao_saude=row['condicao_saude'],
                )
                atendimentos_filtrados.append(atendimento_dto)

            return atendimentos_filtrados

        except Exception as e:
            raise BusinessLogicException("Error while filtering CSV file.")
