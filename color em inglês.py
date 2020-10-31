from tkinter import *

root = Tk()

class Layout(Frame):
    def __init__(self, master):
        super().__init__()
        self.root = root
        self.root.title("Layout")

        # calculos
        self.y = self.root.winfo_screenheight()
        self.x = self.root.winfo_screenwidth()
        self.y_final = int(self.y/2) - int(720/2)
        self.x_final = int(self.x/2) - int(500/2)
        self.root.geometry(f"720x500+{self.x_final}+{self.y_final}")
        
        self.fram_configura()     
        self.root.mainloop()
        
    texto = StringVar()
    def trocar(self):
        for x in self.primeira_f.winfo_children():
            x.destroy()
        self.primeira_f["bg"] = self.texto.get()
    
    def fram_configura(self):
        self.primeira_f = Frame(self.root, bg = "red")
        self.segunda = Frame(self.root, bg = "#ccc")
        self.primeira_f.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.9)
        self.segunda.place(relx = 0, rely = 0.9, relwidth = 1, relheight = 0.1)

        self.label_1 = Label(self.segunda, text = "Cor/Color")
        self.get_valor = Entry(self.segunda, textvariable = self.texto)
        self.nota = Label(self.segunda, text = "Escreva cor a inglês ou exa-decimal", fg = "red", bg = "#ccc")
        self.executar = Button(self.segunda, text = "Executar", command = lambda: self.trocar())

        self.label_1.pack(side = LEFT)
        self.get_valor.pack(side = LEFT)
        self.nota.pack(side = RIGHT)
        self.executar.pack(side = LEFT)

Layout(root)
