import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from produtos import Produtos

class produtosView:
    def __init__(self, win):
        self.produtosCRUD = Produtos()

        #Criando Elementos
        #Inserts
        self.nomeLabel = tk.Label(win, text="Nome")
        self.nomeEdit = tk.Entry(borderwidth="2")

        self.descricaoLabel = tk.Label(win, text="Descrição")
        self.descricaoEdit = tk.Text(borderwidth="2")
        
        #TreeView
        self.produtosList = ttk.Treeview(win, columns=("Cod.", "Nome", "Descrição"), show='headings', selectmode="browse")

        self.produtosList.heading("Cod.", text="Cod.")
        self.produtosList.heading("Nome", text="Nome")
        self.produtosList.heading("Descrição", text="Descrição")

        self.produtosList.column("Cod.", minwidth=0, width=50)
        self.produtosList.column("Nome", minwidth=0, width=100)
        self.produtosList.column("Descrição", minwidth=0, width=500)

        self.produtosList.pack(padx=10, pady=10)
        self.produtosList.bind("<<TreeviewSelect>>", self._on_selected_object)

        self.verscrlbar = ttk.Scrollbar(win, orient="vertical", command=self.produtosList.yview)
        self.verscrlbar.pack(side='right', fill='x')
        self.produtosList.configure(yscrollcommand=self.verscrlbar.set)

        #Criando Botões
        self.btnCadastrar = tk.Button(win, text='Cadastrar', command=self._on_cadastrar_clicked, width=8)
        self.btnAlterar = tk.Button(win, text='Alterar', command=self._on_alterar_clicked, width=8)
        self.btnExcluir = tk.Button(win, text='Excluir', command=self._on_excluir_clicked, width=8)

        #Posicionando Elementos
        self.produtosList.place(x=10, y=30, width= 750, height=300)

        self.nomeLabel.place(x= 10, y=350)
        self.nomeEdit.place(x=70, y=350, width=600)

        self.descricaoLabel.place(x=10, y=390)
        self.descricaoEdit.place(x=70, y=390, width=600, height=200)

        self.btnCadastrar.place(x=700, y=400)
        self.btnAlterar.place(x=700, y=450)
        self.btnExcluir.place(x=700, y=500)

        #Carregando Dados
        self.carregar_dados_treeview()


    def carregar_dados_treeview(self):
            resultset = self.produtosCRUD.consultar()
            self.produtosList.delete(*self.produtosList.get_children())
            cont = 0
            for registro in resultset:
                self.produtosList.insert('', 'end', iid=cont, values=(str(registro[0]), registro[1], registro[2]))
                cont += 1

    def _on_cadastrar_clicked(self):
        #Pegar os valores digitados pelo usuário
        nome = self.nomeEdit.get()
        descricao = self.descricaoEdit.get("1.0", "end").strip("\n")
        
        #Caso nome ou descriçãoo estejam vazios
        if nome == "" or descricao == "":
            mb.showinfo("Mensagem", "Nome ou descrições vazias não são permitidas")
            self.nomeEdit.focus_set()
        else:
            #Insere no banco e mostra a mensagem garantindo inserção
            if self.produtosCRUD.cadastrar(nome, descricao):
                id = self.produtosCRUD.consultarUltimoID()
                self.produtosList.insert('', 'end', iid=(id+1), values=(str(id), nome, descricao))
                self.nomeEdit.delete(0, tk.END)
                self.descricaoEdit.delete("1.0", tk.END)
                mb.showinfo("Mensagem", "Cadastro realizado com SUCESSO!")
                self.nomeEdit.focus_set()
            #Caso erro aconteça na inserção
            else:
                mb.showinfo("Mensagem", "Erro no cadastro")
                self.nomeEdit.focus_set()

    def _on_alterar_clicked(self):
        #Pegar os valores digitados pelo usuário
        linhaSelecionada = self.produtosList.selection()
        
        #Caso nome ou descriçãoo estejam vazios
        if len(linhaSelecionada) == 0:
            mb.showinfo("Mensagem", "Nome ou descrições vazias não são permitidas")
            self.nomeEdit.focus_set()
        else:
            id = self.produtosList.item(linhaSelecionada[0])['values'][0]
            nome = self.nomeEdit.get()
            descricao = self.descricaoEdit.get("1.0", "end").strip("\n")
            #Insere no banco e mostra a mensagem garantindo inserção
            if self.produtosCRUD.update(id, nome, descricao):
                self.produtosList.delete(*self.produtosList.get_children())
                self.carregar_dados_treeview()


                self.nomeEdit.delete(0, tk.END)
                self.descricaoEdit.delete("1.0", tk.END)
                mb.showinfo("Mensagem", "Produto alterado com SUCESSO!")
                self.nomeEdit.focus_set()
            #Caso erro aconteça na inserção
            else:
                mb.showinfo("Mensagem", "Erro na alteração")
                self.nomeEdit.focus_set()

    def _on_excluir_clicked(self):
        linhaSelecionada = self.produtosList.selection()

        if len(linhaSelecionada) != 0:
            id_produto = self.produtosList.item(linhaSelecionada[0])["values"][0]
            
            if self.produtosCRUD.excluir(id_produto):

                self.produtosList.delete(linhaSelecionada)
                self.nomeEdit.delete(0, tk.END)
                self.descricaoEdit.delete("1.0", tk.END)
                self.nomeEdit.focus_set()

                mb.showinfo("Mensagem", "Exclusão realizada com SUCESSO!")
            else:
                mb.showinfo("Mensagem", "Erro na exclusão")



    def _on_selected_object(self, event):
        selection = self.produtosList.selection()
        item = self.produtosList.item(selection)

        nomeProduto = item["values"][1]
        descricaoProtudo = item["values"][2]

        self.nomeEdit.delete(0, tk.END)
        self.descricaoEdit.delete("1.0", tk.END)

        self.nomeEdit.insert(0, nomeProduto)
        self.descricaoEdit.insert("1.0", descricaoProtudo)


janela = tk.Tk()
principal = produtosView(janela)
janela.title("Cadastro de Departamento")
janela.geometry("800x600+0+0")
janela.mainloop()