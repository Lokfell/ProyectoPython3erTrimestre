import tkinter as tk
from tkinter import ttk, messagebox
import conexion
import FormularioMenu

def mostrar_formulario():
    # ---- Funciones de la aplicación ----
    def volver():
        app.destroy()
        FormularioMenu.menu()
        
    def limpiar():
        entry_apellido.delete(0, tk.END)
        entry_ci.delete(0, tk.END)
        entry_nombre.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        combo_nacionalidad.set("Seleccione una Nacionalidad")
        combo_ciudad.set("Seleccione una Ciudad")
        entry_direccion.delete(0, tk.END)
        text_resultado.delete("1.0", tk.END)

    def obtener_nacionalidad():
        try:
            conn = conexion.conexion()
            with conn.cursor() as cursor:
                cursor.execute('SELECT descripcion FROM nacionalidades')  # ⚠️ mejor sin tilde en la DB #Lo cambiare cuando no me de hueva
                resultados = cursor.fetchall()
                opciones = [fila[0] for fila in resultados]
            conn.close()
            return opciones
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener nacionalidades: {e}")
            return []

    def obtener_ciudad():
        try:
            conn = conexion.conexion()
            with conn.cursor() as cursor:
                cursor.execute('SELECT nombre FROM ciudades')
                resultados = cursor.fetchall()
                opcionesC = [fila[0] for fila in resultados]
            conn.close()
            return opcionesC
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener ciudades: {e}")
            return []

    def insertar():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        ci = entry_ci.get()
        telefono = entry_telefono.get()
        email = entry_email.get()
        nacionalidad = combo_nacionalidad.get()
        ciudad = combo_ciudad.get()
        direccion = entry_direccion.get()

        if not nombre or not apellido or not ci:
            messagebox.showerror("Error", "Nombre, Apellido y CI son obligatorios")
            return
        if nacionalidad.startswith("Seleccione") or ciudad.startswith("Seleccione"):
            messagebox.showerror("Error", "Debe seleccionar Nacionalidad y Ciudad")
            return

        try:
            conn = conexion.conexion()
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO personas (nombre, apellido, ci, telefono, email, nacionalidad, ciudad, direccion) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                (nombre, apellido, ci, telefono, email, nacionalidad, ciudad, direccion))
            conn.commit()
            limpiar()
            messagebox.showinfo("Éxito", "Datos insertados correctamente")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

    def actualizar():
        ci = entry_ci.get()
        if not ci:
            messagebox.showerror("Error", "El campo CI es obligatorio")
            return

        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        telefono = entry_telefono.get()
        email = entry_email.get()
        nacionalidad = combo_nacionalidad.get()
        ciudad = combo_ciudad.get()
        direccion = entry_direccion.get()

        try:
            conn = conexion.conexion()
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE personas SET nombre=%s, apellido=%s, telefono=%s, email=%s, 
                          nacionalidad=%s, ciudad=%s, direccion=%s WHERE ci=%s""",
                (nombre, apellido, telefono, email, nacionalidad, ciudad, direccion, ci))
            conn.commit()
            limpiar()
            messagebox.showinfo("Éxito", "Datos actualizados correctamente")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

    def eliminar():
        ci = entry_ci.get()
        if not ci:
            messagebox.showerror("Error", "El campo CI es obligatorio")
            return

        try:
            conn = conexion.conexion()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM personas WHERE ci=%s", (ci,))
            conn.commit()
            limpiar()
            messagebox.showinfo("Éxito", "Datos eliminados correctamente")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

    def consultar():
        text_resultado.delete("1.0", tk.END)
        ci = entry_ci.get()
        if not ci:
            messagebox.showerror("Error", "El campo CI es obligatorio")
            return

        try:
            conn = conexion.conexion()
            cursor = conn.cursor()
            cursor.execute("""SELECT ci, nombre, apellido, telefono, email, nacionalidad, ciudad, direccion 
                              FROM personas WHERE ci=%s""", (ci,))
            result = cursor.fetchone()

            if result:
                entry_nombre.delete(0, tk.END)
                entry_nombre.insert(0, result[1])
                entry_apellido.delete(0, tk.END)
                entry_apellido.insert(0, result[2])
                entry_telefono.delete(0, tk.END)
                entry_telefono.insert(0, result[3])
                entry_email.delete(0, tk.END)
                entry_email.insert(0, result[4])
                combo_nacionalidad.set(result[5])
                combo_ciudad.set(result[6])
                entry_direccion.delete(0, tk.END)
                entry_direccion.insert(0, result[7])

                texto = (f"CI: {result[0]}\nNombre: {result[1]}\nApellido: {result[2]}\n"
                         f"Teléfono: {result[3]}\nEmail: {result[4]}\n"
                         f"Nacionalidad: {result[5]}\nCiudad: {result[6]}\nDirección: {result[7]}")
                text_resultado.insert(tk.END, texto)
            else:
                messagebox.showwarning("Consulta", "No se encontraron datos para el CI proporcionado")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

    # ---- Interfaz ----
    app = tk.Tk()
    app.title("Formulario de Datos Personales del Alumno")
    app.geometry("510x505")

    ttk.Label(app, text="Datos del Alumno", font=("Arial", 17), foreground="#683DCC").grid(column=1, row=0, padx=10, pady=10)

    # Campos
    etiquetas = ["Nombre", "Apellido", "CI", "Teléfono", "Email", "Nacionalidad", "Ciudad", "Dirección"]
    for i, texto in enumerate(etiquetas, start=1):
        ttk.Label(app, text=texto, font=("Arial", 11)).grid(column=0, row=i, padx=10, pady=5, sticky="e")

    entry_nombre = ttk.Entry(app, width=50); entry_nombre.grid(column=1, row=1)
    entry_apellido = ttk.Entry(app, width=50); entry_apellido.grid(column=1, row=2)
    entry_ci = ttk.Entry(app, width=50); entry_ci.grid(column=1, row=3)
    entry_telefono = ttk.Entry(app, width=50); entry_telefono.grid(column=1, row=4)
    entry_email = ttk.Entry(app, width=50); entry_email.grid(column=1, row=5)

    opciones = obtener_nacionalidad()
    combo_nacionalidad = ttk.Combobox(app, values=opciones, state="readonly", width=48)
    combo_nacionalidad.set("Seleccione una Nacionalidad")
    combo_nacionalidad.grid(column=1, row=6)

    opcionesC = obtener_ciudad()
    combo_ciudad = ttk.Combobox(app, values=opcionesC, state="readonly", width=48)
    combo_ciudad.set("Seleccione una Ciudad")
    combo_ciudad.grid(column=1, row=7)

    entry_direccion = ttk.Entry(app, width=50); entry_direccion.grid(column=1, row=8)

    # Área de resultado
    ttk.Label(app, text="Resultado", font=("Arial", 11)).grid(column=0, row=9, padx=10, pady=5)
    text_resultado = tk.Text(app, height=6, width=40, font=("Arial", 10))
    text_resultado.grid(column=1, row=9, padx=10, pady=10)

    # Botones
    ttk.Button(app, text="Insertar", command=insertar).grid(column=0, row=10, pady=10)
    ttk.Button(app, text="Actualizar", command=actualizar).grid(column=1, row=10, pady=10)
    ttk.Button(app, text="Eliminar", command=eliminar).grid(column=2, row=10, pady=10)
    ttk.Button(app, text="Buscar", command=consultar).grid(column=2, row=3, padx=10, pady=5)
    ttk.Button(app, text="🔙", command=volver).grid(column=1, row=12, padx=10, pady=5)
    ttk.Button(app, text="Limpiar", command=limpiar).grid(column=2, row=12, padx=10, pady=5)

    app.mainloop()