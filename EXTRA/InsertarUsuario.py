import psycopg2
import bcrypt
import traceback


def insertar_usuario(cod_alumno, usuario, clave_plana, rol):
    try:
        conexion = psycopg2.connect(
            host="localhost",
            port=5432,
            dbname="PruebaPython",
            user="postgres",
            password="123"
        )
        cursor = conexion.cursor()

        # Encriptar la contraseña
        clave_encriptada = bcrypt.hashpw(clave_plana.encode('utf-8'), bcrypt.gensalt())

        # Insertar usuario
        consulta = "INSERT INTO usuarios (cod_persona, usuario, clave, rol) VALUES (%s, %s, %s, %s)"
        cursor.execute(consulta, (cod_alumno, usuario, clave_encriptada.decode('utf-8'), rol))

        conexion.commit()
        cursor.close()
        conexion.close()
        print("Usuario creado correctamente.")
    except Exception as e:
        print("Error al insertar usuario:")
        traceback.print_exc()
        

if __name__ == "__main__":
    insertar_usuario("123456", "Admin", "123", "Administrador")
