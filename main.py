import tkinter as tk
from insidentesView import IncidentesView
from produtosView import produtosView

class Main():
    def __init__(self, win):
        self.lblTitulo = tk.Label(win, text="Controle de Incidentes", font='Arial 20 bold')
        self.btnUsuarios = tk.Button(win, text="Usuários", command=self._openUsuarios)
        self.btnProdutos = tk.Button(win, text="Produtos", command=self._openProdutos)
        self.btnIncidentes = tk.Button(win, text="Incidentes", command=self._openIncidentes)
        
        self.lblTitulo.place(x=270, y=30)
        self.btnUsuarios.place(x=50, y=150, width=220, height=110)
        self.btnProdutos.place(x=300, y=150, width=220, height=110)
        self.btnIncidentes.place(x=550, y=150, width=220, height=110)
        
    def _openUsuarios(self):
        pass
        
    def _openProdutos(self):
        janela=tk.Toplevel()
        principal=produtosView(janela)
        janela.title('Produtos')
        janela.geometry("800x600+0+0")
        janela.mainloop()
        
    def _openIncidentes(self):
        janela = tk.Toplevel()
        principal = IncidentesView(janela)
        janela.title('Cadastro de Chamados Técnicos')
        janela.geometry("690x510+0+0")
        janela.mainloop()
        
janela=tk.Tk()
janela.title('Main')
janela.geometry("800x400+0+0")
principal=Main(janela)
janela.mainloop()
