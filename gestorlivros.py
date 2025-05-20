class gestorLivros:

    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, livro):
        self.livros.remove(livro)

    def listar_livros(self):
        return self.livros
    
    def emprestar_livro(self, codigo):
        for livro in self.livros:
            if livro.codigo == codigo and livro.disponivel:
                livro.disponivel = False
                return f'O livro "{self.titulo}" foi emprestado com sucesso.'
            return True
        return False

    def devolver_livro(self, codigo):
        for livro in self.livros:
            if livro.codigo == codigo and not livro.disponivel:
                livro.disponivel = True
                return f'O livro "{self.titulo}" foi devolvido com sucesso.'
            return True
        return False