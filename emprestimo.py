from livro import Livro
from leitor import Leitor
import datetime

# lista_de_livros
class EmprestimoLivro:
    def __init__(self, titulo, autor, codigo, data_emprestimo, nome, matricula):
        self.livro = Livro (titulo, autor, codigo)
        self.leitor = Leitor (nome, matricula)
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = None
