import tkinter as tk
from Backend import Backend

class Gui:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Nomes")
        self.master.geometry("600x350")

        self.label = tk.Label(master, text="Digite seu nome:")
        self.label.pack(pady=5)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        self.botao = tk.Button(master, text="Salvar", command=self.salvar_nome)
        self.botao.pack(pady=10)

        self.mensagem = tk.Label(master, text="", fg="green")
        self.mensagem.pack()

    def salvar_nome(self):
        nome = self.entry.get()
        if nome.strip():
            Backend.salvar_nome(nome)
            self.mensagem.config(text="Nome salvo com sucesso!")
            self.entry.delete(0, tk.END)
        else:
            self.mensagem.config(text="Por favor, digite um nome.", fg="red")
            