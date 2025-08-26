import tkinter as tk
from tkinter import ttk, messagebox
import conexion
import FormularioMenu
import bcrypt

def mostrar_FUsuario():
    # ---- Funciones de la aplicación ----
    def volver():
        app.destroy()
        FormularioMenu.menu()
    
    def limpiar():
        entry_cod_persona.delete(0, tk.END)
        entry_usuario.delete(0, tk.END)
        entry_clave.delete(0, tk.END)

    def insertar():
        cod_persona = entry_cod_persona.get()
        usuario = entry_usuario.get()
        clave = entry_clave.get()

        if not cod_persona:
            messagebox.showerror("Error", "La C.I. es obligatoria")
            return
        if not usuario:
            messagebox.showerror("Error", "El usuario es obligatorio")
            return
        if not clave:
            messagebox.showerror("Error", "La clave es obligatoria")
            return

        try:
            conn = conexion.conexion()
            cursor = conn.cursor()
            clave_encriptada = bcrypt.hashpw(clave.encode('utf-8'), bcrypt.gensalt())
            consulta = "INSERT INTO usuarios (cod_persona, usuario, clave, rol) VALUES (%s, %s, %s, 'Alumno/a')"
            cursor.execute(consulta, (cod_persona, usuario, clave_encriptada.decode('utf-8')))
            conn.commit()
            cursor.close()
            conn.close()

            messagebox.showinfo("Éxito", "Usuario insertado correctamente")
            limpiar()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo insertar el usuario: {e}")
        
      
    # ---- Configuración de la ventana ----
    app = tk.Tk()
    app.title("Formulario de Usuario")
    app.geometry("380x230")

    ttk.Label(app, text="Formulario de Usuario", font=("Arial", 17), foreground="#1CC663").grid(column=0, row=0, columnspan=2, padx=10, pady=10)

    # Campos
    etiquetas = ["C.I.", "Usuario", "Clave"]
    for i, texto in enumerate(etiquetas, start=1):
        ttk.Label(app, text=texto, font=("Arial", 11)).grid(column=0, row=i, padx=10, pady=10, sticky="ew")
            
    entry_cod_persona = ttk.Entry(app, width=30); entry_cod_persona.grid(column=1, row=1)
    entry_usuario = ttk.Entry(app, width=30); entry_usuario.grid(column=1, row=2)
    entry_clave = ttk.Entry(app, width=30, show="*"); entry_clave.grid(column=1, row=3)

    # ---- Botones ----

    ttk.Button(app, text="Insertar Usuario", command=insertar).grid(column=0, row=10, padx=10, pady=10)
    ttk.Button(app, text="Limpiar", command=limpiar).grid(column=1, row=10, pady=10)
    ttk.Button(app, text="🔙", command=volver).grid(column=2, row=10, columnspan=2, pady=10)
    
    app.mainloop()