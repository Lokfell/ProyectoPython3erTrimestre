import psycopg2

try:
    conexion = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="PruebaPython",
        user="postgres",
        password="123"
    )
    print("Conexión exitosa a la base de datos PostgreSQL.")
except Exception as e:
    print("Error al conectar:", e)