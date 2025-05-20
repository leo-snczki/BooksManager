class GestorLeitor:

    def __init__(self):
        self.leitores = []

    def adicionar_leitor(self, leitor):
        self.leitores.append(leitor)

    def remover_leitor(self, leitor):
        self.leitores.remove(leitor)

    def listar_leitores(self):
        return self.leitores
