import json
import requests
from livro import Livro
from emprestimo import EmprestimoLivro
from terminal import click_para_continuar
from datetime import datetime

class gestorLivros:

    def __init__(self):
        self.livros: list[Livro] = []
        self.emprestimos: list[EmprestimoLivro] = []
        self.devolucoes: list[EmprestimoLivro] = []
        self.arquivo_livros = "livros.json"
        self.arquivo_emprestimos = "emprestimos.json"
        self.arquivo_devolucoes = "devolucoes.json"

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
        for devolucao in self.emprestimos:
            if devolucao.livro.codigo == codigo:
                devolucao.livro.disponivel = True
                devolucao.data_devolvida = datetime.now().strftime("%d/%m/%Y")
                self.emprestimos.remove(devolucao)
                self.devolucoes.append(devolucao)
                return f'O livro "{devolucao.livro.titulo}" foi devolvido com sucesso por {devolucao.leitor.matricula}:{devolucao.leitor.nome}.'
        return "Livro não encontrado nos empréstimos."
    
    def listar_devolucoes(self):
        return self.devolucoes

    def listar_emprestimos(self):
        return self.emprestimos
    
    def carregar_livros_json(self):
        try:
            with open(self.arquivo_livros, 'r', encoding='utf-8') as file:
                livros_json = json.load(file)
                for livro_json in livros_json:
                    livro = Livro.from_dict(livro_json)
                    self.adicionar_livro(livro)
                return True # permite o if no main.py
            
        # Todas as exceções abaixo vão retornar none, 
        # logo a confirmação do case não vai aparecer.
        
        except FileNotFoundError:
            print(f"Arquivo '{self.arquivo_livros}' não encontrado.\n")
            print("Nenhum livro foi carregado.\n")
            click_para_continuar()
        except json.JSONDecodeError:
            print(f"Erro ao ler o arquivo '{self.arquivo_livros}'. Verifique se o JSON está correto.\n")
            print("Nenhum livro foi carregado.\n")            
            click_para_continuar()
        except Exception as e:
            print(f"Erro ao carregar os livros: {e}\n")
            print("Nenhum livro foi carregado.\n")
            click_para_continuar()
    
    def carregar_emprestimos_json(self):
        try:
            with open(self.arquivo_emprestimos, 'r', encoding='utf-8') as file:
                emprestimos_json = json.load(file)
            for emprestimo_json in emprestimos_json:
                emprestimo = EmprestimoLivro.from_dict(emprestimo_json)
                self.emprestimos.append(emprestimo)
            return True
        
        # Todas as exceções abaixo vão retornar none, 
        # logo a confirmação do case não vai aparecer.
        
        except FileNotFoundError:
            print(f"Arquivo '{self.arquivo_emprestimos}' não encontrado.\n")
            print("Nenhum empréstimo foi carregado.\n")
            click_para_continuar()
        except json.JSONDecodeError:
            print(f"Erro ao ler o arquivo '{self.arquivo_emprestimos}'. Verifique se o JSON está correto.\n")
            print("Nenhum empréstimo foi carregado.\n")
            click_para_continuar()
        except Exception as e:
            print(f"Erro ao carregar os empréstimos: {e}\n")
            print("Nenhum empréstimo foi carregado.\n")
            click_para_continuar()

    def carregar_devolucoes_json(self):
        try:
            with open(self.arquivo_devolucoes, 'r', encoding='utf-8') as file:
                devolucoes_json = json.load(file)
            for devolucao_json in devolucoes_json:
                devolucao = EmprestimoLivro.from_dict(devolucao_json)
                self.devolucoes.append(devolucao)
            return True
        except FileNotFoundError:
            print("Arquivo 'devolucoes.json' não encontrado.\n")
            print("Nenhuma devolução foi carregada.\n")
            click_para_continuar()
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo 'devolucoes.json'. Verifique se o JSON está correto.\n")
            print("Nenhuma devolução foi carregada.\n")
            click_para_continuar()
        except Exception as e:
            print(f"Erro ao carregar as devoluções: {e}\n")
            print("Nenhuma devolução foi carregada.\n")
            click_para_continuar()


    def salvar_livros_json(self):
        try:
            livros_json = [livro.to_dict() for livro in self.livros]
            with open(self.arquivo_livros, 'w', encoding='utf-8') as file:
                json.dump(livros_json, file, indent=4, ensure_ascii=False)
            return True # permite o if no main.py
        except Exception as e:
            print(f"Erro ao salvar os livros: {e}")
            click_para_continuar()

    def salvar_emprestimos_json(self):
        try:
            emprestimos_json = [emprestimo.to_dict() for emprestimo in self.emprestimos]
            with open(self.arquivo_emprestimos, 'w', encoding='utf-8') as file:
                json.dump(emprestimos_json, file, indent=4, ensure_ascii=False)
            return True # permite o if no main.py
        except Exception as e:
            print(f"Erro ao salvar os emprestimos: {e}")
            click_para_continuar()
    
    def salvar_devolucoes_json(self):
        try:
            devolucoes_json = [devolucao.to_dict() for devolucao in self.devolucoes]
            with open(self.arquivo_devolucoes, 'w', encoding='utf-8') as file:
                json.dump(devolucoes_json, file, indent=4, ensure_ascii=False)
            return True # permite o if no main.py
        except Exception as e:
            print(f"Erro ao salvar as devoluções: {e}")
            click_para_continuar()
            
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
                print(f"\n'{titulo}' foi adicionado com sucesso.")
                click_para_continuar()
                return
        print("Código não encontrado nos resultados.")
        click_para_continuar()
