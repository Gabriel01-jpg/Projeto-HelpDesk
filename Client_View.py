'''
Develop by:
Luis Eduardo and Wallison
'''
from tkinter.constants import END
from client import register_Client
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

class register_Client_View:

    def __init__(self, screen):
        self.client_CRUD = register_Client()
        self.deptSelected = None

        #1
        self.lblNameClient = tk.Label(screen, text='NAME')
        self.NameClientEdit = tk.Entry(width = 35, bd=2)

        #2
        self.lblLastName = tk.Label(screen, text="LAST NAME")
        self.LastNameClientEdit = tk.Entry(width = 35, bd=2)

        #3
        self.lblCPFClient = tk.Label(screen, text="CPF")
        self.CPFClientEdit = tk.Entry(width = 35, bd=2)

        #4
        self.lblPhoneClient = tk.Label(screen, text="TELEFONE")
        self.PhoneClientEdit = tk.Entry(width = 35, bd=2)

        #5
        self.lblEmailClient = tk.Label(screen, text="EMAIL")
        self.EmailClientEdit = tk.Entry(width = 35, bd=2)

        #6
        self.lblAdressClient = tk.Label(screen, text="ADRESS")
        self.AdressClientEdit = tk.Entry(width = 35, bd=2)

        self.btnCadastrar = tk.Button(screen, text='Cadastrar', width = 10, command=self._on_cadastrar_clicked) 
        self.btnAlterar = tk.Button(screen, text='Alterar', width = 10, command=self._on_update_clicked) 
        self.btnExcluir = tk.Button(screen, text='Excluir', width = 10, command=self._on_delete_clicked)   
        
        self.clientList = ttk.Treeview(screen, columns=(1,2,3,4,5,6,7), show='headings')
        self.verscrlbar_2 = ttk.Scrollbar(screen,  orient="horizontal", command=self.clientList.xview)
        self.verscrlbar = ttk.Scrollbar(screen, orient="vertical", command=self.clientList.xview)  
        self.verscrlbar_2.pack(side = 'right', fill='x')
        self.verscrlbar.pack(side ='right', fill ='y')
        self.clientList.configure(yscrollcommand=self.verscrlbar.set)
        self.clientList.configure(xscrollcommand=self.verscrlbar_2.set)

        self.clientList.heading(1, text="ID")
        self.clientList.heading(2, text="First Name") 
        self.clientList.heading(3, text="Last Name")
        self.clientList.heading(4, text="CPF") 
        self.clientList.heading(5, text="Phone")
        self.clientList.heading(6, text="Email")
        self.clientList.heading(7, text="Adress")

        self.clientList.column(1, minwidth=0, width=40)
        self.clientList.column(2, minwidth=0, width=110)
        self.clientList.column(3, minwidth=0, width=120)
        self.clientList.column(4, minwidth=0, width=140)
        self.clientList.column(5, minwidth=0, width=140)
        self.clientList.column(6, minwidth=0, width=170)
        self.clientList.column(7, minwidth=0, width=190)

        self.clientList.pack()
        self.clientList.bind("<<TreeviewSelect>>",self._on_mostrar_clicked)
       
        #1
        self.lblNameClient.place(x=60, y=10)
        self.NameClientEdit.place(x=120, y=10)
        #2
        self.lblLastName.place(x=370, y=10)
        self.LastNameClientEdit.place(x=450, y=10)
        #3
        self.lblCPFClient.place(x=60, y=60)
        self.CPFClientEdit.place(x=120, y=60)
        #4
        self.lblPhoneClient.place(x=370, y=60)
        self.PhoneClientEdit.place(x=450, y=60)
        #5
        self.lblEmailClient.place(x=60, y=110)
        self.EmailClientEdit.place(x=120, y=110)
        #6
        self.lblAdressClient.place(x=370, y=110)
        self.AdressClientEdit.place(x=450, y=110)

        self.clientList.place(x=10, y=220, width=740)
        self.verscrlbar.place(x=750, y=220, height=230)
        self.verscrlbar_2.place(x=10, y=446,  height=20, width=740)

        self.btnCadastrar.place(x=355, y=160)
        self.btnAlterar.place(x=245, y=160)  
        self.btnExcluir.place(x=465, y=160)

        self.carregar_dados_iniciais_treeView()
        
    
 
    def _on_mostrar_clicked(self, event):
        #Seleção do Usuário, linha na qual ele clicou
        selection = self.clientList.selection()
        item = self.clientList.item(selection)
        
        lblNameClient = item["values"][1]
        lblLastName = item["values"][2]
        lblCPFClient = item["values"][3]
        lblPhoneClient = item["values"][4]
        lblEmailClient = item["values"][5]
        lblAdressClient = item["values"][6]

        self.NameClientEdit.delete(0, tk.END)
        self.NameClientEdit.insert(0, lblNameClient)
        self.LastNameClientEdit.delete(0, tk.END)
        self.LastNameClientEdit.insert(0, lblLastName)
        self.CPFClientEdit.delete(0, tk.END)
        self.CPFClientEdit.insert(0, lblCPFClient)
        self.PhoneClientEdit.delete(0, tk.END)
        self.PhoneClientEdit.insert(0, lblPhoneClient)
        self.EmailClientEdit.delete(0, tk.END)
        self.EmailClientEdit.insert(0, lblEmailClient)
        self.AdressClientEdit.delete(0, tk.END)
        self.AdressClientEdit.insert(0, lblAdressClient)



    def carregar_dados_iniciais_treeView(self):
        registros = self.client_CRUD.consult()       

        count = 0
        for item in registros:
            idCliente = item[0]
            lblNameClient = item[1]
            lblLastName = item[2]
            lblCPFClient = item[3]
            lblPhoneClient = item[4]
            lblEmailClient = item[5]
            lblAdressClient = item[6]
            self.clientList.insert('','end',iid=count,values=(str(idCliente),lblNameClient,lblLastName,lblCPFClient,lblPhoneClient,lblEmailClient,lblAdressClient ))
            count = count + 1

    def _on_cadastrar_clicked(self):

        lblNameClient = self.NameClientEdit.get()
        lblLastName = self.LastNameClientEdit.get()
        lblCPFClient = self.CPFClientEdit.get()
        lblPhoneClient = self.PhoneClientEdit.get()
        lblEmailClient = self.EmailClientEdit.get()
        lblAdressClient = self.AdressClientEdit.get()

        
        if self.client_CRUD.register(lblNameClient,lblLastName,lblCPFClient,lblPhoneClient,lblAdressClient,lblEmailClient):

            idCliente = self.client_CRUD.consult_last_id()
            numeroLinhas = len(self.clientList.get_children())
            self.clientList.insert('','end',iid=(idCliente),values=(str(idCliente + 1),lblNameClient,lblLastName,lblCPFClient,lblPhoneClient,lblEmailClient,lblAdressClient))
            
            mb.showinfo("Mensagem", "Cadastro executado com sucesso.")       
            self.NameClientEdit.delete(0, tk.END)
            self.LastNameClientEdit.delete(0, tk.END)
            self.CPFClientEdit.delete(0, tk.END)
            self.PhoneClientEdit.delete(0, tk.END)
            self.EmailClientEdit.delete(0, tk.END)
            self.AdressClientEdit.delete(0, tk.END)
            self.AdressClientEdit.focus_set()
        else:
            mb.showinfo("Mensagem", "Erro no cadastro.") 
            self.nomeEdit.focus_set()


    def _on_update_clicked(self):        
        linhaSelecionada = self.clientList.selection()

        if len(linhaSelecionada) != 0:
            idCliente = self.clientList.item(linhaSelecionada[0])['values'][0]
            lblNameClient = self.NameClientEdit.get()
            lblLastName = self.LastNameClientEdit.get()
            lblCPFClient = self.CPFClientEdit.get()
            lblPhoneClient = self.PhoneClientEdit.get()
            lblEmailClient = self.EmailClientEdit.get()
            lblAdressClient = self.AdressClientEdit.get()
            
         
            if self.client_CRUD.update(idCliente,lblNameClient,lblLastName,lblCPFClient,lblPhoneClient,lblEmailClient,lblAdressClient):

                self.clientList.item(self.clientList.focus(), values=(str(idCliente),lblNameClient,lblLastName,lblCPFClient,lblPhoneClient,lblEmailClient,lblAdressClient))

                mb.showinfo("Mensagem", "Alteração executada com sucesso.")       
                self.NameClientEdit.delete(0, tk.END)
                self.LastNameClientEdit.delete(0, tk.END)
                self.CPFClientEdit.delete(0, tk.END)
                self.PhoneClientEdit.delete(0, tk.END)
                self.EmailClientEdit.delete(0, tk.END)
                self.AdressClientEdit.delete(0, tk.END)
                self.NameClientEdit.focus_set()
                self.LastNameClientEdit.focus_set()
                self.CPFClientEdit.focus_set()
                self.PhoneClientEdit.focus_set()
                self.EmailClientEdit.focus_set()
                self.AdressClientEdit.focus_set()
            else:
                mb.showinfo("Mensagem", "Erro no alteração.") 
                self.nomeEdit.focus_set()
    



    def _on_delete_clicked(self):
        linhaSelecionada = self.clientList.selection()

        if len(linhaSelecionada) != 0:
            idCliente = self.clientList.item(linhaSelecionada[0])["values"][0]

            if self.client_CRUD.delete(idCliente):
                self.clientList.delete(linhaSelecionada)
                
                mb.showinfo("Mensagem", "Exclusão executada com sucesso.")
                self.NameClientEdit.delete(0, tk.END)
                self.LastNameClientEdit.delete(0, tk.END)
                self.CPFClientEdit.delete(0, tk.END)
                self.PhoneClientEdit.delete(0, tk.END)
                self.EmailClientEdit.delete(0, tk.END)
                self.AdressClientEdit.delete(0, tk.END)
                self.NameClientEdit.focus_set()
                self.LastNameClientEdit.focus_set()
                self.CPFClientEdit.focus_set()
                self.PhoneClientEdit.focus_set()
                self.EmailClientEdit.focus_set()
                self.AdressClientEdit.focus_set()
            else:
                mb.showinfo("Mensagem", "Erro na exclusão.")
                self.nomeEdit.focus_set()



janela=tk.Tk()
principal=register_Client_View(janela)
janela.title('Cadastro de Cliente')
janela.geometry("770x465+0+0")
janela.mainloop()
