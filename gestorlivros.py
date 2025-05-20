import json
from livro import Livro

class gestorLivros:

    def __init__(self):
        self.livros: list[Livro] = []

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
                return f'O livro "{livro.titulo}" foi emprestado com sucesso.'
        return "Livro não disponível ou não encontrado."

    def devolver_livro(self, codigo):
        for livro in self.livros:
            if livro.codigo == codigo and not livro.disponivel:
                livro.disponivel = True
                return f'O livro "{livro.titulo}" foi devolvido com sucesso.'
        return "Livro não está emprestado ou não encontrado."
    
    def carregar_livros_json(self, arquivo):
        try:
            with open(arquivo, 'r', encoding='utf-8') as file:
                livros_json = json.load(file)
                for livro_json in livros_json:
                    livro = Livro(
                        livro_json['titulo'],
                        livro_json['autor'],
                        livro_json['codigo']
                    )
                    self.adicionar_livro(livro)
            print(f"{len(self.livros)} livro(s) carregado(s) de '{arquivo}'.")
        except FileNotFoundError:
            print(f"Arquivo '{arquivo}' não encontrado.")
        except json.JSONDecodeError:
            print(f"Erro ao ler o arquivo '{arquivo}'. Verifique se o JSON está correto.")
        except Exception as e:
            print(f"Erro ao carregar os livros: {e}")