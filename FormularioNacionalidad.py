import tkinter as tk
from tkinter import ttk, messagebox
import conexion
import FormularioMenu

def mostrar_FNacionalidad():
    # ---- Funciones de la aplicación ----
    def volver():
        app.destroy()
        FormularioMenu.menu()
    
    def limpiar():
        entry_descripción.delete(0, tk.END)

    def insertar():
        descripción = entry_descripción.get()

        if not descripción:
            messagebox.showerror("Error", "La descripción es obligatoria")
            return

        try:
            conn = conexion.conexion()
            cursor = conn.cursor()
            consulta = "INSERT INTO nacionalidades (descripcion) VALUES (%s)"
            cursor.execute(consulta, (descripción,))
            conn.commit()
            cursor.close()
            conn.close()

            messagebox.showinfo("Éxito", "Nacinalidad insertada correctamente")
            limpiar()
            listar()  # refrescar la tabla
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo insertar la Nacionalidad: {e}")

    def listar():
        """Traer todas las Nacionalidades de la BD y mostrarlas en el Treeview"""
        for fila in tabla.get_children():  # limpiar tabla antes de cargar
            tabla.delete(fila)

        try:
            conn = conexion.conexion()
            cursor = conn.cursor()
            cursor.execute("SELECT id, descripcion FROM nacionalidades ORDER BY id")
            resultados = cursor.fetchall()  # lista de tuplas [(1, 'Paraguayo/a'), (2, 'Argentino/a')]

            # Insertar filas en la tabla
            for fila in resultados:
                tabla.insert("", tk.END, values=fila)

            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron traer las nacionalidades: {e}")

    # ---- Configuración de la ventana ----
    app = tk.Tk()
    app.title("Formulario de Nacionalidades")
    app.geometry("490x425")

    ttk.Label(app, text="Formulario de Nacionalidad", font=("Arial", 17), foreground="#1CC663").grid(
        column=0, row=0, columnspan=2, padx=10, pady=10
    )

    # Campos
    etiquetas = ["Nacionalidad"]
    for i, texto in enumerate(etiquetas, start=1):
        ttk.Label(app, text=texto, font=("Arial", 11)).grid(column=0, row=i, padx=10, pady=10, sticky="ew")

    entry_descripción = ttk.Entry(app, width=48)
    entry_descripción.grid(column=1, row=1)

    # ---- Botones ----
    ttk.Button(app, text="Insertar Nacionalidad", command=insertar).grid(column=0, row=10, pady=10)
    ttk.Button(app, text="Limpiar", command=limpiar).grid(column=1, row=10, pady=10)
    ttk.Button(app, text="🔙", command=volver).grid(column=0, row=12, columnspan=2, pady=10)

    # ---- Tabla para mostrar nacionalidad ----
    columnas = ("ID", "Descripción")
    tabla = ttk.Treeview(app, columns=columnas, show="headings", height=10)
    tabla.grid(column=0, row=11, columnspan=2, padx=10, pady=10)

    # Encabezados
    tabla.heading("ID", text="ID")
    tabla.heading("Descripción", text="Descripción")

    # Ajustar tamaño columnas
    tabla.column("ID", width=50, anchor="center")
    tabla.column("Descripción", width=350, anchor="w")

    listar()  # cargar datos al iniciar

    app.mainloop()