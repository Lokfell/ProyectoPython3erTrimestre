import tkinter as tk 
from tkinter import ttk, messagebox
import bcrypt
import conexion
import FormularioMenu

def verificar_login():
    try:
        usuario = entry_usuario.get()
        clave_ingresada = entry_clave.get()

        conn = conexion.conexion()
        cursor = conn.cursor()

        # Traemos también el rol para decidir después
        consulta = "SELECT clave, rol FROM usuarios WHERE usuario = %s"
        cursor.execute(consulta, (usuario,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        if resultado:
            clave_encriptada, rol = resultado
            clave_encriptada = clave_encriptada.encode('utf-8')

            if bcrypt.checkpw(clave_ingresada.encode('utf-8'), clave_encriptada):
                if rol == "Alumno/a":
                    messagebox.showinfo("Éxito", "Bienvenido Alumno/a")
                    app.withdraw()  
                    FormularioMenu.menu()   # Abre menú de alumno
                else:
                    messagebox.showinfo("Éxito", f"Bienvenido {rol}")
                    app.withdraw()
                    FormularioMenu.menuA()  # Abre menú de administrador u otro rol
                return True
            else:
                messagebox.showerror("Error", "Clave incorrecta")
                return False
        else:
            messagebox.showerror("Error", "Usuario no encontrado")
            return False

    except Exception as e:
        messagebox.showerror("Error", f"Problema en la conexión: {e}")
        return False


# Crear la ventana principal de la aplicación
app = tk.Tk()
app.title("LOGIN")
app.geometry("320x210")

ttk.Label(app, text="Iniciar Sesión", font=("Arial", 17), foreground="#1CC663").grid(column=1, row=0, padx=10, pady=10)

ttk.Label(app, text="Usuario", font=("Arial", 11)).grid(column=0, row=1, padx=10, pady=10)
entry_usuario = ttk.Entry(app, width=30)
entry_usuario.grid(column=1, row=1)

ttk.Label(app, text="Clave", font=("Arial", 11)).grid(column=0, row=2, padx=10, pady=10)
entry_clave = ttk.Entry(app, width=30, show="*")
entry_clave.grid(column=1, row=2)

i = ttk.Style()
i.configure("iniciar.TButton", foreground="#000000", background="#0fca37")
i.map("iniciar.TButton", foreground=[("active", "#0E8216")])

ttk.Button(app, text="Iniciar Sesión", command=verificar_login, style="iniciar.TButton").grid(column=1, row=10, pady=20)

app.mainloop()