from ..models.dto import AtendimentoFilterDto
from ..models.exception import BusinessLogicException
from ..repository import AtendimentosRepository
from datetime import datetime

class AtendimentosService:
    def __init__(self):
        self.condicoes_saude = ["hipertensao", "diabetes", "ferida vascular", "dengue", "tuberculose"]
    def extract_request_args(self, args):
        atendimento_filter = AtendimentoFilterDto()
        if args.get('data_atendimento'):
            data_atendimento = args.get('data_atendimento')
            try:
                data_atendimento = datetime.strptime(data_atendimento, '%Y-%m-%d')
                atendimento_filter.data_atendimento = data_atendimento
            except ValueError:
                raise BusinessLogicException("Erro no formato do filtro data_atendimento.")
        if args.get('condicao_saude'):
            condicao_saude = args.get('condicao_saude')
            atendimento_filter.condicao_saude = condicao_saude
            if condicao_saude not in self.condicoes_saude:
                raise BusinessLogicException("Erro no formato do filtro condicao_saude.")
        if args.get('unidade'):
            unidade = args.get('unidade')
            atendimento_filter.unidade = unidade
        return atendimento_filter

    def find_with_filter(self, filter):
        atendimento_repository = AtendimentosRepository()
        atendimentos = atendimento_repository.find_with_filter(filter)
        return atendimentos