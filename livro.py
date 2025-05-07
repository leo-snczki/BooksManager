class Livro:
    def __init__(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = True 

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return f'O livro "{self.titulo}" foi emprestado com sucesso.'
        return f'O livro "{self.titulo}" não está disponível para empréstimo.'
    
    def devolver(self):
        self.disponivel = True
        return f'O livro "{self.titulo}" foi devolvido com sucesso.'