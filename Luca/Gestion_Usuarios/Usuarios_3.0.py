# MODIFICAR ESTRUCTURA DONDE SE GUARDAN LOS DATOS EN UN DICCIONARIO 

# Listas de usuarios y contraseñas. El usuario 'root' es el único con privilegios de administrador.
usuarios = ["admin", "Martin", "luca", "Pedro", "Lucia", "Tomas"]
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
    print("                Si no tiene necesita una cuenta , comunicarse con el administrador                       ")
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

def Interfaz_BuscarUsuario():
    print("=========================================================================================================")
    print("|                                          AUDITORIA                                                    |")
    print("=========================================================================================================")

def Interfaz_MenuAdministrador():
    print("=========================================================================================================")
    print("|                             MENÚ ADMINISTRADOR - Gestión de Usuarios                                  |")
    print("=========================================================================================================")
    print("|                                   1. Crear cuenta                                                     |")
    print("|                                   2. Eliminar cuenta                                                  |")
    print("|                                   3. Ver usuarios                                                     |")
    print("|                                   4. Buscar usuario                                                   |")
    print("|                                   5. Ver Auditoria (falta desarrollar)                                |")
    print("|                                   6. Cerrar sesión                                                    |")
    print("=========================================================================================================")

#-------------------------------------------- FUNCIONES DE GESTIÓN ------------------------------------------------
def iniciar_sesion():
    # MODIFICAR EN BASE A LA NUEVA ESTRUCTURA DONDE SE GUARDAN LOS DATOS (Diccionario)
    intentos = 0
    while intentos < 3:
    # NECESITO VALIDAR USANDO TRY: EXCEPT LOS PARAMETROS
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
    # MODIFICAR EN BASE A LA NUEVA ESTRUCTURA DONDE SE GUARDAN LOS DATOS (Diccionario)
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
    # MODIFICAR EN BASE A LA NUEVA ESTRUCTURA DONDE SE GUARDAN LOS DATOS (Diccionario)
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
    # MODIFICAR EN BASE A LA NUEVA ESTRUCTURA DONDE SE GUARDAN LOS DATOS (Diccionario)
    usuarios_con_claves = sorted(zip(usuarios, contraseñas), key=lambda x: x[0].lower())
    for nombre, clave in usuarios_con_claves:
        print(f"Usuario: {nombre:<15} | Contraseña: {'*' * len(clave)}")

def buscar_usuario():
    Interfaz_BuscarUsuario()
    # TRABAJO DE EXCEPT MAS ESPECIFICO PARA EL PROBLEMA , NO TAN GENERICO
    try:
        nombre = input("Ingrese el nombre del usuario a buscar: ")
        if nombre in usuarios:
            print("El usuario existe.")
        else:
            print("El usuario NO existe.")
    except:
        print("Error al buscar usuario.")

def menu_admin():
    # AGREGAR LA OPCION DE AUDITORIA EN EL MENU
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
    # REALIZAR UN MINI PROGRAMA DE GESTOR DE EVENTOS A MODO DE EJEMPLO, (CREAR,ELIMINAR,VER)
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
            if usuario_actual == "admin":
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


"""
    COSAS A AGREGAR EN EL PROGRAMA:
    - Cambio de estructura donde se guardan los datos (Diccionarios), modificando las funciones que estan involucradas
    - el uso de try: except en el programa de manera especifica para evitar errores
    - realizar funcion de AUDITORIA para el programa de solo uso para el administrador (tiene que auditar: Inicios/cierres de las cuentas de todos(admin y usuarios), modificaciones en datos personales, crear/eliminar/modificar eventos)
    - La Auditoria se tiene que guardar en un archivo .txt (FECHA,HORA,ACCION,QUIEN) CVS
    - El uso de archivos tiene que estar perfectamente estructurado para que no haya ningun error (Solicitarme que estructura necesita respertar)
    - Advertencia no utilizar librerias externas 
    - funcion Modificar tus datos de la cuenta (para usuarios)
    
    - Todo el programa tiene que estar documentado (descripciones breves de cada función y explicaciones de que hace)
        
    Cualquier otra cosa a contemplar notificarme antes, Necesito tambien que los cambios los vayas realizando con mi supervisacion
    Respeta la estructura del programa, las interfacez, todo tiene que estar en funciones y se tiene que cumplir que se hagan una unica cosa.
    si modificas algo me lo mostras y yo apruebo si se realiza el cambio.

    -Repetición de código
        Varias funciones repiten patrones similares (menús, impresiones).
        Sugerencia: Reutilizar código con funciones auxiliares para impresión de menús o validaciones.
        
    
"""
