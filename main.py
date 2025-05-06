from clear import clear_term
import alunos
import livros

def ver_alunos(alunos_cadastrados):
    for i in range(len(alunos_cadastrados)):
        aluno = alunos_cadastrados[i]
        print(f"Aluno: ({aluno.nome}) - matrícula: ({aluno.matricula}) - Lista De Livros Emprestados: ({aluno.lista_de_livros}).")
        print("\n")
    if len(alunos_cadastrados) == 0:
            print("Não há alunos cadastrados.\n")
    return input("Aperte ENTER para continuar."), clear_term()

def ver_livros(livros_criados):
    for i in range(len(livros_criados)):
        livro = livros_criados[i]
        print(f"Código Do Livro: ({livro.codigo}) - Livro: ({livro.titulo}) - Autor: ({livro.autor}) - Quantidade De Livros: ({livro.quantidade}).")
        print("\n")
    if len(livros_criados) == 0:
            print("Não há livros cadastrados.\n")
    return input("Aperte ENTER para continuar."), clear_term()


livros_criados = []
livro = ""

alunos_cadastrados = []
aluno = ""

while True:
    clear_term()
    opcao = str(input("1 - Criar livro\n2 - Ver livros\n3 - Cadastrar aluno\n4 - Ver alunos\n5 - Alterar status de um livro\n6 - Sair\n\nOpção: "))
    
    if opcao == "1":
        livro = livros("", "", "", "", "")
        print(livro.cadastrar_livro())
        livros_criados.append(livro)

    elif opcao == "2":
        alunos.ver_livros(livros_criados)

    elif opcao == "3":
        aluno = alunos("", "", "")
        print(aluno.cadastrar_aluno())
        alunos_cadastrados.append(aluno)

    elif opcao == "4":
        ver_alunos(alunos_cadastrados)

    elif opcao == "5":
        for i in range(len(livros_criados)):
            livro = livros_criados[i]
            print(f"Código Do Livro: ({livro.codigo}) - Livro: ({livro.titulo}) - Autor: ({livro.autor}) - Quantidade De Livros: ({livro.quantidade}).")
            print("\n")
        opcao = str(input("Digite o código do livro que deseja emprestar: "))
        if livro.codigo == opcao:
            print(livro.alterar_status())
            break
        else:
            input("Livro não encontrado.\n\nAperte ENTER para continuar.")

    elif opcao == "6":
        break
    else:
        input("Opção inválida.\n\nAperte ENTER para continuar.")
