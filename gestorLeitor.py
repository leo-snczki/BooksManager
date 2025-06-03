from leitor import Leitor

class GestorLeitor:

    def __init__(self):
        self.leitores: list[Leitor] = []

    def adicionar_leitor(self, leitor):
        self.leitores.append(leitor)

    def remover_leitor(self, leitor):
        self.leitores.remove(leitor)

    def listar_leitores(self):
        return self.leitores
    
    def encontrar_leitor(self, identificador):
        return next(
            (l for l in self.leitores if l.nome.lower() == identificador.lower() or l.matricula.lower() == identificador.lower()),
            # Se não encontrar, retorna None.
            None
        )

