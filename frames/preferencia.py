import tkinter as tk

preferencia = None

def inicializa_frame(janela):
    global preferencia

    framePreferencias = tk.Frame(janela)
    framePreferencias.grid(row=2, column=0, sticky="w", pady=10)

    labelPreferencias = tk.Label(framePreferencias, text="Preferência por marcas:", font=("Arial", 11, "bold"))
    labelPreferencias.grid(row=0, column=0)

    preferencia = tk.StringVar(value="Indiferente")
    prefereIndiferente = tk.Radiobutton(framePreferencias, text="Indiferente", variable=preferencia, value="Indiferente")
    prefereIndiferente.grid(row=1, column=0)

    prefereItel = tk.Radiobutton(framePreferencias, text="Intel", variable=preferencia, value="Intel")
    prefereItel.grid(row=1, column=1)

    prefereAMD = tk.Radiobutton(framePreferencias, text="AMD", variable=preferencia, value="AMD")
    prefereAMD.grid(row=1, column=2)

def get_preferencia():
    if preferencia is None:
        return "Indiferente"
    return preferencia.get()
