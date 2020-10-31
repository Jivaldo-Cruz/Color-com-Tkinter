from tkinter import *

root = Tk()

class Layout(Frame):
    def __init__(self, master):
        super().__init__()
        self.root = root
        self.root.title("San-Color")

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
        colors = {"branco": "white", "preto": "black", "rosa": "pink",
                  "verde": "green", "vermelho": "red", "amarelo": "yellow",
                  "azul": "blue", "bege": "beige", "borbô": "burgundy",
                  "caramelo": "caramel", "cáqui": "khaki", "castanho": "brown",
                  "cinza": "gray", "creme": "cream", "laranja": "orange", "lilás": "lilac",
                  "marrom": "brown", "mostarda": "mustard", "roxo": "purple", 
                  "salmão": "salmon", "violeta": "violet"}
        for x in colors:
            if(x == (self.texto.get()).lower()):
                self.primeira_f["bg"] = colors[x]
            if(self.texto.get()[0] == "#"):
                self.primeira_f["bg"] = self.texto.get()
            if(x != (self.texto.get()).lower()):
                self.nota["text"] = "Está cor não existe no programa!"
                
    def fram_configura(self):
        self.primeira_f = Frame(self.root, bg = "red")
        self.segunda = Frame(self.root, bg = "#ccc")
        self.primeira_f.place(relx = 0, relwidth = 1, relheight = 0.9)
        self.segunda.place(relx = 0, rely = 0.9, relwidth = 1, relheight = 0.1)

        self.label_1 = Label(self.segunda, text = "Cor/Color", bg = "#34abe0", fg = "#fff", font = "Arial 14")
        self.get_valor = Entry(self.segunda, textvariable = self.texto, width = 30)
        self.nota = Label(self.segunda, text = "Escreva cor a português ou exa-decimal", fg = "red", bg = "#ccc")
        self.executar = Button(self.segunda, text = "Executar", bg = "#414146", fg = "#fff", command = lambda: self.trocar())

        self.label_1.pack(side = LEFT)
        self.get_valor.pack(side = LEFT)
        self.executar.pack(side = LEFT)
        self.nota.pack(side = RIGHT)

Layout(root)
