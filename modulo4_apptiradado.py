import tkinter as tk
import random

ventana = tk.Tk()

def tirar_dado():
    valor_dado = (random.randint(1,6))
    etiqueta = tk.Label(text="Valor del dado: " + str(valor_dado))
    etiqueta.place(x=20, y=100)

ventana.config(width=300, height=300)
ventana.title("Jugar a los dados")

boton1 = tk.Button(text="Tirar Dado", command=tirar_dado)
boton1.place(x=20, y=50, width=100, height=30)


ventana.mainloop()