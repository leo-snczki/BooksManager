from clear import clear_term
from readkeys import getch
#from emprestimo import EmprestimoLivro

def MostrarMenu():
    opcoes = [
        "1 - Criar livro",
        "2 - Ver livros",
        "3 - Cadastrar leitor",
        "4 - Ver leitores",
        "5 - Alterar status de um livro",
        "6 - Sair"
    ]
    
    print("\n".join(opcoes))
    print("\nOpção: ", end="")

def Menu (opcao):
    match opcao:
        case "1":
            return True # Lógica não implementada ainda
        case "2":
            return True # Lógica não implementada ainda
        case "3":
            return True # Lógica não implementada ainda
        case "4":
            return True # Lógica não implementada ainda
        case "5":
            return True # Lógica não implementada ainda
        case "6":
            return False
        case _:
            print("\nOpção inválida.\n")
            getch(print("Pressione qualquer tecla para tentar novamente..."))
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
