import psycopg2
import tkinter as tk
from tkinter import ttk, messagebox


app=tk.Tk()
app.title("Formulario de Datos Personales del Alumno")
app.geometry("400x300")

ttk.Label(app, text="Nombre").grid(column=0, row=0, padx=10, pady=10)
entry_nombre = ttk.Entry(app)
entry_nombre.grid(column=1, row=0)

ttk.Label(app, text="Apellido").grid(column=0, row=1, padx=10, pady=10)
entry_apellido = ttk.Entry(app)
entry_apellido.grid(column=1, row=1)

ttk.Label(app, text="ci").grid(column=0, row=2, padx=10, pady=10)
entry_ci = ttk.Entry(app)
entry_ci.grid(column=1, row=2)


