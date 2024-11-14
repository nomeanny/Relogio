# Relógio com Tkinter 🕒

Este projeto é um simples relógio digital implementado com a biblioteca Tkinter em Python. Ele exibe a hora atual em uma janela gráfica e atualiza automaticamente a cada segundo.

## Funcionalidades

- Cria uma interface gráfica (GUI) com uma janela de relógio.
- Atualiza a hora em tempo real a cada segundo.
- Usa a função `root.after()` para garantir a atualização contínua da hora no rótulo (label).

## Pré-requisitos

- Python 3.x
- Biblioteca Tkinter (normalmente já incluída no Python)

## Como o código funciona

1. **Interface Gráfica**: A janela principal é criada usando o Tkinter.
2. **Função de Atualização**: A função `atualizar_relogio()` é chamada a cada segundo usando `root.after(1000, atualizar_relogio)`. Isso garante que a hora seja atualizada em tempo real.
3. **Loop Principal**: O `root.mainloop()` inicia o loop da interface gráfica, permitindo que a janela permaneça aberta e responda a eventos enquanto exibe o relógio.

## Como Executar

1. Clone este repositório ou copie o código para um arquivo `.py`.
2. Abra o terminal na pasta do arquivo.
3. Execute o comando:

    ```bash
    python nome_do_arquivo.py
    ```

4. A janela do relógio será aberta, exibindo a hora atual.

## Exemplo de Código

```python
import tkinter as tk
from time import strftime

def atualizar_relogio():
    hora_atual = strftime('%H:%M:%S')
    label.config(text=hora_atual)
    root.after(1000, atualizar_relogio)

root = tk.Tk()
root.title("Relógio")

label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
label.pack(anchor='center')

atualizar_relogio()
root.mainloop()
