# Valor constante que representa la opción de salir del programa
Fin = -1

# Listas de usuarios y contraseñas. El usuario 'admin' es el único con privilegios de administrador.
usuarios = ["root", "Martin", "luca", "Pedro", "Lucia", "Tomas"]
contraseñas = ["1234", "123", "1234", "2210", "123456", "1234567"]

#-------------------------------------------- INTERFECEZ DE GESTION DE USUARIO ------------------------------------------------
def menu_interactivo():
    print("=========================================================================================================")
    print("|                     BIENVENIDO, INGRESE SU SESSION PARA INGRESAR AL PROGRAMA                          |")
    print("=========================================================================================================")
    print("|                                     1. Iniciar sesión                                                 |")
    print("|                                    -1. Salir del programa                                             |")
    print("=========================================================================================================")
    print("=========================================================================================================")
    print("              Si no tiene seesion y necesita crear una, comunicarse con el administrador                 ")
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
    print("|                        MENÚ ADMINISTRADOR (admin) - Gestión de Usuarios                               |")
    print("=========================================================================================================")
    print("|                                   1. Crear cuenta                                                     |")
    print("|                                   2. Eliminar cuent                                                   |")
    print("|                                   3. Ver usuarios                                                     |")
    print("|                                   4. Buscar usuario                                                   |")
    print("|                                  -1. Cerrar sesión                                                    |")
    print("=========================================================================================================")
#-------------------------------------------- INTERFECEZ DE GESTION DE USUARIO ------------------------------------------------

# Permite al usuario iniciar sesión con usuario y contraseña. Devuelve el nombre si es exitoso.
def iniciar_sesion():
    intentos = 0
    while intentos < 3:
        nombre = input("Nombre de usuario: ")
        clave = input("Contraseña: ")
        i = 0
        while i < len(usuarios):
            if usuarios[i] == nombre and contraseñas[i] == clave:
                print("Inicio de sesión exitoso.")
                return nombre
            i += 1
        intentos += 1
        print("Credenciales incorrectas. Intentos restantes:", 3 - intentos)
    print("Demasiados intentos fallidos. Sesión bloqueada.")
    return None

# Solo para el administrador: permite crear una nueva cuenta de usuario
def crear_cuenta():
    nuevo = input("Ingrese nombre del nuevo usuario: ")
    i = 0
    while i < len(usuarios):
        if usuarios[i] == nuevo:
            print("Ese nombre ya está en uso.")
            return
        i += 1
    clave = input("Ingrese contraseña del nuevo usuario: ")
    usuarios.append(nuevo)
    contraseñas.append(clave)
    print("Cuenta creada exitosamente.")

# Solo para el administrador: permite eliminar un usuario existente (excepto el admin)
def eliminar_cuenta():
    nombre = input("Ingrese el nombre del usuario que desea eliminar: ")
    if nombre == "admin":
        print("No se puede eliminar al usuario administrador.")
        return
    i = 0
    while i < len(usuarios):
        if usuarios[i] == nombre:
            usuarios.pop(i)
            contraseñas.pop(i)
            print("Usuario eliminado correctamente.")
            return
        i += 1
    print("El usuario no existe.")

# Solo para el administrador: muestra la lista completa de usuarios con contraseñas ocultas
#------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------
def imprimir_usuarios():
    # Copiamos listas para no alterar las originales
    copia_usuarios = []
    copia_contraseñas = []
    i = 0
    while i < len(usuarios):
        copia_usuarios.append(usuarios[i])
        copia_contraseñas.append(contraseñas[i])
        i += 1

    # Ordenamos
    ordenar_usuarios_por_nombre(copia_usuarios, copia_contraseñas)

    # Imprimimos
    i = 0
    while i < len(copia_usuarios):
        nombre = copia_usuarios[i]
        clave = copia_contraseñas[i]
        asteriscos = ""
        j = 0
        while j < len(clave):
            asteriscos += "*"
            j += 1
        print("Usuario:", nombre, "| Contraseña:", asteriscos)
        i += 1
#------------------------------------------------------------------------------------------------------------------------------------
def buscar_usuario():
    nombre = input("Ingrese el nombre del usuario a buscar: ")
    i = 0
    existe = False
    while i < len(usuarios):
        if usuarios[i] == nombre:
            existe = True
        i += 1
    if existe:
        print("El usuario existe.")
    else:
        print("El usuario NO existe.")
#------------------------------------------------------------------------------------------------------------------------------------

# Menú exclusivo para el usuario "admin", con funciones de gestión de usuarios
def menu_admin():
    opcion = "0"
    while opcion != "-1":
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_cuenta()
        elif opcion == "2":
            eliminar_cuenta()
        elif opcion == "3":
            imprimir_usuarios()
        elif opcion == "4":
            buscar_usuario()
        elif opcion != "-1":
            print("Opción inválida.")


# Menú para usuarios normales con acceso limitado
def menu_usuario(nombre):
    opcion = ""
    while opcion != "-1":
        opcion = input("Seleccione una opción: ")
        if opcion != "-1":
            print("No tienes permisos para esa acción.")

# ============================
#        PROGRAMA PRINCIPAL
# ============================

# Bucle principal del programa
opcion_principal = 0
while opcion_principal != Fin:
    # Mostrar menú principal
    menu_interactivo()
    entrada = input("Ingrese una opción: ")
    # Lógica según opción seleccionada
    if entrada == 1:
        usuario_actual = iniciar_sesion()
        if usuario_actual == "root":
            menu_admin()  # Acceso total
        elif usuario_actual != None:
            menu_usuario(usuario_actual)  # Acceso limitado
    elif entrada == Fin:
        print("USTED HA FINALIZADO EL PROGRAMA. HASTA LUEGO.")
        opcion_principal = Fin
