# emprestimoLivro.py
from livro import Livro
from leitor import Leitor
import datetime


class EmprestimoLivro:
    def __init__(self, livro, leitor, data_emprestimo):
        self.livro = livro
        self.leitor = leitor 
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = None

    def devolver_livro(self):
        if not self.livro.disponivel: 
            self.livro.devolver() 
            self.data_devolucao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Usa a data e hora atuais
            return f'O livro "{self.livro.titulo}" foi devolvido com sucesso.'
        return "Este livro não foi emprestado."
