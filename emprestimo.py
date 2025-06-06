from livro import Livro
from leitor import Leitor
from datetime import datetime,timedelta

# lista_de_livros
class EmprestimoLivro:
    def __init__(self, livro: Livro, leitor: Leitor):
        self.livro = livro
        self.leitor = leitor
        self.data_emprestimo = datetime.today()
        self.data_para_devolucao = (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y")
        self.data_devolvida:str
