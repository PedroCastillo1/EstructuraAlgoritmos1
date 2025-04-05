# Valor constante que representa la opción de salir del programa
Fin = -1

# Listas de usuarios y contraseñas. El usuario 'admin' es el único con privilegios de administrador.
usuarios = ["root", "Martin", "luca", "Pedro", "Lucia", "Tomas"]
contraseñas = ["1234", "123", "1234", "2210", "123456", "1234567"]

# Muestra el menú principal del programa
def menu_interactivo():
    print("="*97)
    print("|                             BIENVENIDO AL PROGRAMA DE GESTION DE EVENTOS                              |")
    print("="*97)
    print("|                                         1. Iniciar sesión                                              |")
    print("|                                        -1. Salir del programa                                          |")
    print("="*97)

# Función para verificar si una cadena es un número entero válido o "-1"
def es_entero(valor):
    digitos = "0123456789"
    if valor == "-1":
        return True
    i = 0
    while i < len(valor):
        if valor[i] not in digitos:
            return False
        i += 1
    return True

# Valida que la opción ingresada sea válida (1 o -1). Si no, vuelve a pedirla.
def verificar_menu(valor):
    if valor != 1 and valor != Fin:
        nuevo = input("Opción inválida. Ingrese una opción válida: ")
        if es_entero(nuevo):
            return verificar_menu(int(nuevo))
        else:
            return verificar_menu(None)
    return valor

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
    print("="*97)
    print("|                                         CREAR CUENTA (Solo Admin)                                      |")
    print("="*97)
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
    print("="*97)
    print("|                                         ELIMINAR CUENTA (Solo Admin)                                   |")
    print("="*97)
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
def ordenar_usuarios_por_nombre(lista_usuarios, lista_contraseñas):
    i = 0
    while i < len(lista_usuarios) - 1:
        j = 0
        while j < len(lista_usuarios) - i - 1:
            nombre_actual = lista_usuarios[j]
            nombre_siguiente = lista_usuarios[j + 1]

            k = 0
            menor = False
            mayor = False
            while (k < len(nombre_actual)) and (k < len(nombre_siguiente)) and (not menor) and (not mayor):
                if nombre_actual[k] > nombre_siguiente[k]:
                    mayor = True
                elif nombre_actual[k] < nombre_siguiente[k]:
                    menor = True
                k += 1

            if (mayor) or ((not menor) and (len(nombre_actual) > len(nombre_siguiente))):
                # Intercambiamos usuarios
                aux_u = lista_usuarios[j]
                lista_usuarios[j] = lista_usuarios[j + 1]
                lista_usuarios[j + 1] = aux_u
                # Intercambiamos contraseñas
                aux_c = lista_contraseñas[j]
                lista_contraseñas[j] = lista_contraseñas[j + 1]
                lista_contraseñas[j + 1] = aux_c
            j += 1
        i += 1
#------------------------------------------------------------------------------------------------------------------------------------
def imprimir_usuarios():
    print("="*97)
    print("|                          LISTA DE USUARIOS (ORDENADOS POR NOMBRE)                                    |")
    print("="*97)
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
    print("="*97)
#------------------------------------------------------------------------------------------------------------------------------------
def buscar_usuario():
    print("="*97)
    print("|                                         BUSCAR USUARIO                                                 |")
    print("="*97)
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
        print("="*97)
        print("|                        MENÚ ADMINISTRADOR (admin) - Gestión de Usuarios                               |")
        print("="*97)
        print("|                            1. Crear cuenta                                                             |")
        print("|                            2. Eliminar cuenta                                                          |")
        print("|                            3. Ver usuarios                                                             |")
        print("|                            4. Buscar usuario                                                           |")
        print("|                           -1. Cerrar sesión                                                            |")
        print("="*97)
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
    print("="*97)
    print("|                         MENÚ DE USUARIO:", nombre, " " * (48 - len(nombre)), "|")
    print("="*97)
    print("|                      (Este es un acceso limitado para usuarios estándar)                              |")
    print("|                         -1. Cerrar sesión                                                             |")
    print("="*97)
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

    # Pedir opción y validar
    entrada = input("Ingrese una opción: ")
    if es_entero(entrada):
        valor = verificar_menu(int(entrada))
    else:
        valor = verificar_menu(None)

    # Lógica según opción seleccionada
    if valor == 1:
        usuario_actual = iniciar_sesion()
        if usuario_actual == "root":
            menu_admin()  # Acceso total
        elif usuario_actual != None:
            menu_usuario(usuario_actual)  # Acceso limitado
    elif valor == Fin:
        print("USTED HA FINALIZADO EL PROGRAMA. HASTA LUEGO.")
        opcion_principal = Fin
