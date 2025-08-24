from tkinter import ttk
import tkinter as tk

root = tk.Tk()

# Lista de opciones
opciones = ["Argentina", "Brasil", "Chile", "Paraguay"]

# Crear el ComboBox
combo = ttk.Combobox(root, values=opciones, state="readonly")
combo.set("Seleccione un país")  # Texto inicial
combo.pack(padx=10, pady=10)

# Obtener el valor seleccionado
def mostrar_seleccion():
    seleccionado = combo.get()
    print("Seleccionaste:", seleccionado)

ttk.Button(root, text="Mostrar selección", command=mostrar_seleccion).pack()

root.mainloop()