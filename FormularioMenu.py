import tkinter as tk
from tkinter import ttk
import FormularioPersona
import FormularioCiudad
import FormularioUsuario
import FormularioCarreras
import FormularioNacionalidad
import FormularioExtensiones

def menuA():
    # ---- Configuración de la ventana ----
    app = tk.Tk()
    app.title("MENÚ PRINCIPAL")
    app.geometry("370x380")

    def abrir_formulario_Ciudad():
        app.withdraw()  # Oculta la ventana del menú
        FormularioCiudad.mostrar_FCiudad()  
        app.deiconify()  # Vuelve a mostrar el menú al cerrar el formulario

    def abrir_formulario_alumno():
        app.withdraw()  
        FormularioPersona.mostrar_formulario()  
        app.deiconify()
        
    def abrir_formulario_usuario():
        app.withdraw()  
        FormularioUsuario.mostrar_FUsuario()  
        app.deiconify()
        
    def abrir_formulario_carreras():
        app.withdraw()  
        FormularioCarreras.mostrar_FCarreras()  
        app.deiconify()
        
    def abrir_formulario_nacionalidad():
        app.withdraw()  
        FormularioNacionalidad.mostrar_FNacionalidad()  
        app.deiconify()
        
    def abrir_formulario_extensiones():
        app.withdraw()  
        FormularioExtensiones.mostrar_FExtensiones()  
        app.deiconify()

    ttk.Label(app, text="Menú Principal", font=("Arial", 17), foreground="#43AE70").pack(pady=10)
    ttk.Button(app, text="Abrir Formulario de Alumno", command=abrir_formulario_alumno).pack(pady=10)
    ttk.Button(app, text="Abrir Formulario de Ciudad", command=abrir_formulario_Ciudad).pack(pady=10)
    ttk.Button(app, text="Abrir Formulario de Usuario", command=abrir_formulario_usuario).pack(pady=10)
    ttk.Button(app, text="Abrir Formulario de Carreras", command=abrir_formulario_carreras).pack(pady=10)
    ttk.Button(app, text="Abrir Formulario de Nacionalidad", command=abrir_formulario_nacionalidad).pack(pady=10)
    ttk.Button(app, text="Abrir Formulario de Extensiones", command=abrir_formulario_extensiones).pack(pady=10)
    ttk.Button(app, text="Salir", command=app.quit).pack(pady=10)

    app.mainloop()
    
def menu():
    # ---- Configuración de la ventana ----
    app = tk.Tk()
    app.title("MENÚ PRINCIPAL")
    app.geometry("370x380")

    def abrir_formulario_extensiones():
        app.withdraw()  
        FormularioExtensiones.mostrar_FExtensiones()  
        app.deiconify()

    ttk.Label(app, text="Menú Principal", font=("Arial", 17), foreground="#43AE70").pack(pady=10)
    ttk.Button(app, text="Abrir Formulario de Extensiones", command=abrir_formulario_extensiones).pack(pady=10)
    ttk.Button(app, text="Salir", command=app.quit).pack(pady=10)

    app.mainloop()