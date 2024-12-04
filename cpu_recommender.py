import tkinter as tk
from tkinter import scrolledtext

from frames import atividades, gastos, preferencia, refrigeracao, placaMae

from util import processarCsv, response_generator

def resposta():
    nova_janela = tk.Toplevel()  # Cria uma nova janela
    nova_janela.title("Recomendação")  # Título da nova janela
    nova_janela.geometry("400x100")

    text = scrolledtext.ScrolledText(nova_janela, width=60, height=20, font=("Arial", 12))
    text.pack()
    text.insert(tk.END,response_generator.resposta())

janela = tk.Tk()
janela.title("CPU Recommender")
janela.geometry("640x640")
janela.resizable(False, False)

atividades.inicializa_frame(janela)
gastos.inicializa_frame(janela)
preferencia.inicializa_frame(janela)
refrigeracao.inicializa_frame(janela)
placaMae.inicializa_frame(janela)

tk.Button(janela, text="submeter", command=lambda:resposta()).grid(row=5, column=0, pady=15, sticky="nsew")

janela.mainloop()