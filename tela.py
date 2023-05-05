import tkinter as tk
from tkinter import ttk

#função para criar a primeira aba
def criar_aba1(notebook, criar_pergunta):
  tab1 = ttk.Frame(notebook)
  notebook.add(tab1, text='Gerar pergunta')

  #linha 0
  tk.Label(tab1, text='Assunto:').grid(row=0, column=0, sticky='W', padx=5, pady=5)
  assunto_entry = tk.Entry(tab1)
  assunto_entry.grid(row=0, column=1, columnspan=3, sticky='WE', padx=5, pady=5)

  #linha 1
  tk.Label(tab1, text='Tipo:').grid(row=1, column=0, sticky='W', padx=5, pady=5)
  tipo_var = tk.StringVar()
  tk.Radiobutton(tab1, text='Dissertativa', variable=tipo_var, value='Dissertativa').grid(row=1, column=1, sticky='W', padx=5, pady=5)
  tk.Radiobutton(tab1, text='Alternativa', variable=tipo_var, value='Alternativa').grid(row=1, column=2, sticky='W', padx=5, pady=5)

  #linha 2
  tk.Label(tab1, text='Dificuldade:').grid(row=2, column=0, sticky='W', padx=5, pady=5)
  dificuldade_var = tk.StringVar()
  tk.Radiobutton(tab1, text='Fácil', variable=dificuldade_var, value='Fácil').grid(row=2, column=1, sticky='W', padx=5, pady=5)
  tk.Radiobutton(tab1, text='Média', variable=dificuldade_var, value='Média').grid(row=2, column=2, sticky='W', padx=5, pady=5)
  tk.Radiobutton(tab1, text='Difícil', variable=dificuldade_var, value='Difícil').grid(row=2, column=3, sticky='W', padx=5, pady=5)

  #linha 3
  tk.Label(tab1, text='Pergunta exemplo:').grid(row=3, column=0, sticky='W', padx=5, pady=5)

  #linha 4
  pergunta_exemplo = tk.Text(tab1)
  #20 linhas de texto
  pergunta_exemplo.configure(height=20)
  pergunta_exemplo.grid(row=4, column=0, columnspan=4, sticky='WE', padx=5, pady=5)
  

  #linha 5
  tk.Label(tab1, text='Resposta:').grid(row=5, column=0, sticky='W', padx=5, pady=5)

   #linha 6
  resposta_text = tk.Text(tab1)
  #20 linhas de texto
  resposta_text.configure(height=20)
  resposta_text.grid(row=6, column=0, columnspan=4, sticky='WE', padx=5, pady=5)

  #linha 7
  def executar():
    #num Text TKinter '1.0' representa número da linha (começa do 1) e da coluna (começa do zero)
    #limpamos para casos de perguntas anteriores
    resposta_text.delete("1.0", 'end')
    print('executar')
    resposta = criar_pergunta(assunto_entry.get(), tipo_var.get(), dificuldade_var.get(), pergunta_exemplo.get('1.0', 'end'))
    resposta_text.insert("1.0", resposta)

  ok_button = tk.Button(tab1, text='OK', command=executar)
  ok_button.grid(row=7, column=0, columnspan=4, sticky='WE', padx=5, pady=5)

  #peso 1 para cada linha conforme o usuário expande
  for i in range(6):  # para 8 linhas (0-7)
    tab1.grid_rowconfigure(i, weight=1)  # expande com peso 1
  for i in range(4):  # para 4 colunas (0-3)
    tab1.grid_columnconfigure(i, weight=1)  # expande com peso 1
  return tab1



def criar_tela(criar_pergunta):
  window = tk.Tk()
  window.title('ChatGPT - Gerador/Corretor de Questões')
  window.minsize(800, 600)

  notebook = ttk.Notebook(window, padding=10)

  #cria a primeir aba
  tab1 = criar_aba1(notebook, criar_pergunta)
  notebook.pack(expand=True, fill='both')
  window.mainloop()
