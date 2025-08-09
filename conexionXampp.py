import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Por defecto en XAMPP, el usuario root no tiene contraseña
        database="mysql",
        port=3306
    )
    print("Conexión exitosa a la base de datos MySQL/MariaDB.")
except mysql.connector.Error as err:
    print(f"Error al conectar: {err}")