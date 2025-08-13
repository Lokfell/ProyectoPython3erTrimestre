import psycopg2
import bcrypt

# Configuración de conexión
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "PruebaPython",
    "user": "postgres",
    "password": "123"
}

# Función para insertar usuario nuevo
def insertar_usuario(usuario, clave_plana):
    try:
        conexion = psycopg2.connect(**DB_CONFIG)
        cursor = conexion.cursor()

        # Encriptar la contraseña
        clave_encriptada = bcrypt.hashpw(clave_plana.encode('utf-8'), bcrypt.gensalt())

        # Insertar el nuevo usuario
        consulta = "INSERT INTO usuarios (usuario, clave) VALUES (%s, %s)"
        cursor.execute(consulta, (usuario, clave_encriptada.decode('utf-8')))

        conexion.commit()
        cursor.close()
        conexion.close()
        print("✅ Usuario creado correctamente.")
    except psycopg2.errors.UniqueViolation:
        print("⚠️ El usuario ya existe.")
    except Exception as e:
        print("❌ Error al insertar usuario:", e)

# Función para verificar login
def verificar_login(usuario, clave_ingresada):
    try:
        conexion = psycopg2.connect(**DB_CONFIG)
        cursor = conexion.cursor()

        consulta = "SELECT clave FROM usuarios WHERE usuario = %s"
        cursor.execute(consulta, (usuario,))
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado:
            clave_encriptada = resultado[0].encode('utf-8')
            if bcrypt.checkpw(clave_ingresada.encode('utf-8'), clave_encriptada):
                return True
        return False
    except Exception as e:
        print("❌ Error en la verificación:", e)
        return False

# Menú principal
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = input("Nuevo usuario: ")
            clave = input("Nueva clave: ")
            insertar_usuario(usuario, clave)
        elif opcion == "2":
            usuario = input("Usuario: ")
            clave = input("Clave: ")
            if verificar_login(usuario, clave):
                print("✅ Login exitoso.")
            else:
                print("❌ Usuario o clave incorrectos.")
        elif opcion == "3":
            print("👋 Saliendo del programa.")
            break
        else:
            print("⚠️ Opción inválida.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
