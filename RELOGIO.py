import tkinter as tk
from datetime import datetime

def atualizar_relogio():
    agora = datetime.now()
    hora_formatada = agora.strftime("%H:%M:%S")
    label.config(text=hora_formatada)
    # Atualiza o relogio a cada 1000 milissegundos (1 segundo)
    root.after(1000, atualizar_relogio)

# Cria a janela principal
root = tk.Tk()
root.title("Relogio")

# Cria um rotulo para exibir a hora
label = tk.Label(root, font=("Helvetica", 48), fg="black")
label.pack()

# Inicia a atualização do relogio
atualizar_relogio()

# Inicia o loop da interface grafica
root.mainloop()