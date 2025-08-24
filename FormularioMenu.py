import tkinter as tk
from tkinter import ttk
import FormularioAlumno
import FormularioCiudad

def menu():
    # ---- Configuración de la ventana ----
    app = tk.Tk()
    app.title("MENÚ PRINCIPAL")
    app.geometry("300x200")

    def abrir_formulario_Ciudad():
        app.withdraw()  # Oculta la ventana del menú
        FormularioCiudad.mostrar_FCiudad()  
        app.deiconify()  # Vuelve a mostrar el menú al cerrar el formulario

    def abrir_formulario_alumno():
        app.withdraw()  
        FormularioAlumno.mostrar_formulario()  
        app.deiconify()

    ttk.Label(app, text="Menú Principal", font=("Arial", 17), foreground="#43AE70").pack(pady=10)
    ttk.Button(app, text="Abrir Formulario de Alumno", command=abrir_formulario_alumno).pack(pady=10)
    ttk.Button(app, text="Abrir Formulario de Ciudad", command=abrir_formulario_Ciudad).pack(pady=10)
    ttk.Button(app, text="Salir", command=app.quit).pack(pady=10)

    app.mainloop()