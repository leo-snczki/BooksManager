from terminal import limpar_term,click_para_continuar
from gestorLeitor import GestorLeitor
from gestorlivros import gestorLivros
from leitor import Leitor
from livro import Livro
from datetime import datetime

#  ______                       
# |  ___ \                      
# | | _ | |  ____  ____   _   _ 
# | || || | / _  )|  _ \ | | | |
# | || || |( (/ / | | | || |_| |
# |_||_||_| \____)|_| |_| \____|                           

# ============================
# _mostrar_menu_inicial
# ============================
def _mostrar_menu_inicial():
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

# ============================
# _mostrar_menu_adicionar
# ============================
def _mostrar_menu_adicionar():
    opcoes = [
        "1 - Adicionar Livro",
        "2 - Cadastrar Leitor",
        "3 - Pesquisar e adicionar Livro",
        "0 - Voltar"
    ]
    
    print("\n".join(opcoes))
    print("\nOpção: ", end="")

# ============================
# _mostrar_menu_ver
# ============================
def _mostrar_menu_ver():
    opcoes = [
        "1 - Ver Livros",
        "2 - Ver Leitores",
        "3 - Ver empréstimos",
        "4 - Ver ultimas devoluções",
        "5 - Ver livros emprestados por aluno",
        "0 - Voltar"
    ]

    print("\n".join(opcoes))
    print("\nOpção: ", end="")

# ============================
# _mostrar_menu_deletar
# ============================
def _mostrar_menu_deletar():
    opcoes = [
        "1 - Deletar Livro",
        "2 - Deletar Leitor",
        "0 - Voltar"
    ]

    print("\n".join(opcoes))
    print("\nOpção: ", end="")

# ============================
# _mostrar_menu_salvar
# ============================
def _mostrar_menu_salvar():
    opcoes = [
        "1 - Salvar Todos os dados",
        "2 - Salvar Livros",
        "3 - Salvar Leitores",
        "4 - Salvar Empréstimos e devoluções",
        "0 - Voltar"
    ]

    print("\n".join(opcoes))
    print("\nOpção: ", end="")

# ============================
# _mostrar_menu_carregar
# ============================
def _mostrar_menu_carregar():
    opcoes = [
        "1 - Carregar Todos os dados",
        "2 - Carregar Livros",
        "3 - Carregar Leitores",
        "4 - Carregar Empréstimos e devoluções",
        "0 - Voltar"
    ]

    print("\n".join(opcoes))
    print("\nOpção: ", end="")

#  _  _                          
# | |(_)       _                 
# | | _   ___ | |_   ____   ____ 
# | || | /___)|  _) / _  | / ___)
# | || ||___ || |__( ( | || |    
# |_||_|(___/  \___)\_||_||_|    

# ============================
# _listar_leitores
# ============================
def _listar_leitores():
    try:
        leitores = leitores_gestor.listar_leitores()
        if not leitores:
            print("Nenhum leitor cadastrado.")
        else:
            print("Leitores cadastrados:\n")
            for leitor in leitores:
                print(f"{leitor.matricula}: {leitor.nome}")
    except Exception as e:
        print(f"Ocorreu um erro ao listar os leitores: {e}")

# ============================
# _listar_livros
# ============================
def _listar_livros():
    try:
        livros = livros_gestor.listar_livros()
        if not livros:
            print("Nenhum livro cadastrado.")
        else:
            for livro in livros:
                status = "Disponível" if livro.disponivel else "Emprestado"
                print(f"{livro.codigo}: {livro.titulo} - {livro.autor} ({status})")
    except Exception as e:
        print(f"Ocorreu um erro ao listar os livros: {e}")
    finally:
        click_para_continuar()

# ============================
# _listar_devolucoes
# ============================
def _listar_devolucoes():
    try:
        if not livros_gestor.devolucoes:
            print("Nenhuma devolução registrada.")
            return

        print("Lista de Devoluções:")
        for dev in livros_gestor.devolucoes:
            # Se a data de devolução for Nula, exibe "Data desconhecida".
            data_devolucao = dev.data_devolvida or "Data desconhecida"
            print(f'- "{dev.livro.titulo}" por {dev.livro.autor}, devolvido por {dev.leitor.matricula}:{dev.leitor.nome} em {data_devolucao}')
    except Exception as e:
        print(f"Ocorreu um erro ao listar as devoluções: {e}")
    finally:
        click_para_continuar()

# ============================
# _listar_emprestimos
# ============================
def _listar_emprestimos():
    try:
        emprestimos = livros_gestor.listar_emprestimos()
        if not emprestimos:
            print("Nenhum empréstimo em curso.")
        else:
            for emp in emprestimos:
                print(f"{emp.leitor.matricula} - {emp.livro.titulo}:{emp.livro.codigo} - data para devolver: {emp.data_para_devolucao}")
    except Exception as e:
        print(f"Ocorreu um erro ao listar os empréstimos: {e}")
    finally:
        click_para_continuar()

# ============================
# _listar_livros_emprestados_por_aluno
# ============================
def _listar_livros_emprestados_por_aluno():
    try:
        identificador = input("Digite o nome ou matrícula do leitor: ").strip()
        if not identificador:
            print("Operação cancelada.")
            return
        
        leitor = leitores_gestor.encontrar_leitor(identificador)
        if not leitor:
            print("Leitor não encontrado.")
            return
        
        emprestimos = livros_gestor.listar_emprestimos_por_leitor(leitor)
        if not emprestimos:
            print(f"O leitor {leitor.nome} não possui livros emprestados.")
            return
        
        print(f"\nLivros emprestados por {leitor.nome}:\n")
        for emp in emprestimos:
            print(f"- {emp.livro.titulo} (Código: {emp.livro.codigo}) - Data para devolução: {emp.data_para_devolucao}")
    except Exception as e:
        print(f"Ocorreu um erro ao listar os livros emprestados: {e}")
    finally:
        click_para_continuar()


#             _  _         _                             
#            | |(_)       (_)                            
#   ____   _ | | _   ____  _   ___   ____    ____   ____ 
#  / _  | / || || | / ___)| | / _ \ |  _ \  / _  | / ___)
# ( ( | |( (_| || |( (___ | || |_| || | | |( ( | || |    
#  \_||_| \____||_| \____)|_| \___/ |_| |_| \_||_||_|                                                          

# ============================
# criar_livro
# ============================
def criar_livro():
    try:
        print("Criar novo livro")
        titulo = input("Título (ou pressione Enter para cancelar): ").strip()
        if titulo == "":
            limpar_term()
            print("Operação de criação de livro cancelada.")
            return
        autor = input("Autor (ou pressione Enter para cancelar): ").strip()
        if autor == "":
            limpar_term()
            print("Operação de criação de livro cancelada.")
            return
        codigo = input("Código (ou pressione Enter para cancelar): ").strip()
        if codigo == "":
            limpar_term()
            print("Operação de criação de livro cancelada.")
            return
        livro = Livro(titulo, autor, codigo)
        livros_gestor.adicionar_livro(livro)
        print(f"\nLivro '{titulo}' adicionado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o livro: {e}")
    finally:
        click_para_continuar()
# ============================
# _cadastrar_leitor
# ============================

def _cadastrar_leitor():
    try:
        print("Cadastrar novo leitor")
        nome = input("Nome (ou pressione Enter para cancelar): ").strip()
        if nome == "":
            limpar_term()
            print("Operação de cadastro de leitor cancelada.")
            return
        matricula = input("Matrícula (ou pressione Enter para cancelar): ").strip()
        if matricula == "":
            limpar_term()
            print("Operação de cadastro de leitor cancelada.")
            return
        leitor = Leitor(nome, matricula)
        leitores_gestor.adicionar_leitor(leitor)
        print(f"\nLeitor '{nome}' cadastrado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao cadastrar o leitor: {e}")
    finally:
        click_para_continuar()

# ============================
# pesquisar_adicionar_livro
# ============================
def pesquisar_adicionar_livro():
    try:
        termo = input("Digite o título, autor ou palavra-chave para buscar livros (ou pressione Enter para cancelar): ")
        
        if termo == "":
            limpar_term()
            print("Operação de pesquisa e adição de livro cancelada.")
            return
        
        resultados = livros_gestor.pesquisar_livros_openlibrary(termo)

        if not resultados:
            print("Nenhum livro encontrado.")
            return True

        print("\nResultados encontrados:")
        for i, (codigo, titulo, autor) in enumerate(resultados, start=1):
            print(f"{i}. [{codigo}] {titulo} - {autor}")

        escolha = input("\nDigite o número do livro que deseja adicionar (ou Enter para cancelar): ")
        if not escolha.isdigit():
            print("\nOperação cancelada.")
            return

        index = int(escolha) - 1
        if not 0 <= index < len(resultados):
            print("Número inválido.")        
        else:
            codigo = resultados[index][0]
            livros_gestor.adicionar_livro_por_codigo(codigo, resultados)
    except Exception as e:
        print(f"Ocorreu um erro ao pesquisar e adicionar o livro: {e}")                                                                                                 

#   ____  ____  ____    ___  _   _  ____   ____ 
#  / ___)/ _  )|    \  / _ \| | | |/ _  ) / ___)
# | |   ( (/ / | | | || |_| |\ V /( (/ / | |    
# |_|    \____)|_|_|_| \___/  \_/  \____)|_|                                                 

# ============================
# _remover_livro
# ============================
def _remover_livro():
    try:
        print("Remover Livro")
        codigo = input("Código do livro a remover (ou pressione Enter para cancelar): ").strip()
        if codigo == "":
            limpar_term()
            print("Operação de remoção de livro cancelada.")
            return
        livro = next((l for l in livros_gestor.livros if l.codigo == codigo), None)
        if not livro:
            print("\nLivro não encontrado.")
            return
        emprestado = any(e.livro.codigo == codigo for e in livros_gestor.emprestimos)
        if emprestado:
            print("\nEste livro está emprestado e não pode ser removido.")
            return
        livros_gestor.remover_livro(livro)
        print(f'\nLivro "{livro.titulo}" removido com sucesso.')
    except Exception as e:
        print(f"Ocorreu um erro ao remover o livro: {e}")
    finally:
        click_para_continuar()

# ============================
# _remover_leitor
# ============================
def _remover_leitor():
    try:
        print("Remover Leitor\n")
        _listar_leitores()
        identificador = input("\nNome ou Matrícula do leitor (ou pressione Enter para cancelar): ").strip()
        if identificador == "":
            limpar_term()
            print("Operação de remoção de leitor cancelada.")
            return
        leitor = leitores_gestor.encontrar_leitor(identificador)
        if not leitor:
            print("\nLeitor não encontrado.")
            return
        emprestando = any(e.leitor == leitor for e in livros_gestor.emprestimos)
        if emprestando:
            print("\nEste leitor possui livros emprestados e não pode ser removido.")
            return
        leitores_gestor.remover_leitor(leitor)
        print(f"\nLeitor '{leitor.matricula}' removido com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao remover o leitor: {e}")
    finally:
        click_para_continuar()                                                           

#                                          _                 
#   ____  ____   ____    ____  ____   ___ | |_   ____   ____ 
#  / _  )|    \ |  _ \  / ___)/ _  ) /___)|  _) / _  | / ___)
# ( (/ / | | | || | | || |   ( (/ / |___ || |__( ( | || |    
#  \____)|_|_|_|| ||_/ |_|    \____)(___/  \___)\_||_||_|    
#               |_|                                          

# ============================
# _emprestar_livro
# ============================

def _emprestar_livro():
    try:
        print("Emprestar Livro")
        
        codigo = input("Código do livro (ou pressione Enter para cancelar): ").strip()
        if codigo == "":
            limpar_term()
            print("Operação de empréstimo de livro cancelada.")
            return
        identificador = input("Nome ou Matrícula do leitor (ou pressione Enter para cancelar): ").strip()
        if identificador == "":
            limpar_term()
            print("Operação de empréstimo de livro cancelada.")
            return
        leitor = leitores_gestor.encontrar_leitor(identificador)
        if leitor is None:
            print("\nLeitor não encontrado.")
        else:
            resultado = livros_gestor.emprestar_livro_obj(codigo, leitor)
            print(f"\n{resultado}")
    except Exception as e:
        print(f"Ocorreu um erro ao emprestar o livro: {e}")
    finally:
        click_para_continuar()

#      _                      _                     
#     | |                    | |                    
#   _ | |  ____  _   _  ___  | | _   _  ____   ____ 
#  / || | / _  )| | | |/ _ \ | || | | |/ _  ) / ___)
# ( (_| |( (/ /  \ V /| |_| || | \ V /( (/ / | |    
#  \____| \____)  \_/  \___/ |_|  \_/  \____)|_|                                                    

# ============================
# _devolver_livro
# ============================

def _devolver_livro():
    try:
        print("Devolver Livro")
        codigo = input("Código do livro (ou pressione Enter para cancelar): ").strip()
        if codigo == "":
            limpar_term()
            print("Operação de devolução de livro cancelada.")
            return
        resultado = livros_gestor.devolver_livro(codigo)
        print(f"\n{resultado}")
    except Exception as e:
        print(f"Ocorreu um erro ao devolver o livro: {e}")
    finally:
        click_para_continuar()


#                            _     
#                _          | |    
#  ____    ____ | |_   ____ | | _  
# |    \  / _  ||  _) / ___)| || \ 
# | | | |( ( | || |__( (___ | | | |
# |_|_|_| \_||_| \___)\____)|_| |_|                                

def Menu(opcao):
    match opcao:

        # ╔══════════════════════════════╗
        # ║          [1] ADICIONAR       ║
        # ╚══════════════════════════════╝
        case "1":
            while True:
                limpar_term()
                _mostrar_menu_adicionar()
                sub_opcao = input()
                limpar_term()

                # ────────────── Submenu: ADICIONAR ───────────────
                match sub_opcao:
                    # ── [1.1] Criar livro ────────────────────────
                    case "1":
                        criar_livro()

                    # ── [1.2] Cadastrar leitor ───────────────────
                    case "2":
                        _cadastrar_leitor()

                    # ── [1.3] Pesquisar e adicionar livro ────────
                    case "3":
                        pesquisar_adicionar_livro()

                    # ── [1.0] Voltar ─────────────────────────────
                    case "0":
                        break

                    # ── Inválida ─────────────────────────────────
                    case _:
                        print("Opção inválida.")
                        click_para_continuar()
            return True

        # ╔══════════════════════════════╗
        # ║            [2] VER           ║
        # ╚══════════════════════════════╝
        case "2":
            while True:
                limpar_term()
                _mostrar_menu_ver()
                sub_opcao = input()
                limpar_term()

                # ─────────────── Submenu: VER ────────────────────
                match sub_opcao:
                    # ── [2.1] Listar livros ─────────────────────
                    case "1":
                        _listar_livros()

                    # ── [2.2] Listar leitores ───────────────────
                    case "2":
                        _listar_leitores()
                        click_para_continuar()

                    # ── [2.3] Listar empréstimos ────────────────
                    case "3":
                        _listar_emprestimos()

                    # ── [2.4] Listar devoluções ─────────────────
                    case "4":
                        _listar_devolucoes()
                    case "5":
                        _listar_livros_emprestados_por_aluno()
                    # ── [2.0] Voltar ────────────────────────────
                    case "0":
                        break

                    # ── Inválida ─────────────────────────────────
                    case _:
                        print("Opção inválida.")
                        click_para_continuar()
            return True

        # ╔══════════════════════════════╗
        # ║         [3] DELETAR          ║
        # ╚══════════════════════════════╝
        case "3":
            while True:
                limpar_term()
                _mostrar_menu_deletar()
                sub_opcao = input()
                limpar_term()

                # ─────────────── Submenu: DELETAR ────────────────
                match sub_opcao:
                    # ── [3.1] Remover livro ─────────────────────
                    case "1":
                        _remover_livro()

                    # ── [3.2] Remover leitor ────────────────────
                    case "2":
                        _remover_leitor()

                    # ── [3.0] Voltar ────────────────────────────
                    case "0":
                        break

                    # ── Inválida ─────────────────────────────────
                    case _:
                        print("Opção inválida.")
                        click_para_continuar()
            return True

        # ╔══════════════════════════════╗
        # ║        [4] EMPRESTAR         ║
        # ╚══════════════════════════════╝
        case "4":
            _emprestar_livro()
            return True

        # ╔══════════════════════════════╗
        # ║         [5] DEVOLVER         ║
        # ╚══════════════════════════════╝
        case "5":
            _devolver_livro()
            return True

        # ╔══════════════════════════════╗
        # ║          [6] SALVAR          ║
        # ╚══════════════════════════════╝
        case "6":
            while True:
                limpar_term()
                _mostrar_menu_salvar()
                sub_opcao = input()
                limpar_term()

                # ─────────────── Submenu: SALVAR ────────────────
                match sub_opcao:
                    # ── [6.1] Salvar tudo ──────────────────────
                    case "1":
                        if (livros_gestor.salvar_livros_json() and leitores_gestor.salvar_leitores_json()
                            and livros_gestor.salvar_emprestimos_json() and livros_gestor.salvar_devolucoes_json()):
                            print(f"{len(livros_gestor.livros)} livros e {len(leitores_gestor.leitores)} leitores salvos.")
                            print(f"{len(livros_gestor.emprestimos)} empréstimos e {len(livros_gestor.devolucoes)} devoluções salvos.")

                    # ── [6.2] Salvar livros ─────────────────────
                    case "2":
                        if livros_gestor.salvar_livros_json():
                            print(f"{len(livros_gestor.livros)} livros salvos com sucesso.")

                    # ── [6.3] Salvar leitores ───────────────────
                    case "3":
                        if leitores_gestor.salvar_leitores_json():
                            print(f"{len(leitores_gestor.leitores)} leitores salvos com sucesso.")

                    # ── [6.4] Salvar empréstimos e devoluções ──
                    case "4":
                        if (livros_gestor.salvar_emprestimos_json() and livros_gestor.salvar_devolucoes_json()):
                            print(f"{len(livros_gestor.emprestimos)} empréstimos e {len(livros_gestor.devolucoes)} devoluções salvos.")

                    # ── [6.0] Voltar ────────────────────────────
                    case "0":
                        break

                    # ── Inválida ─────────────────────────────────
                    case _:
                        print("Opção inválida.")
                click_para_continuar()
            return True

        # ╔══════════════════════════════╗
        # ║         [7] CARREGAR         ║
        # ╚══════════════════════════════╝
        case "7":
            while True:
                limpar_term()
                _mostrar_menu_carregar()
                sub_opcao = input()
                limpar_term()

                # ─────────────── Submenu: CARREGAR ──────────────
                match sub_opcao:
                    # ── [7.1] Carregar tudo ─────────────────────
                    case "1":
                        if (livros_gestor.carregar_livros_json() and leitores_gestor.carregar_leitores_json()
                            and livros_gestor.carregar_emprestimos_json() and livros_gestor.carregar_devolucoes_json()):
                            print("Todos os dados carregados com sucesso.")

                    # ── [7.2] Carregar livros ───────────────────
                    case "2":
                        if livros_gestor.carregar_livros_json():
                            print("Livros carregados.")

                    # ── [7.3] Carregar leitores ─────────────────
                    case "3":
                        if leitores_gestor.carregar_leitores_json():
                            print("Leitores carregados.")

                    # ── [7.4] Carregar empréstimos e devoluções ─
                    case "4":
                        if (livros_gestor.carregar_emprestimos_json() and livros_gestor.carregar_devolucoes_json()):
                            print("Empréstimos e devoluções carregados.")

                    # ── [7.0] Voltar ────────────────────────────
                    case "0":
                        break

                    # ── Inválida ─────────────────────────────────
                    case _:
                        print("Opção inválida.")
                click_para_continuar()
            return True

        # ╔══════════════════════════════╗
        # ║         [0] SAIR/VOLTAR      ║
        # ╚══════════════════════════════╝
        case "0":
            return not _sair_do_loop()

        # ╔══════════════════════════════╗
        # ║       OPÇÃO INVÁLIDA         ║
        # ╚══════════════════════════════╝
        case _:
            print("Opção inválida.")
            click_para_continuar()
            return True

#               _        
#              (_)       
#   ___   ____  _   ____ 
#  /___) / _  || | / ___)
# |___ |( ( | || || |    
# (___/  \_||_||_||_|    

# ============================
# _sair_do_loop
# ============================
def _sair_do_loop():
    try:
        print("Deseja realmente sair?")
        sair = input("Digite 's' para sair ou 'n' para continuar: ")    
        if sair == "n":
            return False
        else:
            return True
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return False
#                _        
#               (_)       
#  ____    ____  _  ____  
# |    \  / _  || ||  _ \ 
# | | | |( ( | || || | | |
# |_|_|_| \_||_||_||_| |_|  

if __name__ == "__main__":
    leitores_gestor = GestorLeitor()
    livros_gestor = gestorLivros()

    leitores_gestor.carregar_leitores_json()
    livros_gestor.carregar_livros_json()
    livros_gestor.carregar_emprestimos_json()
    livros_gestor.carregar_devolucoes_json()
    continuar = True

    while(continuar):
        limpar_term()
        _mostrar_menu_inicial()
        opcao = str(input())
        limpar_term()
        continuar = Menu(opcao)
