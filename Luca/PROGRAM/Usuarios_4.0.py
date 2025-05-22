from datetime import datetime

# Estructura actualizada: diccionario con contraseña y rol
usuarios = {
    #"admin": {"contraseña": "1234", "rol": "admin"},
}

eventos = {}
#########################################################################################################################################
#########################################################################################################################################
def Interfaz_CrearCuenta():
    print("=========================================================================================================")
    print("|                                        CREAR CUENTA (Solo Admin)                                      |")
    print("=========================================================================================================")
def Interfaz_ImprimirUsuarios():
    print("=========================================================================================================")
    print("|                                       LISTA DE USUARIOS                                               |")
    print("=========================================================================================================")
def Interfaz_BuscarUsuario():
    print("=========================================================================================================")
    print("|                                         BUSCAR USUARIO                                                |")
    print("=========================================================================================================")
def Interfaz_EliminarCuenta():
    print("=========================================================================================================")
    print("|                                        ELIMINAR CUENTA (Solo Admin)                                   |")
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
def Auditoria_interfaz():
    print("=========================================================================================================")
    print("|                                          AUDITORÍA DEL SISTEMA                                        |")
    print("=========================================================================================================")
def Interfaz_ModificarDatos():
    print("=========================================================================================================")
    print("|                               MODIFICAR DATOS PERSONALES - USUARIO                                    |")
    print("=========================================================================================================")
def Interfaz_MenuUsuario():
    print("=========================================================================================================")
    print("|                                    MENÚ USUARIO - GESTIÓN PERSONAL                                    |")
    print("=========================================================================================================")
    print("|                               1. Modificar mis datos personales                                       |")
    print("|                               2. Gestor de eventos (crear/ver/eliminar)                               |")
    print("|                               3. Cerrar sesión                                                        |")
    print("=========================================================================================================")
def Interfaz_MisEventos():
    print("=========================================================================================================")
    print("|                                            MIS EVENTOS                                                |")
    print("=========================================================================================================")
def Interfaz_EliminarEvento():
    print("=========================================================================================================")
    print("|                                         ELIMINAR EVENTO                                               |")
    print("=========================================================================================================")

def Interfaz_MenuEvento():
    print("=========================================================================================================")
    print("|                                      GESTOR DE EVENTOS                                                |")
    print("=========================================================================================================")
    print("|                             1. Crear nuevo evento                                                     |")
    print("|                             2. Ver mis eventos                                                        |")
    print("|                             3. Eliminar un evento                                                     |")
    print("|                             4. Volver al menú anterior                                                |")
    print("=========================================================================================================")
def Interfaz_CrearEvento():
    print("=========================================================================================================")
    print("|                                           CREAR EVENTO                                                |")
    print("=========================================================================================================")
#########################################################################################################################################
#########################################################################################################################################
def cargar_usuarios_desde_csv():
    """
    Carga los usuarios desde el archivo usuarios.csv al diccionario usuarios.
    Si el archivo no existe, arranca con un admin por defecto.
    """
    global usuarios
    usuarios = {}

    try:
        archivo = open("usuarios.csv", "rt")
        for linea in archivo:
            partes = linea.strip().split(",")
            if len(partes) == 3:
                nombre, contraseña, rol = partes
                usuarios[nombre] = {"contraseña": contraseña, "rol": rol}
    except FileNotFoundError:
        print("Archivo de usuarios no encontrado. Se creará con usuario admin por defecto.")
        usuarios["admin"] = {"contraseña": "1234", "rol": "admin"}
    except OSError as mensaje:
        print("Error al cargar usuarios:", mensaje)
    finally:
        try:
            archivo.close()
        except NameError:
            pass
#########################################################################################################################################
def guardar_usuarios_en_csv():
    """
    Guarda el contenido actual del diccionario usuarios en el archivo usuarios.csv.
    Sobrescribe el archivo completo.
    """
    try:
        archivo = open("usuarios.csv", "wt")
        for nombre, datos in usuarios.items():
            linea = f"{nombre},{datos['contraseña']},{datos['rol']}\n"
            archivo.write(linea)
    except OSError as mensaje:
        print("No se puede guardar el archivo de usuarios:", mensaje)
    finally:
        try:
            archivo.close()
        except NameError:
            pass       
#########################################################################################################################################
def cargar_eventos_desde_csv():
    """
    Carga los eventos desde el archivo eventos.csv al diccionario eventos.
    Si el archivo no existe, el diccionario queda vacío.
    """
    global eventos
    eventos = {}

    try:
        archivo = open("eventos.csv", "rt")
        for linea in archivo:
            partes = linea.strip().split(",")
            if len(partes) == 6:
                fecha, salon, turno, cliente, tipoevento, cantpersonas = partes
                clave = (fecha, salon, turno)
                eventos[clave] = [cliente, tipoevento, cantpersonas]
    except FileNotFoundError:
        print("Archivo de eventos no encontrado. Se iniciará sin eventos.")
    except OSError as mensaje:
        print("Error al cargar eventos:", mensaje)
    finally:
        try:
            archivo.close()
        except NameError:
            pass
#########################################################################################################################################
def guardar_eventos_en_csv():
    """
    Guarda el contenido actual del diccionario eventos en el archivo eventos.csv.
    Sobrescribe el archivo completo.
    """
    try:
        arch = open("eventos.csv", "wt")  # 'w' sobrescribe, 't' texto
        for clave, datos in eventos.items():
            fecha, salon, turno = clave
            cliente, tipoevento, cantpersonas = datos
            linea = f"{fecha},{salon},{turno},{cliente},{tipoevento},{cantpersonas}\n"
            arch.write(linea)
    except OSError as mensaje:
        print("No se puede grabar el archivo de eventos:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass
#########################################################################################################################################
#########################################################################################################################################
def crear_cuenta():
    Interfaz_CrearCuenta()
    nuevo = input("Ingrese nombre del nuevo usuario: ")
    if nuevo in usuarios:
        print("Ese nombre ya está en uso.")
        return
    clave = input("Ingrese contraseña del nuevo usuario: ")
    usuarios[nuevo] = {"contraseña": clave, "rol": "usuario"}
    print("Cuenta creada exitosamente.")
    registrar_auditoria("admin", f"Creó cuenta para {nuevo}")
    guardar_usuarios_en_csv()
#########################################################################################################################################
def imprimir_usuarios():
    """Muestra la lista de usuarios y oculta la contraseña."""
    Interfaz_ImprimirUsuarios()
    for nombre in sorted(usuarios):
        clave = usuarios[nombre]["contraseña"]
        rol = usuarios[nombre]["rol"]
        print(f"Usuario: {nombre:<15} | Contraseña: {'*' * len(clave):<10} | Rol: {rol}")
#########################################################################################################################################
#########################################################################################################################################
def buscar_usuario():
    """Permite buscar si un usuario existe en el sistema."""
    Interfaz_BuscarUsuario()
    try:
        nombre = input("Ingrese el nombre del usuario a buscar: ")
        if nombre in usuarios:
            print("El usuario existe.")
        else:
            print("El usuario NO existe.")
    except Exception as e:
        print(f"Error al buscar usuario: {str(e)}")
#########################################################################################################################################
#########################################################################################################################################
def eliminar_cuenta():
    Interfaz_EliminarCuenta()
    nombre = input("Ingrese el nombre del usuario que desea eliminar: ")
    if nombre == "admin":
        print("No se puede eliminar el usuario administrador.")
        return
    if nombre in usuarios:
        del usuarios[nombre]
        print("Usuario eliminado correctamente.")
        registrar_auditoria("admin", f"Eliminó cuenta de {nombre}")
        guardar_usuarios_en_csv()
    else:
        print("El usuario no existe.")

#########################################################################################################################################
def registrar_auditoria(usuario, accion):
    """
    Registra una acción en el archivo de auditoría con fecha y hora.
    
    Parámetros:
    usuario (str): Nombre del usuario que realiza la acción.
    accion (str): Descripción de la acción realizada.
    """
    try:
        arch = open("auditoria.txt", "at")  # 'a' para agregar, 't' para modo texto
        ahora = datetime.now()
        fecha = ahora.strftime("%Y-%m-%d")
        hora = ahora.strftime("%H:%M:%S")
        linea = f"{fecha},{hora},{usuario},{accion}\n"
        arch.write(linea)
    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass
#########################################################################################################################################
def ver_auditoria():
    """
    Muestra el contenido del archivo de auditoría. Solo el administrador accede.
    """
    Auditoria_interfaz()
    try:
        archivo = open("auditoria.txt", "rt")
        for linea in archivo:
            print(linea.strip())
    except FileNotFoundError:
        print("El archivo de auditoría no existe aún.")
    except OSError as mensaje:
        print("No se pudo abrir el archivo de auditoría:", mensaje)
    finally:
        try:
            archivo.close()
        except NameError:
            pass
#########################################################################################################################################
#########################################################################################################################################
def menu_admin():
    while True:
        Interfaz_MenuAdministrador()
        try:
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                crear_cuenta()
                registrar_auditoria("admin", "Creó una nueva cuenta")
            elif opcion == "2":
                eliminar_cuenta()
                registrar_auditoria("admin", "Eliminó una cuenta")
            elif opcion == "3":
                imprimir_usuarios()
            elif opcion == "4":
                buscar_usuario()
            elif opcion == "5":
                ver_auditoria()
            elif opcion == "6":
                print("Cierre de sesión del administrador.")
                registrar_auditoria("admin", "Cerró sesión")
                break
            else:
                print("Opción inválida.")
        except Exception as e:
            print("Error inesperado:", e)
#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################
def agregar_evento(usuario):
    """
    Permite al usuario crear un nuevo evento y lo guarda en el diccionario.
    """
    Interfaz_CrearEvento()
    try:
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        salon = input("Ingrese el nombre del salón: ")
        turno = input("Ingrese el turno (mañana/tarde/noche): ")
        tipoevento = input("Ingrese el tipo de evento (cumpleaños, casamiento, etc.): ")
        cantpersonas = input("Ingrese la cantidad estimada de personas: ")

        clave = (fecha, salon, turno)
        if clave in eventos:
            print("Ya existe un evento registrado para esa fecha, salón y turno.")
            return

        eventos[clave] = [usuario, tipoevento, cantpersonas]
        print("Evento agregado correctamente.")
        registrar_auditoria(usuario, f"Agregó un evento en {salon} el {fecha} - {turno}")
        guardar_eventos_en_csv()

    except Exception as e:
        print("Error al crear el evento:", e)
#########################################################################################################################################
def ver_eventos(usuario):
    """
    Muestra todos los eventos registrados por un usuario específico.
    """
    Interfaz_MisEventos()
    tiene_eventos = False
    for clave, datos in eventos.items():
        if datos[0] == usuario:
            fecha, salon, turno = clave
            cliente, tipoevento, cantpersonas = datos
            print(f"{fecha} | {salon} | {turno} | {tipoevento} | {cantpersonas} personas")
            tiene_eventos = True
    if not tiene_eventos:
        print("No tenés eventos registrados.")
#########################################################################################################################################
def eliminar_evento(usuario):
    """
    Permite al usuario eliminar un evento que haya registrado.
    """
    Interfaz_EliminarEvento()
    try:
        fecha = input("Ingrese la fecha del evento a eliminar (YYYY-MM-DD): ")
        salon = input("Ingrese el salón: ")
        turno = input("Ingrese el turno: ")

        clave = (fecha, salon, turno)
        if clave in eventos:
            if eventos[clave][0] != usuario:
                print("No puedes eliminar eventos que no te pertenecen.")
                return
            del eventos[clave]
            print("Evento eliminado correctamente.")
            registrar_auditoria(usuario, f"Eliminó un evento en {salon} el {fecha} - {turno}")
            guardar_eventos_en_csv()
        else:
            print("No existe un evento registrado con esos datos.")
    except Exception as e:
        print("Error al eliminar el evento:", e)
#########################################################################################################################################
#########################################################################################################################################
def menu_eventos(usuario):
    while True:
        Interfaz_MenuEvento()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_evento(usuario)
        elif opcion == "2":
            ver_eventos(usuario)
        elif opcion == "3":
            eliminar_evento(usuario)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
#########################################################################################################################################
#########################################################################################################################################
def modificar_datos_personales(usuario):
    Interfaz_ModificarDatos()
    try:
        actual = input("Ingrese su contraseña actual: ")
        if usuarios[usuario]["contraseña"] != actual:
            print("Contraseña incorrecta. No se realizaron cambios.")
            return

        nueva = input("Ingrese nueva contraseña: ")
        confirmacion = input("Confirme nueva contraseña: ")

        if nueva != confirmacion:
            print("Las contraseñas no coinciden. Intente nuevamente.")
            return

        usuarios[usuario]["contraseña"] = nueva
        print("Contraseña actualizada correctamente.")
        registrar_auditoria(usuario, "Modificó su contraseña")
        guardar_usuarios_en_csv()

    except KeyError:
        print("Error al acceder a los datos del usuario.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
#########################################################################################################################################
def menu_usuario(nombre):
    while True:
        Interfaz_MenuUsuario()
        try:
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                modificar_datos_personales(nombre)
            elif opcion == "2":
                menu_eventos(nombre)
            elif opcion == "3":
                print("Cierre de sesión del usuario.")
                registrar_auditoria(nombre, "Cerró sesión")
                break
            else:
                print("Opción inválida.")
        except Exception as e:
            print("Error inesperado:", e)
#########################################################################################################################################
def iniciar_sesion():
    """Solicita credenciales y valida contra el diccionario de usuarios. Devuelve el nombre del usuario si es válido."""
    intentos = 0
    while intentos < 3:
        try:
            nombre = input("Nombre de usuario: ")
            clave = input("Contraseña: ")
            if nombre in usuarios and usuarios[nombre]["contraseña"] == clave:
                print("Inicio de sesión exitoso.")
                registrar_auditoria(nombre, "Inicio de sesión")
                return nombre
            else:
                intentos += 1
                print("Credenciales incorrectas. Intentos restantes:", 3 - intentos)
        except KeyError:
            print("Error al acceder a los datos del usuario.")
            intentos += 1
    print("Demasiados intentos fallidos. Sesión bloqueada.")
    return None
# =====================================================================================================================================
#                                                      PROGRAMA PRINCIPAL                                                             |
# =====================================================================================================================================
cargar_usuarios_desde_csv()
cargar_eventos_desde_csv()
while True:
    menu_interactivo()
    try:
        entrada = input("Ingrese una opción: ")
        if entrada == "1":
            usuario_actual = iniciar_sesion()
            if usuario_actual and usuarios[usuario_actual]["rol"] == "admin":
                menu_admin()
            else:
                menu_usuario(usuario_actual)
        elif entrada == "-1":
            print("USTED HA FINALIZADO EL PROGRAMA. HASTA LUEGO.")
            break
        else:
            print("Opción inválida.")
    except:
        print("Error inesperado en el menú principal.")
#########################################################################################################################################
#########################################################################################################################################



















