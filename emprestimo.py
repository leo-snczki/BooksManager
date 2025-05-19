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

    def devolver_livro(self):
        if not self.livro.disponivel: 
            self.livro.devolver() 
            self.data_devolucao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Usa a data e hora atuais
            return f'O livro "{self.livro.titulo}" foi devolvido com sucesso.'
        return "Este livro não foi emprestado."
