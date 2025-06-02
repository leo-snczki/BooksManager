import json
from livro import Livro
from emprestimo import EmprestimoLivro

class gestorLivros:

    def __init__(self):
        self.livros: list[Livro] = []
        self.emprestimos: list[EmprestimoLivro] = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, livro):
        self.livros.remove(livro)

    def listar_livros(self):
        return self.livros
    
    def emprestar_livro(self, codigo, nome_leitor, matricula, data_emprestimo):
        for livro in self.livros:
            if livro.codigo == codigo and livro.disponivel:
                livro.disponivel = False
                emprestimo = EmprestimoLivro(
                    livro.titulo, livro.autor, livro.codigo, 
                    data_emprestimo, nome_leitor, matricula
                )
                self.emprestimos.append(emprestimo)
                return f'O livro "{livro.titulo}" foi emprestado com sucesso.'
        return "Livro não disponível ou não encontrado."
    
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