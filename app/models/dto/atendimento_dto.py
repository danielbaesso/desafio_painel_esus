class AtendimentoDto:
    def __init__(self, id=None, nome=None, nascimento=None, cns=None, cpf=None, unidade=None, data_atendimento=None, condicao_saude=None):   
        self.id = id
        self.nome = nome
        self.nascimento = nascimento
        self.cns = cns
        self.cpf = cpf
        self.unidade = unidade
        self.data_atendimento = data_atendimento
        self.condicao_saude = condicao_saude

    def serialize(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "nascimento": self.nascimento,
            "cns": self.cns,
            "cpf": self.cpf,
            "unidade": self.unidade,
            "data_atendimento": self.data_atendimento,
            "condicao_saude": self.condicao_saude,
        }
