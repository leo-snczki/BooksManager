class Leitor:

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "matricula": self.matricula
        }

    @staticmethod
    def from_dict(data):
        return Leitor(
            nome=data["nome"],
            matricula=data["matricula"]
        )