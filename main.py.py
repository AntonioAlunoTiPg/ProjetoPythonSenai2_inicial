import tkinter as tk
from Gui import Gui
from Backend import Backend

def main():
    Backend.initDB()
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()

if __name__ == "__main__":
    main()