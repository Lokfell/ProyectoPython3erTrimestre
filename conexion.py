import psycopg2
from tkinter import messagebox
# ---- Conexión a la base de datos ----
def conexion():
    try:
        conn = psycopg2.connect(database="PruebaPython", user="postgres", password="123", host="localhost", port="5432")        
        return conn
    except Exception as e:
        messagebox.showerror("Error de conexión", str(e))
        return None 