class AtendimentoResponseDto():
    def __init__(self):
        self.atendimentos = None
        self.status = None
        self.message = None

    def serialize(self):
        return {
            "atendimentos": self.atendimentos,
            "status": self.status,
            "message": self.message
        }

    def __dict__(self):
        return self.to_dict()