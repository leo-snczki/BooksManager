from leitor import Leitor
from terminal import click_para_continuar
import json

#  ______  _______     _     _______  _____   ______  
# / _____)(_______)   | |   (_______)/ ___ \ (_____ \ 
#| /  ___  _____       \ \   _      | |   | | _____) )
#| | (___)|  ___)       \ \ | |     | |   | |(_____ ( 
#| \____/|| |_____  _____) )| |_____| |___| |      | |
# \_____/ |_______)(______/  \______)\_____/       |_|
# _        _______  _____  _______  _____   ______    
#| |      (_______)(_____)(_______)/ ___ \ (_____ \   
#| |       _____      _    _      | |   | | _____) )  
#| |      |  ___)    | |  | |     | |   | |(_____ (   
#| |_____ | |_____  _| |_ | |_____| |___| |      | |  
#|_______)|_______)(_____) \______)\_____/       |_|                                                       


class GestorLeitor:
    def __init__(self):
        self.leitores: list[Leitor] = []
        self.arquivo = 'leitores.json'

# ============================
# _adicionar_leitor
# ============================
    def adicionar_leitor(self, leitor):
        self.leitores.append(leitor)

# ============================
# _remover_leitor
# ============================
    def remover_leitor(self, leitor):
        self.leitores.remove(leitor)

# ============================
# _listar_leitores
# ============================
    def listar_leitores(self):
        return self.leitores
    
# ============================
# _encontrar_leitor
# ============================
    def encontrar_leitor(self, identificador):
        return next(
            (l for l in self.leitores if l.nome.lower() == identificador.lower() or l.matricula.lower() == identificador.lower()),
            # Se não encontrar, retorna None.
            None
        )
    
# ============================
# _carregar_leitores_json
# ============================
    def carregar_leitores_json(self):
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as file:
                leitores_json = json.load(file)
                for leitor_json in leitores_json:
                    leitor = Leitor.from_dict(leitor_json)
                    self.adicionar_leitor(leitor)
                return True # permite o if no main.py
        
        # Todas as exceções abaixo vão retornar none, 
        # logo a confirmação do case não vai aparecer.
        
        except FileNotFoundError:
            print(f"Arquivo '{self.arquivo}' não encontrado.")
            print("Nenhum livro foi carregado.\n")
            click_para_continuar()
        except json.JSONDecodeError:
            print(f"Erro ao ler o arquivo '{self.arquivo}'. Verifique se o JSON está correto.\n")
            print("Nenhum livro foi carregado.\n")
            click_para_continuar()
        except Exception as e:
            print(f"Erro ao carregar os leitores: {e}\n")
            print("Nenhum livro foi carregado.\n")
            click_para_continuar()
        
# ============================
# _salvar_leitores_json
# ============================
    def salvar_leitores_json(self):
        try:
            with open(self.arquivo, 'w', encoding='utf-8') as file:
                # Converte a lista de leitores para lista de dicionários
                leitores_dicts = [leitor.to_dict() for leitor in self.leitores]
                json.dump(leitores_dicts, file, ensure_ascii=False, indent=4)
                return True # permite o if no main.py
        except Exception as e:
            print(f"Erro ao salvar os leitores: {e}\n")

