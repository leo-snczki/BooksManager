import tkinter as tk
import json
from tkinter import simpledialog, messagebox, scrolledtext
from gestorLeitor import GestorLeitor
from gestorlivros import gestorLivros
from leitor import Leitor
from livro import Livro

#   _        _____  ______  ______          ______   _     _  
#  | |      (_____)(____  \(_____ \    /\  (_____ \ | |   | | 
#  | |         _    ____)  )_____) )  /  \  _____) )| |___| | 
#  | |        | |  |  __  ((_____ (  / /\ \(_____ (  \_____/  
#  | |_____  _| |_ | |__)  )     | || |__| |     | |   ___    
#  |_______)(_____)|______/      |_||______|     |_|  (___)   
# ______           ______            ______  _______  ______  
#|  ___ \    /\   |  ___ \    /\    / _____)(_______)(_____ \ 
#| | _ | |  /  \  | |   | |  /  \  | /  ___  _____    _____) )
#| || || | / /\ \ | |   | | / /\ \ | | (___)|  ___)  (_____ ( 
#| || || || |__| || |   | || |__| || \____/|| |_____       | |
#|_||_||_||______||_|   |_||______| \_____/ |_______)      |_|
#                ______  _     _  _____                       
#               / _____)| |   | |(_____)                      
#              | /  ___ | |   | |   _                         
#              | | (___)| |   | |  | |                        
#              | \____/|| |___| | _| |_                       
#               \_____/  \______|(_____)                                                                                   


class LibraryManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca")
        self.root.geometry("800x680")
        self.root.configure(bg = "#fff")
        self.root.protocol("WM_DELETE_WINDOW", self.perguntar_salvar) # Pergunta ao tentar fechar a janela.
        self.leitores_gestor=GestorLeitor()
        self.livros_gestor=gestorLivros()
        
        # Não foi colocado try except pois os métodos já estão implementados com isso.
        self.leitores_gestor.carregar_leitores_json()
        self.livros_gestor.carregar_livros_json()
        self.livros_gestor.carregar_emprestimos_json()
        self.livros_gestor.carregar_devolucoes_json()


        self.configurar_interface()

# ============================
# _configurar_interface
# ============================
    def configurar_interface(self):
        configuracao = tk.Frame(self.root,bg="#fff")
        configuracao.pack(padx=20,pady=20,fill=tk.BOTH,expand=True)
        tk.Label(configuracao,text="Gerenciador de Biblioteca",font=("Inter",36,"bold"),bg="#fff",fg="#111827").pack(pady=(0,20))
        botoes = [("Adicionar",self.menu_adicionar),
                  ("Ver",self.menu_ver),
                  ("Deletar",self.menu_deletar),
                  ("Emprestar",self.menu_emprestar),
                  ("Devolver",self.menu_devolver),
                  ("Salvar Dados",self.menu_salvar),
                  ("Carregar Dados",self.menu_carregar),
                  ("Sair",self.perguntar_salvar)]
        for texto, comando in botoes:
            tk.Button(configuracao,text=texto,font=("Poppins",14,"bold"),fg="#fff",bg="#374151",activebackground="#4B5563",
                      activeforeground="#fff",relief="flat",padx=10,pady=10,command=comando,cursor="hand2").pack(fill=tk.X,pady=(0,10))

# ============================
# __mostrar_texto_janela
# ============================
    def _mostrar_texto_janela(self,title,conteudo):
        janela = tk.Toplevel(self.root)
        janela.title(title)
        janela.geometry("650x550")
        janela.configure(bg="#fff")
        area_texto = scrolledtext.ScrolledText(janela,wrap=tk.WORD,font=("Poppins",14),bg="#F9FAFB")
        area_texto.pack(fill=tk.BOTH,expand=True,padx=20,pady=20)
        area_texto.insert(tk.END,conteudo)
        area_texto.configure(state="disabled")

# ============================
# __nova_janela
# ============================
    def _nova_janela(self,title,opcoes):
        janela = tk.Toplevel(self.root)
        janela.title(title)
        janela.geometry("640x500")
        janela.configure(bg="#fff")
        frame = tk.Frame(janela,bg="#fff")
        frame.pack(padx=24,pady=24,fill=tk.BOTH,expand=True)
        for texto,comando in opcoes:
            tk.Button(frame,text=texto,font=("Poppins",15,"bold"),fg="#fff",bg="#2563EB",activebackground="#1E40AF",
                      activeforeground="#fff",relief="flat",padx=14,pady=10,command=lambda cmd=comando,w=janela: (w.destroy(),cmd()),cursor="hand2").pack(fill=tk.X,pady=(0,14))
        tk.Button(frame,text="Voltar",font=("Poppins",15,"bold"),fg="#fff",bg="#6B7280",activebackground="#4B5563",
                  activeforeground="#fff",relief="flat",padx=14,pady=10,command=janela.destroy,cursor="hand2").pack(fill=tk.X)

# ============================
# __listar_selecao
# ============================
    def _listar_selecao(self,title, items, selecionar_botao_texto, select_callback, label_pesquisa="Pesquisar:", filtro_pesquisa=lambda items,termo:items, selecionar_fundo="#2563EB", select_fg="#fff", cancelar_fundo="#6B7280"):
        janela = tk.Toplevel(self.root)
        janela.title(title)
        janela.geometry("850x700")
        janela.configure(bg="#fff")
        container = tk.Frame(janela,bg="#fff")
        container.pack(padx=25,pady=25,fill=tk.BOTH,expand=True)

        tk.Label(container,text=title,bg="#fff",fg="#111827",font=("Poppins",22,"bold")).pack(pady=(0,20))

        frame_pesquisa = tk.Frame(container,bg="#fff")
        frame_pesquisa.pack(fill=tk.X,pady=(0,20))
        tk.Label(frame_pesquisa,text=label_pesquisa,bg="#fff",fg="#6b7280",font=("Poppins",14)).pack(side=tk.LEFT,padx=(0,12))

        variavel_pesquisa = tk.StringVar()
        entrada_pesquisa = tk.Entry(frame_pesquisa,textvariable=variavel_pesquisa,
                                     font=("Poppins",14),
                                     relief="solid",
                                     borderwidth=1,width=40)
        entrada_pesquisa.pack(side=tk.LEFT,fill=tk.X,expand=True)

        frame_lista = tk.Frame(container,bg="#fff")
        frame_lista.pack(fill=tk.BOTH,expand=True)
        lista_itens = tk.Listbox(frame_lista,font=("Poppins",13),activestyle="none",selectbackground="#60A5FA",
                      highlightthickness=1,
                      highlightbackground="#D1D5DB",bd=0)
        lista_itens.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        barra_rolagem = tk.Scrollbar(frame_lista,orient=tk.VERTICAL,command=lista_itens.yview)
        barra_rolagem.pack(side=tk.RIGHT,fill=tk.Y)
        lista_itens.config(yscrollcommand=barra_rolagem.set)

        filtered=items.copy()

# ============================
# _atualizar_lista
# ============================
        def atualizar_lista(lst):
            lista_itens.delete(0,tk.END)
            for e in lst:
                lista_itens.insert(tk.END,e)

# ============================
# _mudanca_na_pesquisa
# ============================
        def mudanca_na_pesquisa(*a):
            termo=variavel_pesquisa.get().strip().lower()
            atualizar_lista(filtro_pesquisa(items,termo))
        variavel_pesquisa.trace_add("write",mudanca_na_pesquisa)

        atualizar_lista(items)

        botaoframe = tk.Frame(container,bg="#fff")
        botaoframe.pack(pady=18,fill=tk.X)

# ============================
# _na_selecao
# ============================
        def na_selecao():
            selecao = lista_itens.curselection()
            if not selecao:
                messagebox.showwarning("Seleção","Selecione um item.")
                return
            try:
                select_callback(lista_itens.get(selecao[0]))
                janela.destroy()
            except Exception as e:
                messagebox.showerror("Erro",str(e))

        tk.Button(botaoframe,text=selecionar_botao_texto,command=na_selecao,fg=select_fg,bg=selecionar_fundo,font=("Poppins",16,"bold"),
                  relief="flat",padx=20,pady=10,cursor="hand2").pack(side=tk.LEFT,expand=True,fill=tk.X,padx=(0,15))
        tk.Button(botaoframe,text="Cancelar",command=janela.destroy,fg="#fff",bg=cancelar_fundo,font=("Poppins",16,"bold"),
                  relief="flat",padx=20,pady=10,cursor="hand2").pack(side=tk.LEFT,expand=True,fill=tk.X)

# ============================
# _menu_adicionar
# ============================
    def menu_adicionar(self):
        self._nova_janela("Adicionar",[
            ("Adicionar Livro",self.criar_livro),
            ("Cadastrar Leitor",self.cadastrar_leitor),
            ("Pesquisar e Adicionar Livro",self.pesquisar_adicionar_livro),
        ])

# ============================
# _menu_ver
# ============================
    def menu_ver(self):
        self._nova_janela("Ver",[
            ("Ver Livros",self.listar_livros),
            ("Ver Leitores",self.listar_leitores),
            ("Ver Empréstimos",self.listar_emprestimos),
            ("Ver Últimas Devoluções",self.listar_devolucoes),
            ("Ver Livros Emprestados por Aluno", self.menu_emprestimos_por_aluno),
        ])

# ============================
# _menu_deletar
# ============================
    def menu_deletar(self):
        self._nova_janela("Deletar",[
            ("Remover Livro",self.menu_remover_livro),
            ("Remover Leitor",self.menu_remover_leitor),
        ])

# ============================
# _menu_salvar
# ============================
    def menu_salvar(self):
        self._nova_janela("Salvar Dados",[
            ("Salvar Todos os Dados",self.salvar_todos_dados),
            ("Salvar Livros",self.salvar_livros),
            ("Salvar Leitores",self.salvar_leitores),
            ("Salvar Empréstimos e Devoluções",self.salvar_emprestimos_devolucoes),
        ])

# ============================
# _menu_carregar
# ============================
    def menu_carregar(self):
        self._nova_janela("Carregar Dados",[
            ("Carregar Todos os Dados",self.carregar_todos_dados),
            ("Carregar Livros",self.carregar_livros),
            ("Carregar Leitores",self.carregar_leitores),
            ("Carregar Empréstimos e Devoluções",self.carregar_emprestimos_devolucoes),
        ])

# ============================
# _criar_livro
# ============================
    def criar_livro(self):
        titulo = simpledialog.askstring("Adicionar Livro","Título:",parent=self.root)
        if not titulo: 
            return
        autor = simpledialog.askstring("Adicionar Livro","Autor:",parent=self.root)
        if not autor: 
            return
        codigo = simpledialog.askstring("Adicionar Livro","Código:",parent=self.root)
        if not codigo: 
            return
        try:
            self.livros_gestor.adicionar_livro(Livro(titulo,autor,codigo))
            messagebox.showinfo("Sucesso",f'Livro "{titulo}" adicionado com sucesso!')
        except Exception as e:
            messagebox.showerror("Erro",f"Erro ao adicionar livro: {e}")

# ============================
# _cadastrar_leitor
# ============================
    def cadastrar_leitor(self):
        nome = simpledialog.askstring("Cadastrar Leitor","Nome:",parent=self.root)
        if not nome: 
            return
        matricula = simpledialog.askstring("Cadastrar Leitor","Matrícula:",parent=self.root)
        if not matricula: 
            return
        try:
            self.leitores_gestor.adicionar_leitor(Leitor(nome,matricula))
            messagebox.showinfo("Sucesso",f'Leitor "{nome}" cadastrado com sucesso!')
        except Exception as e:
            messagebox.showerror("Erro",f"Erro ao cadastrar leitor: {e}")

# ============================
# _pesquisar_adicionar_livro
# ============================
    def pesquisar_adicionar_livro(self):
        termo = simpledialog.askstring("Pesquisar Livro","Título, autor ou palavra-chave:",parent=self.root)
        if not termo: 
            return
        try:
            resultados=self.livros_gestor.pesquisar_livros_openlibrary(termo)
            if not resultados:
                messagebox.showinfo("Resultados","Nenhum livro encontrado.")
                return
        except Exception as e:
            messagebox.showerror("Erro",f"Erro ao pesquisar livros: {e}")
            return
        itens=[f"[{codigo}] {titulo} - {autor}" for codigo, titulo, autor in resultados]

# ============================
# _adicionar
# ============================
        def adicionar(sel):
            idx=itens.index(sel)
            codigo=resultados[idx][0]
            self.livros_gestor.adicionar_livro_por_codigo(codigo,resultados)
            messagebox.showinfo("Sucesso","Livro adicionado com sucesso!")
        self._listar_selecao("Resultados da Pesquisa",itens,
                                   "Adicionar Livro Selecionado",adicionar,
                                   label_pesquisa="Pesquisar livros:")

# ============================
# _menu_emprestar
# ============================
    def menu_emprestar(self):
        livros=[l for l in self.livros_gestor.listar_livros() if l.disponivel]
        itens=[f"[{l.codigo}] {l.titulo} - {l.autor}" for l in livros]

# ============================
# _filtrar
# ============================
        def filtrar(itens,termo):
            if not termo: return itens
            termo=termo.lower()
            return [it for it in itens if termo in it.lower()]
        
# ============================
# _emprestar
# ============================
        def emprestar(selecionado):
            codigo=selecionado.split("]")[0][1:]
            leitor_id=simpledialog.askstring("Emprestar","Nome ou Matrícula do leitor:",parent=self.root)
            if not leitor_id: raise Exception("Leitor não informado.")
            leitor=self.leitores_gestor.encontrar_leitor(leitor_id)
            if not leitor: raise Exception("Leitor não encontrado.")
            resultado=self.livros_gestor.emprestar_livro_obj(codigo,leitor)
            messagebox.showinfo("Empréstimo",resultado)
        self._listar_selecao("Emprestar Livro",itens,"Emprestar Livro Selecionado",emprestar,
                                   label_pesquisa="Pesquisar livros:",
                                   filtro_pesquisa=filtrar,
                                   selecionar_fundo="#2563EB")

# ============================
# _menu_remover_livro
# ============================
    def menu_remover_livro(self):
        livros=[
            l for l in self.livros_gestor.listar_livros()
            if not any(e.livro.codigo==l.codigo for e in self.livros_gestor.emprestimos)
        ]
        itens = [f"[{l.codigo}] {l.titulo} - {l.autor}" for l in livros]

# ============================
# _filtrar
# ============================
        def filtrar(itens,termo):
            if not termo: return itens
            termo = termo.lower()
            return [it for it in itens if termo in it.lower()]
        
# ============================
# _remover
# ============================
        def remover(selecionado):
            codigo=selecionado.split("]")[0][1:]
            livro=next((l for l in self.livros_gestor.livros if l.codigo==codigo),None)
            if not livro: raise Exception("Livro não encontrado.")
            if any(e.livro.codigo==codigo for e in self.livros_gestor.emprestimos): raise Exception("Livro emprestado e não pode ser removido.")
            self.livros_gestor.remover_livro(livro)
            messagebox.showinfo("Sucesso",f'Livro "{livro.titulo}" removido com sucesso.')
        self._listar_selecao("Remover Livro",itens,"Remover Livro Selecionado",remover,
                                   label_pesquisa="Pesquisar livros:",
                                   filtro_pesquisa=filtrar,
                                   selecionar_fundo="#EF4444")

# ============================
# _menu_remover_leitor
# ============================
    def menu_remover_leitor(self):
        leitores = [
            l for l in self.leitores_gestor.listar_leitores()
            if not any(e.leitor==l for e in self.livros_gestor.emprestimos)
        ]
        itens=[f"{l.matricula}: {l.nome}" for l in leitores]

# ============================
# _filtrar
# ============================
        def filtrar(itens,termo):
            if not termo: return itens
            termo=termo.lower()
            return [it for it in itens if termo in it.lower()]
        
# ============================
# _remover
# ============================
        def remover(selecionado):
            matricula=selecionado.split(":")[0].strip()
            leitor = self.leitores_gestor.encontrar_leitor(matricula)
            if not leitor: raise Exception("Leitor não encontrado.")
            if any(e.leitor == leitor for e in self.livros_gestor.emprestimos): raise Exception("Leitor possui empréstimos e não pode ser removido.")
            self.leitores_gestor.remover_leitor(leitor)
            messagebox.showinfo("Sucesso",f'Leitor "{leitor.nome}" removido com sucesso.')
        self._listar_selecao("Remover Leitor",itens,"Remover Leitor Selecionado",remover,
                                   label_pesquisa="Pesquisar leitores:",
                                   filtro_pesquisa=filtrar,
                                   selecionar_fundo="#EF4444")

# ============================
# _menu_devolver
# ============================
    def menu_devolver(self):
        emprestimos = self.livros_gestor.listar_emprestimos()
        if not emprestimos:
            messagebox.showinfo("Devolver", "Nenhum livro está emprestado.")
            return
        itens=[f"[{e.livro.codigo}] {e.livro.titulo} - {e.livro.autor} | Emprestado a: {e.leitor.nome} ({e.leitor.matricula})" for e in emprestimos]
        
# ============================
# _filtrar
# ============================
        def filtrar(itens,termo):
            if not termo: return itens
            termo = termo.lower()
            return [item for item in itens if termo in item.lower()]
        
# ============================
# _devolver
# ============================
        def devolver(selecionado):
            codigo = selecionado.split("]")[0][1:]
            resultado = self.livros_gestor.devolver_livro(codigo)
            messagebox.showinfo("Devolver Livro",resultado)
        self._listar_selecao("Devolver Livro",itens,"Devolver Livro Selecionado",devolver,
                                   label_pesquisa="Pesquisar livros emprestados:",
                                   filtro_pesquisa=filtrar,
                                   selecionar_fundo="#10B981")

# ============================
# _listar_livros
# ============================
    def listar_livros(self):
        livros = self.livros_gestor.listar_livros()
        if not livros:
            messagebox.showinfo("Livros","Nenhum livro cadastrado.")
            return
        txt = "\n".join(f"{l.codigo}: {l.titulo} - {l.autor} ({'Disponível' if l.disponivel else 'Emprestado'})" for l in livros)
        self._mostrar_texto_janela("Lista de Livros",txt)

# ============================
# _listar_leitores
# ============================
    def listar_leitores(self):
        leitores = self.leitores_gestor.listar_leitores()
        if not leitores:
            messagebox.showinfo("Leitores","Nenhum leitor cadastrado.")
            return
        txt="\n".join(f"{l.matricula}: {l.nome}" for l in leitores)
        self._mostrar_texto_janela("Lista de Leitores",txt)

# ============================
# _listar_emprestimos
# ============================
    def listar_emprestimos(self):
        emprestimos = self.livros_gestor.listar_emprestimos()
        if not emprestimos:
            messagebox.showinfo("Empréstimos","Nenhum empréstimo em curso.")
            return
        txt="\n".join(f"{e.leitor.matricula} - {e.livro.titulo}:{e.livro.codigo} - data para devolver: {e.data_para_devolucao}" for e in emprestimos)
        self._mostrar_texto_janela("Lista de Empréstimos",txt)

# ============================
# _listar_devolucoes
# ============================
    def listar_devolucoes(self):
        devolucoes = self.livros_gestor.devolucoes
        if not devolucoes:
            messagebox.showinfo("Devoluções","Nenhuma devolução registrada.")
            return
        txt="Lista de Devoluções:\n" + "\n".join(
            f'- "{d.livro.titulo}" por {d.livro.autor}, devolvido por {d.leitor.matricula}:{d.leitor.nome} em {(d.data_devolvida or "Data desconhecida")}'
            for d in devolucoes
        )
        self._mostrar_texto_janela("Lista de Devoluções",txt)

# ============================
# _menu_emprestimos_por_aluno
# ============================
    def menu_emprestimos_por_aluno(self):   
        identificador = simpledialog.askstring("Livros emprestados", "Informe o nome ou matrícula do leitor:", parent=self.root)
        if not identificador:
            return
        leitor = self.leitores_gestor.encontrar_leitor(identificador)
        if not leitor:
            messagebox.showinfo("Livros emprestados", "Leitor não encontrado.")
            return
        emprestimos = self.livros_gestor.listar_emprestimos_por_leitor(leitor)
        if not emprestimos:
            messagebox.showinfo("Livros emprestados", f"O leitor {leitor.nome} não possui livros emprestados.")
            return
        texto = f"Livros emprestados por {leitor.nome}:\n\n"
        for emp in emprestimos:
            texto += f"- {emp.livro.titulo} (Código: {emp.livro.codigo}) - Data para devolução: {emp.data_para_devolucao}\n"
        self._mostrar_texto_janela(f"Livros emprestados por {leitor.nome}", texto)
        
# ============================
# _devolver_livro
# ============================
    def devolver_livro(self):
        codigo = simpledialog.askstring("Devolver Livro","Digite o código do livro:",parent=self.root)
        if not codigo: return
        try:
            resultado = self.livros_gestor.devolver_livro(codigo)
            messagebox.showinfo("Devolver Livro",resultado)
        except Exception as e:
            messagebox.showerror("Devolver Livro",f"Erro ao devolver livro: {e}")

# ============================
# _salvar_todos_dados
# ============================
    def salvar_todos_dados(self):
        try:
            salvar_livros = self.livros_gestor.salvar_livros_json()
            salvar_leitores = self.leitores_gestor.salvar_leitores_json()
            salvar_emprestimos = self.livros_gestor.salvar_emprestimos_json()
            salvar_devolucoes = self.livros_gestor.salvar_devolucoes_json()
            if salvar_livros and salvar_leitores and salvar_emprestimos and salvar_devolucoes:
                messagebox.showinfo("Salvar","Dados salvos com sucesso.")
            else:
                messagebox.showwarning("Salvar","Falha ao salvar algum dos dados.")
        except Exception as e:
            messagebox.showerror("Salvar",f"Erro ao salvar dados: {e}")

# ============================
# _salvar_livros
# ============================
    def salvar_livros(self):
        try:
            salvar_livros = self.livros_gestor.salvar_livros_json()
            if salvar_livros:
                messagebox.showinfo("Salvar","Livros salvos com sucesso.")
            else:
                messagebox.showwarning("Salvar","Falha ao salvar livros.")
        except Exception as e:
            messagebox.showerror("Salvar",f"Erro ao salvar livros: {e}")

# ============================
# _salvar_leitores
# ============================
    def salvar_leitores(self):
        try:
            salvar_leitores = self.leitores_gestor.salvar_leitores_json()
            if salvar_leitores:
                messagebox.showinfo("Salvar","Leitores salvos com sucesso.")
            else:
                messagebox.showwarning("Salvar","Falha ao salvar leitores.")
        except Exception as e:
            messagebox.showerror("Salvar",f"Erro ao salvar leitores: {e}")

# ============================
# _salvar_emprestimos_devolucoes
# ============================
    def salvar_emprestimos_devolucoes(self):
        try:
            salvar_emprestimos = self.livros_gestor.salvar_emprestimos_json()
            salvar_devolucoes = self.livros_gestor.salvar_devolucoes_json()
            if salvar_emprestimos and salvar_devolucoes:
                messagebox.showinfo("Salvar","Empréstimos e devoluções salvos com sucesso.")
            else:
                messagebox.showwarning("Salvar","Falha ao salvar empréstimos ou devoluções.")
        except Exception as e:
            messagebox.showerror("Salvar",f"Erro ao salvar empréstimos/devoluções: {e}")

# ============================
# _perguntar_salvar
# ============================
    def perguntar_salvar(self):
            resposta = messagebox.askyesnocancel("Salvar Dados", "Deseja salvar os dados antes de sair?")
            if resposta is True: 
                self.salvar_todos_dados()
                self.root.quit()
            elif resposta is False: 
                self.root.quit()

# ============================
# _carregar_todos_dados
# ============================
    def carregar_todos_dados(self):
        try:
            carregar_livros = self.livros_gestor.carregar_livros_json()
            carregar_leitores = self.leitores_gestor.carregar_leitores_json()
            carregar_emprestimos = self.livros_gestor.carregar_emprestimos_json()
            carregar_devolucoes = self.livros_gestor.carregar_devolucoes_json()
            if carregar_livros and carregar_leitores and carregar_emprestimos and carregar_devolucoes:
                messagebox.showinfo("Carregar","Dados carregados com sucesso.")
            else:
                messagebox.showwarning("Carregar","Falha ao carregar algum dos dados.")
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo de leitores.")
        except Exception as e:
            messagebox.showerror("Carregar",f"Erro ao carregar dados: {e}")

# ============================
# _carregar_livros
# ============================
    def carregar_livros(self):
        try:
            carregar_livro = self.livros_gestor.carregar_livros_json()
            if carregar_livro:
                messagebox.showinfo("Carregar","Livros carregados com sucesso.")
            else:
                messagebox.showwarning("Carregar","Falha ao carregar livros.")
        except Exception as e:
            messagebox.showerror("Carregar",f"Erro ao carregar livros: {e}")

# ============================
# _carregar_leitores
# ============================
    def carregar_leitores(self):
        try:
            carregar_leitor = self.leitores_gestor.carregar_leitores_json()
            if carregar_leitor:
                messagebox.showinfo("Carregar","Leitores carregados com sucesso.")
            else:
                messagebox.showwarning("Carregar","Falha ao carregar leitores.")
        except Exception as e:
            messagebox.showerror("Carregar",f"Erro ao carregar leitores: {e}")

# ============================
# _carregar_emprestimos_devolucoes
# ============================
    def carregar_emprestimos_devolucoes(self):
        try:
            carregar_emprestimo = self.livros_gestor.carregar_emprestimos_json()
            carregar_livro = self.livros_gestor.carregar_devolucoes_json()
            if carregar_emprestimo and carregar_livro:
                messagebox.showinfo("Carregar","Empréstimos e devoluções carregados com sucesso.")
            else:
                messagebox.showwarning("Carregar","Falha ao carregar empréstimos ou devoluções.")
        except Exception as e:
            messagebox.showerror("Carregar",f"Erro ao carregar empréstimos/devoluções: {e}")

#                _        
#               (_)       
#  ____    ____  _  ____  
# |    \  / _  || ||  _ \ 
# | | | |( ( | || || | | |
# |_|_|_| \_||_||_||_| |_|  

if __name__ == "__main__":
    root=tk.Tk()
    app=LibraryManagerGUI(root)
    root.mainloop()

