import psycopg2
import bcrypt

def verificar_login(usuario, clave_ingresada):
    try:
        # Conexión a la base de datos
        conexion = psycopg2.connect(
            host="localhost",
            port=5432,
            dbname="PruebaPython",
            user="postgres",
            password="123"
        )
        cursor = conexion.cursor()
        
        # Buscar solo por usuario
        consulta = "SELECT clave FROM usuarios WHERE usuario = %s"
        cursor.execute(consulta, (usuario,))
        resultado = cursor.fetchone()
        
        cursor.close()
        conexion.close()

        if resultado:
            clave_encriptada = resultado[0].encode('utf-8')  # convertir de texto a bytes
            return bcrypt.checkpw(clave_ingresada.encode('utf-8'), clave_encriptada)
        else:
            return False

    except Exception as e:
        print("Error al conectar o consultar:", e)
        return False

# Ejemplo de uso
usuario = input("Usuario: ")
clave = input("Clave: ")

if verificar_login(usuario, clave):
    print("Login exitoso.")
else:
    print("Usuario o Clave incorrectos.")