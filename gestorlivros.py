import json
import requests
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
    
    def emprestar_livro_obj(self, codigo, leitor):
        for livro in self.livros:
            if livro.codigo == codigo and livro.disponivel:
                livro.disponivel = False
                emprestimo = EmprestimoLivro(livro, leitor)
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

    def pesquisar_livros_openlibrary(self, termo_busca, max_resultados=5):
        url = f"https://openlibrary.org/search.json?q={termo_busca}"
        try:
            response = requests.get(url)

            if response.status_code != 200:
                print(f"Erro ao acessar a API: {response.status_code}")
                return

            dados = response.json()
            resultados = []
            for doc in dados.get("docs", [])[:max_resultados]:
                titulo = doc.get("title", "Título desconhecido")
                autor = doc.get("author_name", ["Autor desconhecido"])[0]
                codigo = doc.get("key", "").replace("/works/", "")
                resultados.append((codigo, titulo, autor))
            return resultados

        except Exception as e:
            print(f"Erro ao buscar livros na Open Library: {e}")
            return
    
    def adicionar_livro_por_codigo(self, codigo, resultados):
        for cod, titulo, autor in resultados:
            if cod == codigo:
                if any(livro.codigo == codigo for livro in self.livros):
                    print("Livro já está na lista.")
                    return
                livro = Livro(titulo, autor, codigo)
                self.adicionar_livro(livro)
                print(f'"{titulo}" foi adicionado com sucesso.')
                return
        print("Código não encontrado nos resultados.")
