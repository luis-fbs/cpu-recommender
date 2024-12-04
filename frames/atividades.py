import tkinter as tk
from tkinter import Checkbutton

valorJogar = None
valorVideos = None
valorProgramar = None
valorIA = None
valorDocumentos = None
valorIOT = None
valorInternet = None

def inicializa_frame(janela):
    global valorJogar, valorVideos, valorProgramar, valorIA, valorDocumentos, valorIOT, valorInternet

    frameAtividades = tk.Frame(janela)
    frameAtividades.grid(row=0, column=0, pady=5)

    labelAtivididades = tk.Label(frameAtividades, text="Você usa o computador para:",font=("Arial", 11, "bold"))
    labelAtivididades.grid(row=0, column=0)

    valorJogar = tk.BooleanVar()
    checkJogar = Checkbutton(frameAtividades, text="Jogar", variable=valorJogar)
    checkJogar.grid(row=1, column=0, sticky="w")

    valorVideos = tk.BooleanVar()
    checkVideos = Checkbutton(frameAtividades, text="Editar vídeos", variable=valorVideos)
    checkVideos.grid(row=1, column=1, sticky="w")

    valorProgramar = tk.BooleanVar()
    checkProgramar = Checkbutton(frameAtividades, text="Programar", variable=valorProgramar)
    checkProgramar.grid(row=1, column=2, sticky="w")

    valorIA = tk.BooleanVar()
    checkIA = Checkbutton(frameAtividades, text="Treinar IA", variable=valorIA)
    checkIA.grid(row=2, column=0, sticky="w")

    valorDocumentos = tk.BooleanVar()
    checkDocumentos = Checkbutton(frameAtividades, text="Editar documentos", variable=valorDocumentos)
    checkDocumentos.grid(row=2, column=1, sticky="w")

    valorIOT = tk.BooleanVar()
    checkIOT = Checkbutton(frameAtividades, text="IOT", variable=valorIOT)
    checkIOT.grid(row=2, column=2, sticky="w")

    valorInternet = tk.BooleanVar()
    checkInternet = Checkbutton(frameAtividades, text="Navegar na internet", variable=valorInternet)
    checkInternet.grid(row=3, column=0, sticky="w")

def get_classificacao_uso():
    if valorJogar.get() or valorVideos.get() or valorIA.get():
        return "Intenso"
    else:
        if valorProgramar.get():
            return "Moderado"
        return "Leve"