import tkinter as tk

from util import processarCsv

temPlaca = None
labelSocket = None
listaSockets = None

def get_socket():
    global temPlaca

    if temPlaca.get():
        valor = listaSockets.curselection()
        if valor:
            return listaSockets.get(valor[0])
        else: return "Não possui"
    else: return "Não possui"

def mostrar_sockets(frame, sockets):
    global labelSocket, listaSockets

    if temPlaca.get():
        if labelSocket is None:
            labelSocket = tk.Label(frame, text="Selecione seu socket:", font=("Arial", 11, "bold"))
            labelSocket.grid(row=2, column=0, pady=5)
        if listaSockets is None:
            listaSockets = tk.Listbox(frame)
            for socket in sockets:
                listaSockets.insert(tk.END, socket)
            listaSockets.grid(row=2, column=1)
    else:
        if labelSocket is not None:
            labelSocket.grid_forget()
            listaSockets.grid_forget()
            labelSocket = None
            listaSockets = None

def inicializa_frame(janela):
    global temPlaca
    framePlaca = tk.Frame(janela)
    framePlaca.grid(row=4, column=0, sticky="w", pady=10)

    labelPlaca = tk.Label(framePlaca, text="Você já tem uma placa-mãe?", font=("Arial", 11, "bold"))
    labelPlaca.grid(row=0, column=0)

    temPlaca = tk.BooleanVar()
    radioSimPlaca = tk.Radiobutton(framePlaca, text="Sim", variable=temPlaca, value=True, command=lambda: mostrar_sockets(framePlaca, processarCsv.get_sockets()))
    radioSimPlaca.grid(row=1, column=0)

    radioNaoPlaca = tk.Radiobutton(framePlaca, text="Não", variable=temPlaca, value=False, command=lambda: mostrar_sockets(framePlaca, processarCsv.get_sockets()))
    radioNaoPlaca.grid(row=1, column=1)