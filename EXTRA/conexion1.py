import tkinter as tk
from tkinter import messagebox
import psycopg2

def check_connection():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            port=5432,
            dbname="PruebaPython",
            user="postgres",
            password="123"
        )
        
        conexion.close()
        messagebox.showinfo("Estado de la Conexión", "Conexion exitosa a la base de datos.")
    except Exception as e:
        messagebox.showinfo("Estado de la Conexión", f"Conexion fallida a la base de datos\nError: {e}")
        
root = tk.Tk()
root.title("Verificar Conexión a la Base de Datos")
root.geometry("500x150")
root.resizable(False, False)

windows_height = 150
windows_width = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (windows_width / 2))
y_coordinate = int((screen_height / 2) - (windows_height / 2))
root.geometry("{}x{}+{}+{}".format(windows_width, windows_height, x_coordinate, y_coordinate))

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(expand=True)

tk.Button(main_frame, text="Verificar Conexión", command=check_connection, width=20).pack(pady=10)
tk.Button(main_frame, text="Salir", command=root.quit, width=20).pack(pady=10)


root.mainloop()