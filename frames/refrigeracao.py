import tkinter as tk

temRefrigeracao = None

def eh_bem_refrigerado():
    return temRefrigeracao.get()

def inicializa_frame(janela):
    global temRefrigeracao

    frameRefrigeracao = tk.Frame(janela)
    frameRefrigeracao.grid(row=3, column=0, sticky="w", pady=10)

    labelRefrigeracao = tk.Label(frameRefrigeracao, text="Você possui um bom sistema de refrigeração?", font=("Arial", 11, "bold"))
    labelRefrigeracao.grid(row=0, column=0)

    temRefrigeracao = tk.StringVar(value="Não")
    radioSimRefrigeracao = tk.Radiobutton(frameRefrigeracao, text="Sim", variable=temRefrigeracao, value="Sim")
    radioSimRefrigeracao.grid(row=1, column=0)

    radioNaoRefrigeracao = tk.Radiobutton(frameRefrigeracao, text="Não", variable=temRefrigeracao, value="Não")
    radioNaoRefrigeracao.grid(row=1, column=1)