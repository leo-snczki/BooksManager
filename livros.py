from clear import clear_term

class Livro:
    contador_codigo = 0

    def __init__(self, titulo, autor, codigo, status, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.status = status
        self.quantidade = quantidade

    def cadastrar_livro(self):
        print("Bem Vindo A Opção De Criação De Livros.\n\n")
        self.titulo = str(input("Digite o título do livro: "))
        self.autor = str(input("Digite o nome do autor: "))
        self.quantidade = int(input("Digite a quantidade de livros: "))
        Livro.contador_codigo += 1 
        self.codigo = Livro.contador_codigo
        return input(f"O livro {self.titulo} foi criado com sucesso.\n\nAperte ENTER para continuar.")

        #while True:
            #status = str(input("Escolha o status do livro:\n\n1 - Disponível\n2 - Emprestado\n\nOpção: "))
            #os.system("cls")
            #if status == "1":
                #self.status = "Disponível"
                #break
            #elif status == "2":
                #self.status = "Emprestado"
                #break
            #else:
                #input("Opção inválida.\n\nAperte ENTER para continuar.")
                #os.system("cls")
            #os.system("cls")
            #return input(f"O livro {self.titulo} foi criado com sucesso.\n\nAperte ENTER para continuar.")

    def alterar_status(self):
        opção = str(input(f"O livro {self.titulo} está {self.status}.\n\nDeseja alterar o status do livro?\n\n1 - Sim\n2 - Não\n\nOpção: "))
        clear_term()
        if opção == "1":
            while True:
                status = str(input(f"Escolha o novo status do livro {self.titulo}:\n\n1 - Disponível\n2 - Emprestado\n\nOpção: "))
                clear_term()
                if status == "1":
                    self.status = "Disponível"
                elif status == "2":
                    self.status = "Emprestado"
                else:
                    input("Opção inválida.\n\nAperte ENTER para continuar.")
                    clear_term()
                clear_term()


                return input(f"O status do livro {self.titulo} foi alterado para {self.status}.\n\nAperte ENTER para continuar.")
        elif opção == "2":
            return input(f"O status do livro {self.titulo} não foi alterado.\n\nAperte ENTER para continuar.")
        else:
            return input("Opção inválida.\n\nAperte ENTER para continuar.")
