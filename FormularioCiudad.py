import tkinter as tk
from tkinter import ttk, messagebox
import conexion 
import FormularioMenu

def mostrar_FCiudad():
    # ---- Funciones de la aplicación ----
    def volver():
        app.destroy()
        FormularioMenu.menu()
    
    def limpiar():
        entry_nombre.delete(0, tk.END)
        combo_departamento.set("Seleccione el Departamento Correspondiente")
        
    def obtener_departamentos():
        try:
            conn = conexion.conexion()
            cursor = conn.cursor()
            cursor.execute('SELECT nombre FROM departamentos')  
            resultados = cursor.fetchall()
            opciones = [fila[0] for fila in resultados]
            cursor.close()
            conn.close()
            return opciones
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los departamentos: {e}")
            return []

    def insertar():
        nombre = entry_nombre.get()
        departamento = combo_departamento.get()

        if not nombre:
            messagebox.showerror("Error", "El nombre es obligatorio")
            return
        if departamento == "Seleccione el Departamento Correspondiente":
            messagebox.showerror("Error", "Debe seleccionar un departamento")
            return

        try:
            conn = conexion.conexion()
            cursor = conn.cursor()
            consulta = "INSERT INTO ciudades (nombre, departamento) VALUES (%s, %s)"
            cursor.execute(consulta, (nombre, departamento))
            conn.commit()
            cursor.close()
            conn.close()

            messagebox.showinfo("Éxito", "Ciudad insertada correctamente")
            limpiar()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo insertar la ciudad: {e}")

    # ---- Configuración de la ventana ----
    app = tk.Tk()
    app.title("Formulario de Ciudad")
    app.geometry("515x200")

    ttk.Label(app, text="Formulario de Ciudad", font=("Arial", 17), foreground="#1CC663").grid(column=0, row=0, columnspan=2, padx=10, pady=10)

    # Campos
    etiquetas = ["Nombre", "Departamento"]
    for i, texto in enumerate(etiquetas, start=1):
        ttk.Label(app, text=texto, font=("Arial", 11)).grid(column=0, row=i, padx=10, pady=10, sticky="ew")
            
    entry_nombre = ttk.Entry(app, width=50)
    entry_nombre.grid(column=1, row=1)

    opciones = obtener_departamentos()
    combo_departamento = ttk.Combobox(app, values=opciones, state="readonly", width=48)
    combo_departamento.set("Seleccione el Departamento Correspondiente")
    combo_departamento.grid(column=1, row=2)

    # ---- Botones ----

    ttk.Button(app, text="Insertar Ciudad", command=insertar).grid(column=0, row=10, pady=10)
    ttk.Button(app, text="Limpiar", command=limpiar).grid(column=1, row=10, pady=10)
    ttk.Button(app, text="🔙", command=volver).grid(column=2, row=10, padx=10, pady=10, sticky="e")
    
    app.mainloop()