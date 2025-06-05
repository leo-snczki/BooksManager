from clear import clear_term
from readkeys import getch
from gestorLeitor import GestorLeitor
from gestorlivros import gestorLivros
from leitor import Leitor
from livro import Livro

leitores_gestor = GestorLeitor()
livros_gestor = gestorLivros()

def MostrarMenuInicial():
    opcoes = [
        "1 - Adicionar",
        "2 - Ver",
        "3 - Deletar",
        "4 - Emprestar",
        "5 - Devolver",
        "0 - Sair"
    ]
    
    print("\n".join(opcoes))
    print("\nOpção: ", end="")
    
def MostrarMenuAdicionar():
    opcoes = [
        "1 - Adicionar Livro",
        "2 - Cadastrar Leitor",
        "3 - Pesquisar e adicionar Livro",
        "0 - Voltar"
    ]
    
    print("\n".join(opcoes))
    print("\nOpção: ", end="")

def MostrarMenuVer():
    opcoes = [
        "1 - Ver Livros",
        "2 - Ver Leitores",
        "3 - Ver empréstimos",
        "4 - Ver ultimas devoluções",
        "0 - Voltar"
    ]

    print("\n".join(opcoes))
    print("\nOpção: ", end="")

def MostrarMenuDeletar():
    opcoes = [
        "1 - Deletar Livro",
        "2 - Deletar Leitor",
        "0 - Voltar"
    ]

    print("\n".join(opcoes))
    print("\nOpção: ", end="")


def SairDoLoop():
    clear_term()
    print("Deseja realmente sair?")
    sair = input("Digite 's' para sair ou 'n' para continuar: ")    
    if sair == "n":
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

def emprestar_livro():
    clear_term()
    print("Emprestar Livro")
    
    codigo = input("Código do livro: ")
    identificador = input("Nome ou Matrícula do leitor: ")

    leitor = leitores_gestor.encontrar_leitor(identificador)
    if leitor is None: # Se o leitor não existir.
        print("\nLeitor não encontrado.")
    else:
        resultado = livros_gestor.emprestar_livro_obj(codigo, leitor)
        print(f"\n{resultado}")
    print("\nPressione qualquer tecla para continuar...")
    getch()

def pesquisar_adicionar_livro():
    termo = input("Digite o título, autor ou palavra-chave para buscar livros: ")
    resultados = livros_gestor.pesquisar_livros_openlibrary(termo)

    if not resultados:
        print("Nenhum livro encontrado.")
        return True

    print("\nResultados encontrados:")
    for i, (codigo, titulo, autor) in enumerate(resultados, start=1):
        print(f"{i}. [{codigo}] {titulo} - {autor}")

    escolha = input("Digite o número do livro que deseja adicionar (ou Enter para cancelar): ")
    if not escolha.isdigit():
        print("Operação cancelada.")
        getch()
        return

    index = int(escolha) - 1
    if not 0 <= index < len(resultados):
        print("Número inválido.")
        getch()
        
    else:
        codigo = resultados[index][0]
        livros_gestor.adicionar_livro_por_codigo(codigo, resultados)


def Menu(opcao):
    match opcao:
        case "1":  # Adicionar
            while True:
                clear_term()
                MostrarMenuAdicionar()
                sub_opcao = input()
                match sub_opcao:
                    case "1":
                        criar_livro()
                    case "2":
                        cadastrar_leitor()
                    case "3":
                        pesquisar_adicionar_livro()
                    case "0":
                        break
                    case _:
                        print("Opção inválida.")
                        getch()
            return True

        case "2":  # Ver
            while True:
                clear_term()
                MostrarMenuVer()
                sub_opcao = input()
                match sub_opcao:
                    case "1":
                        listar_livros()
                    case "2":
                        listar_leitores()
                    case "3":
                        print("Ver Empréstimos ainda não implementado.")
                        getch()
                    case "4":
                        print("Ver ultimas devoluções ainda não implementado.")
                        getch()
                    case "0":
                        break
                    case _:
                        print("Opção inválida.")
                        getch()
            return True

        case "3":  # Deletar
            while True:
                clear_term()
                MostrarMenuDeletar()
                sub_opcao = input()
                match sub_opcao:
                    case "1":
                        print("Deletar livro ainda não implementado.")
                        getch()
                    case "2":
                        print("Deletar leitor ainda não implementado.")
                        getch()
                    case "0":
                        break
                    case _:
                        print("Opção inválida.")
                        getch()
            return True

        case "4":  # Emprestar
            emprestar_livro()
            return True

        case "5":  # Devolver
            print("Devolução ainda não implementada.")
            getch()
            return True

        case "0":  # Voltar/Sair
            return not SairDoLoop()

        case _:
            print("Opção inválida.")
            getch()
            return True


leitores_gestor.carregar_leitores_json("leitores.json")
continuar = True

while(continuar):
    clear_term()
    MostrarMenuInicial()
    opcao = str(input())
    continuar = Menu(opcao)
