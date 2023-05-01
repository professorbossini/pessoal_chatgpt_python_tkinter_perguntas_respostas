from tkinter import *
from tkinter import ttk
janela_principal = Tk()
#padding: distância entre borda e conteúdo. Ordem: Left, Top, Right, Bottom
estilo = ttk.Style()
estilo.configure("meu_estilo", borderwidth=2, relief='solid')

frame = ttk.Frame(janela_principal, padding="12 12 12 12", style="meu_estilo")
frame.grid(column=0, row=0)
feet = StringVar()
feet_entry = ttk.Entry(frame, width=12, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))
janela_principal.mainloop()
