from terminal import limpar_term,click_para_continuar
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
        "6 - Salvar",	
        "7 - Carregar",
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

def MostrarMenuSalvar():
    opcoes = [
        "1 - Salvar Todos os dados",
        "2 - Salvar Livros",
        "3 - Salvar Leitores",
        "4 - Salvar Empréstimos",
        "0 - Voltar"
    ]

    print("\n".join(opcoes))
    print("\nOpção: ", end="")

def MostrarMenuCarregar():
    opcoes = [
        "1 - Carregar Todos os dados",
        "2 - Carregar Livros",
        "3 - Carregar Leitores",
        "4 - Carregar Empréstimos",
        "0 - Voltar"
    ]

    print("\n".join(opcoes))
    print("\nOpção: ", end="")

def SairDoLoop():
    limpar_term()
    print("Deseja realmente sair?")
    sair = input("Digite 's' para sair ou 'n' para continuar: ")    
    if sair == "n":
        return False
    else:
        return True

def cadastrar_leitor():
    limpar_term()
    print("Cadastrar novo leitor")
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    leitor = Leitor(nome, matricula)
    leitores_gestor.adicionar_leitor(leitor)
    print(f"\nLeitor '{nome}' cadastrado com sucesso!")
    click_para_continuar()
    
def listar_leitores():
    limpar_term()
    leitores = leitores_gestor.listar_leitores()
    if not leitores:
        print("Nenhum leitor cadastrado.")
    else:
        print("Leitores cadastrados:\n")
        for leitor in leitores:
            print(f"{leitor.matricula}: {leitor.nome}")
    click_para_continuar()
    
def criar_livro():
    limpar_term()
    print("Criar novo livro")
    titulo = input("Título: ")
    autor = input("Autor: ")
    codigo = input("Código: ")
    livro = Livro(titulo, autor, codigo)
    livros_gestor.adicionar_livro(livro)
    print(f"\nLivro '{titulo}' adicionado com sucesso!")

    click_para_continuar()

def listar_livros():

    limpar_term()
    livros = livros_gestor.listar_livros()
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        for livro in livros:
            status = "Disponível" if livro.disponivel else "Emprestado"
            print(f"{livro.codigo}: {livro.titulo} - {livro.autor} ({status})")
    click_para_continuar()

def emprestar_livro():
    limpar_term()
    print("Emprestar Livro")
    
    codigo = input("Código do livro: ")
    identificador = input("Nome ou Matrícula do leitor: ")

    leitor = leitores_gestor.encontrar_leitor(identificador)
    if leitor is None: # Se o leitor não existir.
        print("\nLeitor não encontrado.")
    else:
        resultado = livros_gestor.emprestar_livro_obj(codigo, leitor)
        print(f"\n{resultado}")
    click_para_continuar()

def listar_emprestimos():

    limpar_term()
    emprestimos = livros_gestor.listar_emprestimos()
    if not emprestimos:
        print("Nenhum empréstimo em curso.")
    else:
        for emp in emprestimos:
            print(f"{emp.leitor.matricula} - {emp.livro.titulo}:{emp.livro.codigo} - data para devolver: {emp.data_para_devolucao}")
    click_para_continuar()

def pesquisar_adicionar_livro():
    termo = input("Digite o título, autor ou palavra-chave para buscar livros: ")
    resultados = livros_gestor.pesquisar_livros_openlibrary(termo)

    if not resultados:
        print("Nenhum livro encontrado.")
        click_para_continuar()
        return True

    print("\nResultados encontrados:")
    for i, (codigo, titulo, autor) in enumerate(resultados, start=1):
        print(f"{i}. [{codigo}] {titulo} - {autor}")

    escolha = input("Digite o número do livro que deseja adicionar (ou Enter para cancelar): ")
    if not escolha.isdigit():
        print("\nOperação cancelada.")
        click_para_continuar()
        return

    index = int(escolha) - 1
    if not 0 <= index < len(resultados):
        print("Número inválido.")        
        click_para_continuar()
    else:
        codigo = resultados[index][0]
        livros_gestor.adicionar_livro_por_codigo(codigo, resultados)


def Menu(opcao):
    match opcao:
        case "1":  # Adicionar
            while True:
                limpar_term()
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
                        click_para_continuar()
            return True

        case "2":  # Ver
            while True:
                limpar_term()
                MostrarMenuVer()
                sub_opcao = input()
                match sub_opcao:
                    case "1":
                        listar_livros()
                    case "2":
                        listar_leitores()
                    case "3":
                        listar_emprestimos()
                    case "4":
                        print("Ver ultimas devoluções ainda não implementado.")
                        click_para_continuar()
                    case "0":
                        break
                    case _:
                        print("Opção inválida.")
                        click_para_continuar()
            return True

        case "3":  # Deletar
            while True:
                limpar_term()
                MostrarMenuDeletar()
                sub_opcao = input()
                match sub_opcao:
                    case "1":
                        print("Deletar livro ainda não implementado.")
                        click_para_continuar()
                    case "2":
                        print("Deletar leitor ainda não implementado.")
                        click_para_continuar()
                    case "0":
                        break
                    case _:
                        print("Opção inválida.")
                        click_para_continuar()
            return True

        case "4":  # Emprestar
            emprestar_livro()
            return True

        case "5":  # Devolver
            print("Devolução ainda não implementada.")
            click_para_continuar()
            return True

        case "6": # Salvar
            while True:
                limpar_term()
                MostrarMenuSalvar()
                sub_opcao = input()
                match sub_opcao:
                    case "1":
                        if livros_gestor.salvar_livros_json() and leitores_gestor.salvar_leitores_json():
                            print(f"{len(livros_gestor.livros)} livros e {len(leitores_gestor.leitores)} leitores salvos em '{leitores_gestor.arquivo}'.")
                            click_para_continuar()
                    case "2":
                        if livros_gestor.salvar_livros_json():        
                            print(f"{len(livros_gestor.livros)} livros salvos com sucesso em '{livros_gestor.arquivo}'.")
                            click_para_continuar()
                    case "3":
                        if leitores_gestor.salvar_leitores_json():
                            print(f"{len(leitores_gestor.leitores)} Leitores salvos com sucesso em '{leitores_gestor.arquivo}'.\n")
                            click_para_continuar()
                    case "0":
                        break
                    case _:
                            print("Opção inválida.")
                            click_para_continuar()
        case "7": # Carregar
            while True:
                limpar_term()
                MostrarMenuCarregar()
                sub_opcao = input()
                match sub_opcao:
                    case "1":
                        if livros_gestor.carregar_livros_json() and leitores_gestor.carregar_leitores_json():
                            print("livros e leitores carregados'.\n")
                            click_para_continuar()
                    case "2":
                        if livros_gestor.carregar_livros_json():
                            print("livros carregados'.\n")
                            click_para_continuar()        
                    case "3":
                        if leitores_gestor.carregar_leitores_json():
                            print("leitores carregados'.\n")
                            click_para_continuar()
                    case "0":
                        break
                    case _:
                        print("Opção inválida.")
                        click_para_continuar()
        case "0":  # Voltar/Sair
            return not SairDoLoop()

        case _:
            print("Opção inválida.")
            click_para_continuar()           
            return True


leitores_gestor.carregar_leitores_json()
livros_gestor.carregar_livros_json()
continuar = True

while(continuar):
    limpar_term()
    MostrarMenuInicial()
    opcao = str(input())
    continuar = Menu(opcao)
