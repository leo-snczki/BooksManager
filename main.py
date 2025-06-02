from clear import clear_term
from readkeys import getch
#from emprestimo import EmprestimoLivro
from gestorLeitor import GestorLeitor
from gestorlivros import gestorLivros
from leitor import Leitor
from livro import Livro

clear_term()

leitores_gestor = GestorLeitor()
livros_gestor = gestorLivros()

def MostrarMenu():
    opcoes = [
        "1 - Criar Livro",
        "2 - Cadastrar Leitor",
        "3 - Ver Livros",
        "4 - Ver leitores",
        "5 - Deletar Livro",
        "6 - Deletar Leitor",
        "7 - Emprestar Livro",
        "8 - Devolver Livro",
        "0 - Sair"
    ]
    
    print("\n".join(opcoes))
    print("\nOpção: ", end="")

def SairDoLoop():
    clear_term()
    print("Deseja realmente sair?")
    sair = input("Digite 's' para sair ou 'n' para continuar: ")
    if sair == "s":
        return False
    else:
        return True

def cadastrar_leitor():
    clear_term()
    print("Cadastrar novo leitor")
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    leitor = Leitor(nome, matricula)
    leitores_gestor.adicionar_leitor(leitor)
    print(f"\nLeitor '{nome}' cadastrado com sucesso!")
    print("\nPressione qualquer tecla para continuar...")
    getch()
    
def listar_leitores():
    clear_term()
    leitores = leitores_gestor.listar_leitores()
    if not leitores:
        print("Nenhum leitor cadastrado.")
    else:
        print("Leitores cadastrados:\n")
        for leitor in leitores:
            print(f"{leitor.matricula}: {leitor.nome}")
    print("\nPressione qualquer tecla para continuar...")
    getch()
    
def criar_livro():
    clear_term()
    print("Criar novo livro")
    titulo = input("Título: ")
    autor = input("Autor: ")
    codigo = input("Código: ")
    livro = Livro(titulo, autor, codigo)
    livros_gestor.adicionar_livro(livro)
    print(f"\nLivro '{titulo}' adicionado com sucesso!")
    print("\nPressione qualquer tecla para continuar...")
    getch()

def listar_livros():

    clear_term()
    livros = livros_gestor.listar_livros()
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        for livro in livros:
            status = "Disponível" if livro.disponivel else "Emprestado"
            print(f"{livro.codigo}: {livro.titulo} - {livro.autor} ({status})")
    print("\nPressione qualquer tecla para continuar...")
    getch()

def Menu (opcao):
    match opcao:
        case "1":
            criar_livro()
            return True
        case "2":
            cadastrar_leitor()
            return True
        case "3":           
            listar_livros()
            return True
        case "4":
            listar_leitores()
            return True
        case "5":
            return True # Lógica não implementada ainda
        case "6":
            return True # Lógica não implementada ainda
        case "7":
            return True # Lógica não implementada ainda
        case "8":
            return True # Lógica não implementada ainda
        case "0":
            SairDoLoop()
        case _:
            print("\nOpção inválida.\n")
            getch()
            print("Pressione qualquer tecla para tentar novamente...")
            return True

#                             _      
# ___ __ __ ___  _ __   _ __ | | ___ 
#/ -_)\ \ // -_)| '  \ | '_ \| |/ _ \
#\___|/_\_\\___||_|_|_|| .__/|_|\___/
# __| | ___   _  _  ___|_|_          
#/ _` |/ -_) | || |(_-</ _ \         
#\__,_|\___|  \_,_|/__/\___/   

#emprestimo = EmprestimoLivro("O pequeno principe","Antoine de Saint-Exupéry", "6", "dia 19 de maio", "leonardo", "l2469")
#print(emprestimo.livro.autor)

continuar = True

while(continuar):
    clear_term()
    MostrarMenu()
    opcao = str(input())
    continuar = Menu(opcao)
