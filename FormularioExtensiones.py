import tkinter as tk
from tkinter import ttk, messagebox
import conexion
import FormularioMenu

def mostrar_FExtensiones():
    # ---- Funciones de la aplicación ----
    def volver():
        app.destroy()
        FormularioMenu.menu()
        
    def obtener_carrera():
        try:
            conn = conexion.conexion()
            with conn.cursor() as cursor:
                cursor.execute('SELECT descripcion FROM carreras') 
                resultados = cursor.fetchall()
                opciones = [fila[0] for fila in resultados]
            conn.close()
            return opciones
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener carreras: {e}")
            return []
    
    def limpiar():
        entry_cod_persona.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
        entry_horas.delete(0, tk.END)
        combo_carrera.set("Seleccione una Carrera")

    def insertar():
        cod_persona = entry_cod_persona.get()
        descripcion = entry_descripcion.get()
        horas = entry_horas.get()
        carrera = combo_carrera.get()

        if not cod_persona:
            messagebox.showerror("Error", "La C.I. es obligatoria")
            return
        if not carrera:
            messagebox.showerror("Error", "La carrera es obligatoria")
            return
        try:
            conn = conexion.conexion()
            cursor = conn.cursor()
            consulta = "INSERT INTO extensiones (descripcion, horas, cod_persona, cod_carrera) VALUES (%s, %s, %s, %s)"
            cursor.execute(consulta, (descripcion, horas,  cod_persona, carrera))
            conn.commit()
            cursor.close()
            conn.close()

            messagebox.showinfo("Éxito", "Extension insertada correctamente")
            limpiar()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo insertar la Extension: {e}")
        
      
    # ---- Configuración de la ventana ----
    app = tk.Tk()
    app.title("Formulario de Extensiones")
    app.geometry("380x270")

    ttk.Label(app, text="Formulario de Extensiones", font=("Arial", 17), foreground="#1CC663").grid(column=0, row=0, columnspan=2, padx=10, pady=10)

    # Campos
    etiquetas = ["C.I.", "Descripcion", "Horas", "Carrera"]
    for i, texto in enumerate(etiquetas, start=1):
        ttk.Label(app, text=texto, font=("Arial", 11)).grid(column=0, row=i, padx=10, pady=10, sticky="ew")
    
    entry_cod_persona = ttk.Entry(app, width=30); entry_cod_persona.grid(column=1, row=1)
    entry_descripcion = ttk.Entry(app, width=30); entry_descripcion.grid(column=1, row=2)
    entry_horas = ttk.Entry(app, width=30); entry_horas.grid(column=1, row=3)
    
    opciones = obtener_carrera()
    combo_carrera = ttk.Combobox(app, values=opciones, state="readonly", width=28)
    combo_carrera.grid(column=1, row=4)

    # ---- Botones ----

    ttk.Button(app, text="Insertar Extension", command=insertar).grid(column=0, row=10, padx=10, pady=10)
    ttk.Button(app, text="Limpiar", command=limpiar).grid(column=1, row=10, pady=10)
    ttk.Button(app, text="🔙", command=volver).grid(column=2, row=10, columnspan=2, pady=10)
    
    app.mainloop()