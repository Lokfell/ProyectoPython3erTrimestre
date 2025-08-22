import tkinter as tk
from tkinter import PhotoImage, ttk, messagebox
import conexion
# ---- Funciones de la aplicación ----
def limpiar():
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_ci.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_direccion.delete(0, tk.END)     


# Insertar datos en la tabla alumnos
def insertar():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    ci = entry_ci.get()
    telefono = entry_telefono.get()
    email = entry_email.get()   
    direccion = entry_direccion.get()
    
    if not nombre or not apellido or not ci:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return
    
    try:
        conn = conexion.conexion()
        if conn is None:
            return
        
        cursor = conn.cursor()
        cursor.execute("INSERT INTO alumnos (nombre, apellido, ci, telefono, email, direccion) VALUES (%s, %s, %s, %s, %s, %s)",
                       (nombre, apellido, ci, telefono, email, direccion))
        conn.commit()
        limpiar()
        messagebox.showinfo("Éxito", "Datos insertados correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        cursor.close()
        conn.close()
        
# Actualizar datos en la tabla alumnos
def actualizar():
    global entry_ci
    global entry_nombre
    global entry_apellido
    global entry_telefono
    global entry_email
    global entry_direccion
    
    if not entry_ci.get():
        messagebox.showerror("Error", "El campo CI es obligatorio")
        return
    
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()
    email = entry_email.get()
    direccion = entry_direccion.get()

    
    if not nombre or not apellido:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return
    
    try:
        conn = conexion.conexion()
        if conn is None:
            return
        cursor = conn.cursor()
        cursor.execute("UPDATE alumnos SET nombre=%s, apellido=%s, telefono=%s, email=%s, direccion=%s WHERE ci=%s",
                       (nombre, apellido, telefono, email, direccion, entry_ci.get()))
        conn.commit()
        limpiar()
        messagebox.showinfo("Éxito", "Datos actualizados correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        cursor.close()
        conn.close()

# Eliminar datos de la tabla alumnos
def eliminar():
        global entry_ci
        
        if not entry_ci.get():
            messagebox.showerror("Error", "El campo CI es obligatorio")
            return
        
        try:
            conn = conexion.conexion()
            if conn is None:
                return
            cursor = conn.cursor()
            cursor.execute("DELETE FROM alumnos WHERE ci=%s", (entry_ci.get(),))
            conn.commit()
            limpiar()
            messagebox.showinfo("Éxito", "Datos eliminados correctamente")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            cursor.close()
            conn.close()

# Consultar datos de la tabla alumnos           
def consultar():
    global entry_ci
    global entry_nombre
    global entry_apellido
    global entry_telefono
    global entry_email
    global entry_direccion
    
    # Limpia el área de texto antes de mostrar nuevos resultados
    text_resultado.delete("1.0", tk.END)
    
    if not entry_ci.get():
        messagebox.showerror("Error", "El campo CI es obligatorio")
        return
    
    try:
        conn = conexion.conexion()
        if conn is None:
            return
        cursor = conn.cursor()
        cursor.execute("SELECT ci, nombre, apellido, telefono, direccion, email FROM alumnos WHERE ci=%s", (entry_ci.get(),))
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
            entry_direccion.delete(0, tk.END)
            entry_direccion.insert(0, result[5])
            
            # Muestra los resultados en el área de texto
            texto = f"CI: {result[0]}\nNombre: {result[1]}\nApellido: {result[2]}\nTeléfono: {result[3]}\nEmail: {result[4]}\nDirección: {result[5]}"
            text_resultado.delete("1.0", tk.END)  # Limpia el área de texto antes de insertar nuevos datos
            text_resultado.insert(tk.END, texto)
            
        else:
            messagebox.showwarning("Consulta", "No se encontraron datos para el CI proporcionado")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        cursor.close()
        conn.close()   

# Limpiar campos del formulario
      

#  Crear la ventana principal de la aplicación
app=tk.Tk()
app.title("Formulario de Datos Personales del Alumno")
app.geometry("505x610")

ttk.Label(app, text="Datos del Alumno", font=("Arial", 17), foreground="#683DCC").grid(column=1, row=0, padx=10, pady=10)

ttk.Label(app, text="Nombre", font=("Arial", 11)).grid(column=0, row=1, padx=10, pady=10)
entry_nombre = ttk.Entry(app, width=50)
entry_nombre.grid(column=1, row=1)

ttk.Label(app, text="Apellido", font=("Arial", 11)).grid(column=0, row=2, padx=10, pady=10)
entry_apellido = ttk.Entry(app,  width=50)
entry_apellido.grid(column=1, row=2)

ttk.Label(app, text="ci", font=("Arial", 11)).grid(column=0, row=3, padx=10, pady=10)
entry_ci = ttk.Entry(app, width=50)
entry_ci.grid(column=1, row=3)

ttk.Label(app, text="Telefono", font=("Arial", 11)).grid(column=0, row=4, padx=10, pady=10)
entry_telefono = ttk.Entry(app, width=50)
entry_telefono.grid(column=1, row=4)

ttk.Label(app, text="Email", font=("Arial", 11)).grid(column=0, row=5, padx=10, pady=10)
entry_email = ttk.Entry(app, width=50)    
entry_email.grid(column=1, row=5)

ttk.Label(app, text="Nacionalidad", font=("Arial", 11)).grid(column=0, row=6, padx=10, pady=10)
entry_nacionalidad = ttk.Entry(app, width=50)
entry_nacionalidad.grid(column=1, row=6)

ttk.Label(app, text="Ciudad", font=("Arial", 11)).grid(column=0, row=7, padx=10, pady=10)
entry_ciudad = ttk.Entry(app, width=50)
entry_ciudad.grid(column=1, row=7)

ttk.Label(app, text="Dirección", font=("Arial", 11)).grid(column=0, row=8, padx=10, pady=10)
entry_direccion = ttk.Entry(app, width=50)
entry_direccion.grid(column=1, row=8)

# Agrega un Label para el área de texto
ttk.Label(app, text="Resultado", font=("Arial", 11)).grid(column=0, row=9, padx=10, pady=10)

# Crea el widget Text (área de texto)
text_resultado = tk.Text(app, height=6, width=40, font=("Arial", 10))
text_resultado.grid(column=1, row=9, padx=10, pady=10, columnspan=1)

e = ttk.Style()
e.configure("eliminar.TButton",foreground="#000000", background="#ff0000")
e.map("eliminar.TButton", foreground=[("active", "#A50404")])

i = ttk.Style()
i.configure("insertar.TButton",  foreground="#000000", background="#0fca37")
i.map("insertar.TButton", foreground=[("active", "#0E8216")])


ttk.Button(app, text="Insertar", command=insertar, style="insertar.TButton").grid(column=0, row=10, columnspan=1)
ttk.Button(app, text="Actualizar", command=actualizar).grid(column=1, row=10, columnspan=1)    
ttk.Button(app, text="Eliminar", command=eliminar, style="eliminar.TButton").grid(column=2, row=10)
ttk.Button(app, text="Buscar", command=consultar).grid(column=2, row=3 , columnspan=1, padx=10, pady=10)  
ttk.Button(app, text="Limpiar", command=limpiar).grid(column=2, row=12 , columnspan=1, padx=10, pady=10)   
# ttk.Button(app, text="Salir", command=app.quit).grid(column=2, row=8, columnspan=1, padx=10, pady=10)

app.mainloop()