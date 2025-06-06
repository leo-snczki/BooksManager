class Livro:
    def __init__(self, titulo, autor, codigo, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = disponivel
    
    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "codigo": self.codigo,
            "disponivel": self.disponivel
        }

    @staticmethod
    def from_dict(data):
        return Livro(
            titulo=data["titulo"],
            autor=data["autor"],
            codigo=data["codigo"],
            disponivel=data.get("disponivel", True)
        )