import tkinter as tk # Imports the tkinter library, which is used for creating graphical user interfaces.
from Backend import Backend # Imports the 'Backend' class from a module named 'Backend.py'.

class Gui: # Defines a class named 'Gui' to represent the graphical user interface.
    def __init__(self, master): # Defines the constructor method for the Gui class, taking 'master' (the root window) as an argument.
        self.master = master # Assigns the master (root window) to an instance variable.
        self.master.title("Cadastro de Nomes") # Sets the title of the main window.
        self.master.geometry("600x350") # Sets the initial size of the main window to 600 pixels wide by 350 pixels high.

        self.label = tk.Label(master, text="Digite seu nome:") # Creates a Label widget with the specified text.
        self.label.pack(pady=5) # Places the label in the window and adds 5 pixels of vertical padding.

        self.entry = tk.Entry(master) # Creates an Entry widget (a text input field).
        self.entry.pack(pady=5) # Places the entry field in the window and adds 5 pixels of vertical padding.

        self.botao = tk.Button(master, text="Salvar", command=self.salvar_nome) # Creates a Button widget with the text "Salvar" and links it to the 'salvar_nome' method.
        self.botao.pack(pady=10) # Places the button in the window and adds 10 pixels of vertical padding.

        self.mensagem = tk.Label(master, text="", fg="green") # Creates a Label widget to display messages, initially empty and with green text.
        self.mensagem.pack() # Places the message label in the window.

    def salvar_nome(self): # Defines the 'salvar_nome' method, which is called when the "Salvar" button is clicked.
        nome = self.entry.get() # Retrieves the text entered in the entry field.
        if nome.strip(): # Checks if the entered name, after removing leading/trailing whitespace, is not empty.
            Backend.salvar_nome(nome) # Calls the 'salvar_nome' method from the 'Backend' class, passing the entered name.
            self.mensagem.config(text="Nome salvo com sucesso!") # Updates the message label to indicate success.
            self.entry.delete(0, tk.END) # Clears the content of the entry field.
        else: # If the entered name is empty or only contains whitespace.
            self.mensagem.config(text="Por favor, digite um nome.", fg="red") # Updates the message label to