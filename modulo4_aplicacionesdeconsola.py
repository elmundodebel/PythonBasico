import tkinter as tk

ventana = tk.Tk()

ventana.config(width=400, height=300)
ventana.title("Primera aplicación de escritorio")

boton1 = tk.Button(text="Hello")
boton1.place(x=20, y=50, width=100, height=30)


etiqueta = tk.Label(text="Ingresa tu nombre:")
etiqueta.place(x=20, y=100)

caja = tk.Entry()
caja.place(x=20, y=130, width=200, height=25)

ventana.mainloop()