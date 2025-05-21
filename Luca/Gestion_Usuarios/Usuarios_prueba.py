usuarios = [
    {'nombre': 'admin', 'password': 'admin123', 'rol': 'admin'}
]

def interfaz_menu_principal():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Iniciar sesión")
    print("2. Salir")

def interfaz_menu_admin():
    print("\n--- MENÚ ADMINISTRADOR ---")
    print("1. Crear usuario")
    print("2. Eliminar usuario")
    print("3. Listar usuarios")
    print("4. Cerrar sesión")

def interfaz_menu_usuario():
    print("\n--- MENÚ USUARIO ---")
    print("1. Ver perfil")
    print("2. Cerrar sesión")

def iniciar_sesion():
    intentos = 0
    while intentos < 3:
        nombre = input("Ingrese nombre de usuario: ")
        password = input("Ingrese contraseña: ")
        for u in usuarios:
            if u['nombre'] == nombre and u['password'] == password:
                print(f"Bienvenido, {nombre}. Rol: {u['rol']}")
                return u
        intentos += 1
        print(f"Usuario o contraseña incorrectos. Intento {intentos} de 3.")
    print("Se superó el número máximo de intentos.")
    return None

def crear_usuario():
    print("\n-- Crear nuevo usuario --")
    nombre = input("Nombre de usuario: ")

    # Validar que el nombre no exista ya
    for u in usuarios:
        if u['nombre'] == nombre:
            print("Error: El nombre de usuario ya existe.")
            return

    password = input("Contraseña: ")

    # Elegir rol por opción numérica
    while True:
        print("Seleccione rol:")
        print("1. Admin")
        print("2. Usuario")
        opcion = input("Opción (1/2): ")
        if opcion == '1':
            rol = 'admin'
            break
        elif opcion == '2':
            rol = 'usuario'
            break
        else:
            print("Opción inválida. Intente de nuevo.")

    usuarios.append({'nombre': nombre, 'password': password, 'rol': rol})
    print(f"Usuario '{nombre}' creado con rol '{rol}'.")

def eliminar_usuario():
    print("\n-- Eliminar usuario --")
    nombre = input("Ingrese nombre de usuario a eliminar: ")

    if nombre == 'admin':
        print("No se puede eliminar al usuario administrador principal.")
        return

    for i, u in enumerate(usuarios):
        if u['nombre'] == nombre:
            usuarios.pop(i)
            print(f"Usuario '{nombre}' eliminado.")
            return

    print("Usuario no encontrado.")

def listar_usuarios():
    print("\n-- Lista de usuarios --")
    for u in usuarios:
        print(f"- Nombre: {u['nombre']}, Rol: {u['rol']}")

def ver_perfil(usuario):
    print("\n-- Perfil de usuario --")
    print(f"Nombre: {usuario['nombre']}")
    print(f"Rol: {usuario['rol']}")

def menu_administrador(usuario_actual):
    while True:
        interfaz_menu_admin()
        try:
            opcion = input("Elija una opción: ")
            if opcion == '1':
                crear_usuario()
            elif opcion == '2':
                eliminar_usuario()
            elif opcion == '3':
                listar_usuarios()
            elif opcion == '4':
                print("Cerrando sesión...")
                break
            else:
                print("Opción no válida, intente de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}")

def menu_usuario(usuario_actual):
    while True:
        interfaz_menu_usuario()
        try:
            opcion = input("Elija una opción: ")
            if opcion == '1':
                ver_perfil(usuario_actual)
            elif opcion == '2':
                print("Cerrando sesión...")
                break
            else:
                print("Opción no válida, intente de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}")

def main():
    while True:
        interfaz_menu_principal()
        try:
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                usuario_actual = iniciar_sesion()
                if usuario_actual is None:
                    continue
                if usuario_actual['rol'] == 'admin':
                    menu_administrador(usuario_actual)
                else:
                    menu_usuario(usuario_actual)
            elif opcion == '2':
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida, intente de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
