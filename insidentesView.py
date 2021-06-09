import datetime
from tkinter.constants import BROWSE, CENTER, CHAR, END, INSERT, LEFT, NW
from incidentes import Incidentes

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb


class IncidentesView:

    def __init__(self, win):
        self.IncidenteCRUD = Incidentes()

        self.chamadoLabel = tk.Label(win, text='N° Chamado')
        self.usuarioLabel = tk.Label(win, text='Usuário:')
        self.produtoLabel = tk.Label(win, text='Produto:')
        self.descricaoLabel = tk.Label(win, text='Descrição:')
        self.chamadoEdit = tk.Entry(width=28, bd=3)
        self.descricaoEdit = tk.Text(width=44, bd=3, )
        self.selecionarCliente = ttk.Combobox(win, width=45)
        self.selecionarProduto = ttk.Combobox(win, width=45)
        self.selecaoTTK = 0
        self.dictClientes = {}
        self.dictProdutos = {}

        self.btnCadastrar = tk.Button(
            win, text='Cadastrar', width=7, command=self._on_cadastrar_clicked)
        self.btnPesquisar = tk.Button(
            win, text='Pesquisar', width=9, command=self._on_pesquisar_id)
        self.btnAlterar = tk.Button(
            win, text='Alterar', width=7, command=self._on_atualizar_clicked)
        self.btnExcluir = tk.Button(
            win, text='Excluir', width=7, command=self._on_deletar_clicked)

        self.IncidenteList = ttk.Treeview(
            win,
            columns=(1, 2, 3, 4, 5),
            show='headings',
            selectmode="browse",
        )
        self.verscrlbar = ttk.Scrollbar(
            win, orient="vertical", command=self.IncidenteList.yview)
        self.verscrlbar.pack(side='right', fill='x')
        self.IncidenteList.configure(yscrollcommand=self.verscrlbar.set)

        self.IncidenteList.heading(1, text="N° Chamado")
        self.IncidenteList.heading(2, text="Solicitante")
        self.IncidenteList.heading(3, text="Data de Abertura")
        self.IncidenteList.heading(4, text="Status")
        self.IncidenteList.heading(5, text="Descrição Incidente")
        self.IncidenteList['displaycolumns'] = (1, 2, 3, 4)

        self.IncidenteList.column(1, minwidth=0, width=130)
        self.IncidenteList.column(2, minwidth=0, width=162)
        self.IncidenteList.column(3, minwidth=0, width=140)
        self.IncidenteList.column(4, minwidth=0, width=130)
        self.IncidenteList.column(5, minwidth=0, width=130)

        self.IncidenteList.pack()
        self.IncidenteList.bind("<<TreeviewSelect>>",
                                self._on_mostrar_clicked)

        self.chamadoLabel.place(x=10, y=10)
        self.usuarioLabel.place(x=10, y=180)
        self.produtoLabel.place(x=10, y=225)
        self.descricaoLabel.place(x=10, y=270)
        self.chamadoEdit.place(x=100, y=10)
        self.descricaoEdit.place(x=85, y=270, height=90)
        self.IncidenteList.place(x=10, y=50, height=110)
        self.verscrlbar.place(x=573, y=50, height=110)
        self.selecionarCliente.place(x=70, y=180, height=24)
        self.selecionarProduto.place(x=70, y=224, height=24)
        self.btnPesquisar.place(x=349, y=10)
        self.btnCadastrar.place(x=480, y=190)
        self.btnAlterar.place(x=480, y=250)
        self.btnExcluir.place(x=480, y=310)

        self.carregar_dados_iniciais_treeView()

    def _on_mostrar_clicked(self, event):
        selecao = self.IncidenteList.focus()[0]
        item = self.IncidenteList.item(selecao, 'values')

        chamado = item[0]
        descricao = item[4]

        if self.selecaoTTK == chamado:
            self._on_mostrar_opcoes(2)
            self.selecaoTTK = 0
            return
        else:
            self.descricaoEdit.delete("1.0", tk.END)
            self.descricaoEdit.insert(END, descricao)

            self._on_mostrar_opcoes(1)
            self.selecaoTTK = chamado

    def carregar_dados_iniciais_treeView(self):
        insidentes = self.IncidenteCRUD.consultarListaCompleta()

        count = 0
        for item in insidentes:
            chamado = item[0]
            solicitante = item[3]
            dtAbertura = item[4]
            status = item[5]
            descricao = item[6]
            self.IncidenteList.insert('', 'end', iid=count, values=(
                chamado, solicitante, dtAbertura, status, descricao))
            count += 1

        self._on_mostrar_opcoes()

    def _on_cadastrar_clicked(self):
        selecao = True if self.selecionarCliente.get() == '' else False
        if selecao:
            mb.showinfo("Mensagem", "Registro já cadastrado.")
            return

        id = self.IncidenteCRUD.consultar_ultimo_id()
        idCliente = self.dictClientes[self.selecionarCliente.get()]
        idProduto = self.dictProdutos[self.selecionarProduto.get()]
        descricaoIncidente = str(self.descricaoEdit.get("1.0", 'end-1c'))
        dataAbertura = datetime.date.today()

        if (len(str(idCliente)) > 0 and len(str(idProduto)) > 0 and len(descricaoIncidente) > 0):
            self.IncidenteCRUD.cadastrar(
                idCliente, idProduto, descricaoIncidente, dataAbertura)
            mb.showinfo("Mensagem", "Dados inseridos com sucesso!!!")
        else:
            mb.showinfo(
                "Mensagem", "Por favor preencha todos os campos e tente novamente.")
        self.IncidenteList.insert('', 'end', iid=id+1, values=(
            id+1, self.selecionarCliente.get(), str(dataAbertura.strftime("%d/%m/%Y")), 'Aberto'))
        self.selecionarCliente.set('')
        self.selecionarProduto.set('')
        self.descricaoEdit.delete("1.0", tk.END)

    def _on_atualizar_clicked(self):
        pass
        # linhaSelecionada = self.IncidenteList.selection()
        # if len(linhaSelecionada) != 0:
        #     nome = self.nomeEdit.get()
        #     id = self.IncidenteList.item(linhaSelecionada[0])['values'][0]

        #     if self.IncidenteCRUD.atualizar(id, nome):
        #         self.IncidenteList.item(
        #             self.IncidenteList.focus(), values=(str(id), nome))

        #         mb.showinfo("Mensagem", "Alteração executada com sucesso.")
        #         self.nomeEdit.delete(0, tk.END)
        #     else:
        #         mb.showinfo("Mensagem", "Erro na alteração.")
        #         self.nomeEdit.focus_set()
        #     self.IncidenteList.selection_remove(
        #         self.IncidenteList.selection())

    def _on_deletar_clicked(self):
        pass
        # linhaSelecionada = self.IncidenteList.selection()

        # if len(linhaSelecionada) != 0:
        #     id_dept = self.IncidenteList.item(
        #         linhaSelecionada[0])["values"][0]

        #     if self.IncidenteCRUD.excluir(id_dept):
        #         self.IncidenteList.delete(linhaSelecionada)

        #         mb.showinfo("Mensagem", "Exclusão executada com sucesso.")
        #         self.nomeEdit.delete(0, tk.END)
        #     else:
        #         mb.showinfo("Mensagem", "Erro na exclusão.")
        #         self.nomeEdit.focus_set()

    def _on_pesquisar_id(self):
        idCliente = self.chamadoEdit.get()

        if self.btnPesquisar['text'] == 'Pesquisar':
            self.btnPesquisar['text'] = 'Limpar'
            insidentes = self.IncidenteCRUD.consultarListaCompleta(idCliente)
        else:
            self.btnPesquisar['text'] = 'Pesquisar'
            insidentes = self.IncidenteCRUD.consultarListaCompleta()
            self.chamadoEdit.delete(0, tk.END)

        self.IncidenteList.delete(*self.IncidenteList.get_children())

        count = 0
        for item in insidentes:
            chamado = item[0]
            solicitante = item[3]
            dtAbertura = item[4]
            status = item[5]
            descricao = item[6]
            self.IncidenteList.insert('', 'end', iid=count, values=(
                chamado, solicitante, dtAbertura, status, descricao))
            count += 1

    def _on_mostrar_opcoes(self, lista=0):
        if lista == 1:
            self.selecionarCliente.set('')
            self.selecionarProduto.set('')
            self.selecionarCliente['state'] = 'disable'
            self.selecionarProduto['state'] = 'disable'
            return
        elif lista == 2:
            self.selecionarCliente['state'] = 'normal'
            self.selecionarProduto['state'] = 'normal'
        else:
            listaClientes = self.IncidenteCRUD.consultaCliente()
            listaProdutos = self.IncidenteCRUD.consultaProduto()
            lClientes = []
            lProdutos = []

            for id, usuario in listaClientes:
                lClientes.append((usuario, id))
                self.selecionarCliente['values'] = (
                    *self.selecionarCliente['values'], usuario)
            self.dictClientes = dict(lClientes)

            # self.selecionarCliente['values'] = (*self.selecionarCliente['values'], cliente[1])

            for id, produto in listaProdutos:
                lProdutos.append((produto, id))
                self.selecionarProduto['values'] = (
                    *self.selecionarProduto['values'], produto)
            self.dictProdutos = dict(lProdutos)


janela = tk.Tk()
principal = IncidentesView(janela)
janela.title('Cadastro de Chamados Técnicos')
janela.geometry("598x410+0+0")
janela.mainloop()
