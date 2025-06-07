from livro import Livro
from leitor import Leitor
from datetime import datetime,timedelta


# _______  ______   ______  ______   _______     _     _______  _____  ______    _____  
#(_______)|  ___ \ (_____ \(_____ \ (_______)   | |   (_______)(_____)|  ___ \  / ___ \ 
# _____   | | _ | | _____) )_____) ) _____       \ \   _          _   | | _ | || |   | |
#|  ___)  | || || ||  ____/(_____ ( |  ___)       \ \ | |        | |  | || || || |   | |
#| |_____ | || || || |           | || |_____  _____) )| |_____  _| |_ | || || || |___| |
#|_______)|_||_||_||_|           |_||_______)(______/  \______)(_____)|_||_||_| \_____/ 
#                       _        _____  _    _  ______    _____                         
#                      | |      (_____)| |  | |(_____ \  / ___ \                        
#                      | |         _   | |  | | _____) )| |   | |                       
#                      | |        | |   \ \/ / (_____ ( | |   | |                       
#                      | |_____  _| |_   \  /        | || |___| |                       
#                      |_______)(_____)   \/         |_| \_____/                                                                                                               


class EmprestimoLivro:
    def __init__(self, livro: Livro, leitor:Leitor, data_emprestimo=None, data_para_devolucao=None, data_devolvida=None):
        self.livro = livro
        self.leitor = leitor
        self.data_emprestimo = datetime.today()
        self.data_para_devolucao = (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y")
        self.data_devolvida = data_devolvida # se tipar para string e deixar como "", a data é dada como vazia na importação de json.

# ============================
# _to_dict
# ============================
    def to_dict(self):
        return {
            "livro": self.livro.to_dict(),
            "leitor": self.leitor.to_dict(),
            "data_emprestimo": self.data_emprestimo.strftime("%d/%m/%Y"),
            "data_para_devolucao": self.data_para_devolucao,
            "data_devolvida": self.data_devolvida
        }
    
# ============================
# _from_dict
# ============================
    @staticmethod
    def from_dict(data):
        data_emprestimo = datetime.strptime(data["data_emprestimo"], "%d/%m/%Y") if "data_emprestimo" in data else None
        data_para_devolucao = data["data_para_devolucao"] if "data_para_devolucao" in data else None
        data_devolvida = data["data_devolvida"] if "data_devolvida" in data else None
        # Se não tiver os dados do arquivo json, seta o valor como None.
        return EmprestimoLivro(
            livro=Livro.from_dict(data["livro"]),
            leitor=Leitor.from_dict(data["leitor"]),
            data_emprestimo=data_emprestimo,
            data_para_devolucao=data_para_devolucao,
            data_devolvida=data_devolvida
        )