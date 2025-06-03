from leitor import Leitor
from readkeys import getch
import json

class GestorLeitor:

    def __init__(self):
        self.leitores: list[Leitor] = []

    def adicionar_leitor(self, leitor):
        self.leitores.append(leitor)

    def remover_leitor(self, leitor):
        self.leitores.remove(leitor)

    def listar_leitores(self):
        return self.leitores
    
    def encontrar_leitor(self, identificador):
        return next(
            (l for l in self.leitores if l.nome.lower() == identificador.lower() or l.matricula.lower() == identificador.lower()),
            # Se não encontrar, retorna None.
            None
        )
    
    def carregar_leitores_json(self, arquivo):
        try:
                with open(arquivo, 'r', encoding='utf-8') as file:
                    leitores_json = json.load(file)
                    for leitor_json in leitores_json:
                        leitor = Leitor(
                            leitor_json['nome'],
                            leitor_json['matricula']
                        )
                        self.adicionar_leitor(leitor)
                    print(f"{len(self.leitores)} leitores carregados de '{arquivo}'.\n")
        except FileNotFoundError:
            print(f"Arquivo '{arquivo}' não encontrado.")
            print("Ao clicar, a execução vai continuar sem o arquivo...")
            getch()
        except json.JSONDecodeError:
            print(f"Erro ao ler o arquivo '{arquivo}'. Verifique se o JSON está correto.\n")
            print("Ao clicar, a execução vai continuar sem o arquivo...")
            getch()
        except Exception as e:
            print(f"Erro ao carregar os leitores: {e}\n")
            print("Ao clicar, a execução vai continuar sem o arquivo...")
            getch()

