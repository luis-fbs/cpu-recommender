import tkinter as tk


entradaGastos = None

def inicializa_frame(janela):
    global entradaGastos

    frameGastos = tk.Frame(janela)
    frameGastos.grid(row=1, column=0, sticky="w", pady=10)

    labelGastos = tk.Label(frameGastos, text="Seu limite de gastos:", font=("Arial", 11, "bold"))
    labelGastos.grid(row=0, column=0)

    entradaGastos = tk.Entry(frameGastos)
    entradaGastos.grid(row=0, column=1, sticky="w", padx=5)

def maximo():
    try:
        return float(entradaGastos.get())
    except:
        return 5000.0