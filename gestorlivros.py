import json
import requests
from livro import Livro
from emprestimo import EmprestimoLivro
from terminal import click_para_continuar
from datetime import datetime


def obter_livros():
    """Obtém os livros do site da API"""
    response = requests.get("https://livraria-para-teste.herokuapp.com/livros")
    return response.json()

class gestorLivros:

    def __init__(self):
        self.livros: list[Livro] = []
        self.emprestimos: list[EmprestimoLivro] = []
        self.devolucoes: list[EmprestimoLivro] = []
        self.arquivo = "livros.json"

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
                return f'O livro "{livro.titulo}" foi emprestado com sucesso (Devolução: {emprestimo.data_para_devolucao}).'
        return "Livro não disponível ou não encontrado."

    def devolver_livro(self, codigo):
        for emprestimo in self.emprestimos:
            if emprestimo.livro.codigo == codigo:
                emprestimo.livro.disponivel = True
                emprestimo.data_devolvida = datetime.now().strftime("%d/%m/%Y")  # <-- aqui!
                self.emprestimos.remove(emprestimo)
                self.devolucoes.append(emprestimo)
                return f'O livro "{emprestimo.livro.titulo}" foi devolvido com sucesso por {emprestimo.leitor}.'
        return "Livro não encontrado nos empréstimos."
    
    def listar_devolucoes(self):
        return self.devolucoes

    def listar_emprestimos(self):
        return self.emprestimos
    
    def carregar_livros_json(self):
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as file:
                livros_json = json.load(file)
                for livro_json in livros_json:
                    livro = Livro.from_dict(livro_json)
                    self.adicionar_livro(livro)
                return True # permite o if no main.py
            
        # Todas as exceções abaixo vão retornar none, 
        # logo a confirmação do case não vai aparecer.
        
        except FileNotFoundError:
            print(f"Arquivo '{self.arquivo}' não encontrado.\n")
            print("Nenhum livro foi carregado.\n")
            click_para_continuar()
        except json.JSONDecodeError:
            print(f"Erro ao ler o arquivo '{self.arquivo}'. Verifique se o JSON está correto.\n")
            print("Nenhum livro foi carregado.\n")            
            click_para_continuar()
        except Exception as e:
            print(f"Erro ao carregar os livros: {e}\n")
            print("Nenhum livro foi carregado.\n")
            click_para_continuar()

    def salvar_livros_json(self):
        try:
            livros_json = [livro.to_dict() for livro in self.livros]
            with open(self.arquivo, 'w', encoding='utf-8') as file:
                json.dump(livros_json, file, indent=4, ensure_ascii=False)
            return True # permite o if no main.py
        except Exception as e:
            print(f"Erro ao salvar os livros: {e}")

    def pesquisar_livros_openlibrary(self, termo_busca, max_resultados=5):
        url = f"https://openlibrary.org/search.json?q={termo_busca}"
        try:
            response = requests.get(url)

            if response.status_code != 200:
                raise Exception(f"Erro {response.status_code} ao acessar a API")

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
            click_para_continuar()
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
                click_para_continuar()
                return
        print("Código não encontrado nos resultados.")
        click_para_continuar()
