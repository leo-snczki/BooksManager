class Leitor:
    quantidade_de_Alunos = 0

    def __init__(self, nome, matricula, lista_de_livros):
        self.nome = nome
        self.matricula = matricula
        self.lista_de_livros = lista_de_livros

    def cadastrar_aluno(self):
        print("Bem Vindo A Opção De Cadastro De Leitor.\n\n")
        self.nome = str(input("Digite o nome do Leitor: "))
        Leitor.quantidade_de_Alunos += 1 
        self.matricula = (f"L{Leitor.numero_do_Aluno}")
        self.lista_de_livros = 0
        return input(f"O alunos {self.nome} foi cadastrado com sucesso.\n\nAperte ENTER para continuar.")