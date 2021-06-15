'''
** Feito por:
Gabriel Lima da Silva - 202002690208
        e
Walles 

'''

import datetime
from tkinter.constants import DISABLED, END
from incidentes import Incidentes

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


class IncidentesView:

    def __init__(self, win):
        self.IncidenteCRUD = Incidentes()

        self.chamadoLabel = tk.Label(win, text='N° Chamado')
        self.usuarioLabel = tk.Label(win, text='Usuário:')
        self.produtoLabel = tk.Label(win, text='Produto:')
        self.descricaoLabel = tk.Label(win, text='Descrição\n do \n problema:')
        self.statusLabel = tk.Label(win, text="Situação: ")
        self.solucaoLabel = tk.Label(win, text="Solução \n do \n problema: ", state=DISABLED)
        self.chamadoEdit = tk.Entry(width=30, bd=3)
        self.descricaoEdit = tk.Text(width=50, bd=3, )
        self.solucaoEdit = tk.Text(width=50, bd=3, state=DISABLED)
        self.selecionarCliente = ttk.Combobox(win, width=45) 
        self.selecionarProduto = ttk.Combobox(win, width=45)
        self.selecaoTTK = 0
        self.dictClientes = {}
        self.dictProdutos = {}
        self.OpcoesNaoDuplica = 1
        self.var = StringVar()

        self.btnLimpar = tk.Button(win, text='Limpar', width=8, command=self.fLimparTelaButton) 
        self.btnCadastrar = tk.Button(
            win, text='Cadastrar', width=8, command=self._on_cadastrar_clicked)
        self.btnPesquisar = tk.Button(
            win, text='Pesquisar', width=10, command=self._on_pesquisar_id)
        self.btnAlterar = tk.Button(
            win, text='Alterar', width=8, command=self._on_atualizar_clicked)
        self.btnExcluir = tk.Button(
            win, text='Excluir', width=8, command=self._on_deletar_clicked)
        self.statusRBAberto = tk.Radiobutton(
            win, text="Aberto", value="Aberto", variable=self.var)  # variable=tk.IntVar())
        self.statusRBFechado = tk.Radiobutton(
            win, text="Fechado", value="Fechado", variable=self.var, state=DISABLED)  # variable=tk.IntVar())

        self.IncidenteList = ttk.Treeview(
            win,
            columns=(1, 2, 3, 4, 5, 6),
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
        self.IncidenteList.heading(6, text="Descrição Solução")
        self.IncidenteList['displaycolumns'] = (1, 2, 3, 4)

        self.IncidenteList.column(1, minwidth=0, width=150)
        self.IncidenteList.column(2, minwidth=0, width=172)
        self.IncidenteList.column(3, minwidth=0, width=160)
        self.IncidenteList.column(4, minwidth=0, width=150)
        self.IncidenteList.column(5, minwidth=0, width=150)
        self.IncidenteList.column(6, minwidth=0, width=150)

        self.IncidenteList.pack()
        self.IncidenteList.bind("<<TreeviewSelect>>",
                                self._on_mostrar_clicked)

        self.chamadoLabel.place(x=10, y=10)
        self.usuarioLabel.place(x=10, y=180)
        self.produtoLabel.place(x=10, y=225)
        self.descricaoLabel.place(x=10, y=316)
        self.solucaoLabel.place(x=10, y=414)
        self.statusLabel.place(x=10, y=270)
        self.statusRBAberto.place(x=70, y=270)
        self.statusRBFechado.place(x=135, y=270)
        self.chamadoEdit.place(x=100, y=10)
        self.solucaoEdit.place(x=90, y=410, height=70)
        self.descricaoEdit.place(x=90, y=310, height=80)
        self.IncidenteList.place(x=10, y=50, height=110)
        self.verscrlbar.place(x=645, y=50, height=110)
        self.selecionarCliente.place(x=70, y=180, height=24)
        self.selecionarProduto.place(x=70, y=224, height=24)
        self.btnPesquisar.place(x=300, y=9)
        self.btnCadastrar.place(x=550, y=200)
        self.btnAlterar.place(x=550, y=250)
        self.btnExcluir.place(x=550, y=300)
        self.btnLimpar.place(x=550, y=350)

        self.carregar_dados_iniciais_treeView()


    def _on_mostrar_clicked(self, event):
        selection = self.IncidenteList.selection()
        item = self.IncidenteList.item(selection)
        self._on_mostrar_opcoes(1)
        descricaoProtudo = item["values"][4]
        descricaoSolucao = item["values"][5]
        situacao = item["values"][3]
        if situacao == 'Aberto':
            self.statusRBAberto.select()
        else:
            self.statusRBFechado.select()
        self.descricaoEdit.delete("1.0", tk.END)
        self.solucaoEdit.delete("1.0", tk.END)
        self.descricaoEdit.insert("1.0", descricaoProtudo)
        if descricaoSolucao == 'None':
            descricaoSolucao = ''
        self.solucaoEdit.insert("1.0", descricaoSolucao)    


    def carregar_dados_iniciais_treeView(self):
        insidentes = self.IncidenteCRUD.consultarListaCompleta()

        count = 0

        for item in insidentes:
            chamado = item[0]
            solicitante = item[3]
            dtAbertura = item[4]
            status = item[5]
            descricao = item[6]
            solucao = item[7]
            self.IncidenteList.insert('', 'end', iid=count, values=(
                chamado, solicitante, dtAbertura, status, descricao, solucao))
            count += 1
        self.statusRBAberto.select()
        if self.OpcoesNaoDuplica == 1:
            self._on_mostrar_opcoes()
            self.OpcoesNaoDuplica = 2


    def fLimparTelaButton(self):
        self.solucaoEdit.delete('1.0', END)
        self._on_mostrar_opcoes(2)
        self.selecionarCliente.delete(0, tk.END)
        self.selecionarProduto.delete(0, tk.END)
        self.descricaoEdit.delete('1.0', tk.END)
        self.chamadoEdit.delete(0, tk.END)
        self.statusRBAberto.select()
        self.IncidenteList.delete(*self.IncidenteList.get_children())
        self.carregar_dados_iniciais_treeView()
        
    
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
            self.fLimparTelaButton()
        else:
            mb.showinfo(
                "Mensagem", "Por favor preencha todos os campos e tente novamente.")
        self.IncidenteList.insert('', 'end', iid=id+1, values=(
            id+1, self.selecionarCliente.get(), str(dataAbertura.strftime("%d/%m/%Y")), 'Aberto'))
        self.selecionarCliente.set('')
        self.selecionarProduto.set('')
        self.descricaoEdit.delete("1.0", tk.END)
        


    def _on_atualizar_clicked(self):
         linhaSelecionada = self.IncidenteList.selection()
         if len(linhaSelecionada) != 0:
            descricaoIncidente = self.descricaoEdit.get("1.0", END)
            descricaoResolucao = str(self.solucaoEdit.get("1.0", END))
            selecao = self.IncidenteList.focus()[0]
            item = self.IncidenteList.item(selecao, 'values')
            id = item[0]
            radiobutton = self.var.get()

            if self.IncidenteCRUD.atualizar(id, descricaoIncidente, descricaoResolucao, radiobutton):
                self.IncidenteList.item(
                    self.IncidenteList.focus(), values=(str(id), descricaoIncidente, descricaoResolucao, radiobutton))

                mb.showinfo("Mensagem", "Alteração executada com sucesso.")
                self.fLimparTelaButton()
                
            else:
                mb.showinfo("Mensagem", "Erro na alteração.")

    def _on_deletar_clicked(self):
         linhaSelecionada = self.IncidenteList.selection()

         if len(linhaSelecionada) != 0:
             id_dept = self.IncidenteList.item(
                 linhaSelecionada[0])["values"][0]

             if self.IncidenteCRUD.excluir(id_dept):
                 self.IncidenteList.delete(linhaSelecionada)

                 mb.showinfo("Mensagem", "Exclusão executada com sucesso.")
                 self.nomeEdit.delete(0, tk.END)
             else:
                 mb.showinfo("Mensagem", "Erro na exclusão.")
                 self.nomeEdit.focus_set()
             self.fLimparTelaButton()

    def _on_pesquisar_id(self):
        selecao = True if self.chamadoEdit.get() == '' else False
        if selecao:
            mb.showinfo("Mensagem", "Digite o código do incidente para a pesquisa.")
            return 
        idCliente = self.chamadoEdit.get()
        if self.btnPesquisar['text'] == 'Pesquisar':
            insidentes = self.IncidenteCRUD.consultarListaCompleta(idCliente)

        self.IncidenteList.delete(*self.IncidenteList.get_children())

        count = 0
        for item in insidentes:
            chamado = item[0]
            solicitante = item[3]
            dtAbertura = item[4]
            status = item[5]
            descricao = item[6]
            solucao = item[7]
            self.IncidenteList.insert('', 'end', iid=count, values=(
                chamado, solicitante, dtAbertura, status, descricao, solucao))
            count += 1

    def _on_mostrar_opcoes(self, lista=0):
        if lista == 1:
            self.selecionarCliente.set('')
            self.selecionarProduto.set('')
            self.selecionarCliente['state'] = 'disable'
            self.selecionarProduto['state'] = 'disable'
            self.solucaoLabel['state'] = 'normal'
            self.solucaoEdit['state'] = 'normal'
            self.statusRBFechado['state'] = 'normal'
            return
        elif lista == 2:
            self.selecionarCliente['state'] = 'normal'
            self.selecionarProduto['state'] = 'normal'
            self.solucaoLabel['state'] = 'disable'
            self.solucaoEdit['state'] = 'disable'
            self.statusRBFechado['state'] = 'disable'

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
            
'''janela = tk.Tk()
principal = IncidentesView(janela)
janela.title('Cadastro de Chamados Técnicos')
janela.geometry("690x510+0+0")
janela.resizable(False, False)
janela.mainloop()'''
