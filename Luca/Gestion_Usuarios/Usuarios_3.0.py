# Valor constante que representa la opción de salir del programa
Fin = -1

# Listas de usuarios y contraseñas. El usuario 'root' es el único con privilegios de administrador.
usuarios = ["root", "Martin", "luca", "Pedro", "Lucia", "Tomas"]
contraseñas = ["1234", "123", "1234", "2210", "123456", "1234567"]

#-------------------------------------------- INTERFACES DE GESTIÓN DE USUARIO ------------------------------------------------
def menu_interactivo():
    print("=========================================================================================================")
    print("|                     BIENVENIDO, INGRESE SU SESSION PARA INGRESAR AL PROGRAMA                          |")
    print("=========================================================================================================")
    print("|                                     1. Iniciar sesión                                                 |")
    print("|                                    -1. Salir del programa                                             |")
    print("=========================================================================================================")
    print("=========================================================================================================")
    print("              Si no tiene sesión y necesita crear una, comunicarse con el administrador                 ")
    print("=========================================================================================================")

def Interfaz_CrearCuenta():
    print("=========================================================================================================")
    print("|                                        CREAR CUENTA (Solo Admin)                                      |")
    print("=========================================================================================================")

def Interfaz_EliminarCuenta():
    print("=========================================================================================================")
    print("|                                        ELIMINAR CUENTA (Solo Admin)                                   |")
    print("=========================================================================================================")

def Interfaz_ImprimirUsuarios():
    print("=========================================================================================================")
    print("|                                       LISTA DE USUARIOS                                               |")
    print("=========================================================================================================")

def Interfaz_BuscarUsuario():
    print("=========================================================================================================")
    print("|                                         BUSCAR USUARIO                                                |")
    print("=========================================================================================================")

def Interfaz_MenuAdministrador():
    print("=========================================================================================================")
    print("|                             MENÚ ADMINISTRADOR - Gestión de Usuarios                                  |")
    print("=========================================================================================================")
    print("|                                   1. Crear cuenta                                                     |")
    print("|                                   2. Eliminar cuenta                                                  |")
    print("|                                   3. Ver usuarios                                                     |")
    print("|                                   4. Buscar usuario                                                   |")
    print("|                                  -1. Cerrar sesión                                                    |")
    print("=========================================================================================================")

#-------------------------------------------- FUNCIONES DE GESTIÓN ------------------------------------------------
def iniciar_sesion():
    intentos = 0
    while intentos < 3:
        nombre = input("Nombre de usuario: ")
        clave = input("Contraseña: ")
        if nombre in usuarios:
            indice = usuarios.index(nombre)
            if contraseñas[indice] == clave:
                print("Inicio de sesión exitoso.")
                return nombre
        intentos += 1
        print("Credenciales incorrectas. Intentos restantes:", 3 - intentos)
    print("Demasiados intentos fallidos. Sesión bloqueada.")
    return None

def crear_cuenta():
    Interfaz_CrearCuenta()
    nuevo = input("Ingrese nombre del nuevo usuario: ")
    if nuevo in usuarios:
        print("Ese nombre ya está en uso.")
        return
    clave = input("Ingrese contraseña del nuevo usuario: ")
    usuarios.append(nuevo)
    contraseñas.append(clave)
    print("Cuenta creada exitosamente.")

def eliminar_cuenta():
    Interfaz_EliminarCuenta()
    nombre = input("Ingrese el nombre del usuario que desea eliminar: ")
    try:
        index = usuarios.index(nombre)
        usuarios.remove(nombre)
        contraseñas.pop(index)
        print("Usuario eliminado correctamente.")
    except ValueError:
        print("El usuario no existe.")

def imprimir_usuarios():
    Interfaz_ImprimirUsuarios()
    usuarios_con_claves = sorted(zip(usuarios, contraseñas), key=lambda x: x[0].lower())
    for nombre, clave in usuarios_con_claves:
        print(f"Usuario: {nombre:<15} | Contraseña: {'*' * len(clave)}")

def buscar_usuario():
    Interfaz_BuscarUsuario()
    try:
        nombre = input("Ingrese el nombre del usuario a buscar: ")
        if nombre in usuarios:
            print("El usuario existe.")
        else:
            print("El usuario NO existe.")
    except:
        print("Error al buscar usuario.")

def menu_admin():
    while True:
        Interfaz_MenuAdministrador()
        try:
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                crear_cuenta()
            elif opcion == "2":
                eliminar_cuenta()
            elif opcion == "3":
                imprimir_usuarios()
            elif opcion == "4":
                buscar_usuario()
            elif opcion == "-1":
                break
            else:
                print("Opción inválida.")
        except:
            print("Error inesperado.")

def menu_usuario(nombre):
    print("AQUI VA EL PROGRAMA GESTOR DE EVENTOS")

# ============================
#        PROGRAMA PRINCIPAL
# ============================
while True:
    menu_interactivo()
    try:
        entrada = input("Ingrese una opción: ")
        if entrada == "1":
            usuario_actual = iniciar_sesion()
            if usuario_actual == "root":
                menu_admin()
            elif usuario_actual is not None:
                menu_usuario(usuario_actual)
        elif entrada == "-1":
            print("USTED HA FINALIZADO EL PROGRAMA. HASTA LUEGO.")
            break
        else:
            print("Opción inválida.")
    except:
        print("Error inesperado en el menú principal.")
