class AtendimentoFilterDto:
    def __init__(self):
        self.data_atendimento = None
        self.condicao_saude = None
        self.unidade = None

    def to_dict(self):
        return {
            "data_atendimento": self.data_atendimento,
            "condicao_saude": self.condicao_saude,
            "unidade": self.unidade
        }


    def __dict__(self):
        return self.to_dict()