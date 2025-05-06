class Aluno:
    numero_do_Aluno = 0

    def __init__(self, nome, matricula, lista_de_livros):
        self.nome = nome
        self.matricula = matricula
        self.lista_de_livros = lista_de_livros

    def cadastrar_aluno(self):
        print("Bem Vindo A Opção De Cadastro De Alunos.\n\n")
        self.nome = str(input("Digite o nome do aluno: "))
        Aluno.numero_do_Aluno += 1 
        self.matricula = (f"L{Aluno.numero_do_Aluno}")
        self.lista_de_livros = 0
        return input(f"O alunos {self.nome} foi cadastrado com sucesso.\n\nAperte ENTER para continuar.")