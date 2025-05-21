# Estructura actualizada: diccionario con contraseña y rol
usuarios = {
    "admin": {"contraseña": "1234", "rol": "admin"},
    "Martin": {"contraseña": "123", "rol": "usuario"},
    "luca": {"contraseña": "1234", "rol": "usuario"},
    "Pedro": {"contraseña": "2210", "rol": "usuario"},
    "Lucia": {"contraseña": "123456", "rol": "usuario"},
    "Tomas": {"contraseña": "1234567", "rol": "usuario"}
}
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
#########################################################################################################################################
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
                return nombre
            else:
                intentos += 1
                print("Credenciales incorrectas. Intentos restantes:", 3 - intentos)
        except KeyError:
            print("Error al acceder a los datos del usuario.")
            intentos += 1
    print("Demasiados intentos fallidos. Sesión bloqueada.")
    return None
#########################################################################################################################################
#########################################################################################################################################
def crear_cuenta():
    """Crea un nuevo usuario (solo admin)."""
    Interfaz_CrearCuenta()
    nuevo = input("Ingrese nombre del nuevo usuario: ")
    if nuevo in usuarios:
        print("Ese nombre ya está en uso.")
        return
    clave = input("Ingrese contraseña del nuevo usuario: ")
    usuarios[nuevo] = {"contraseña": clave, "rol": "usuario"}
    print("Cuenta creada exitosamente.")
#########################################################################################################################################
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
    """Elimina un usuario existente, excepto si es el admin."""
    Interfaz_EliminarCuenta()
    nombre = input("Ingrese el nombre del usuario que desea eliminar: ")
    
    if nombre == "admin":
        print("No se puede eliminar el usuario administrador.")
        return

    if nombre in usuarios:
        del usuarios[nombre]
        print("Usuario eliminado correctamente.")
    else:
        print("El usuario no existe.")
#########################################################################################################################################
#########################################################################################################################################
from datetime import datetime

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
#########################################################################################################################################
def ver_auditoria():
    """
    Muestra el contenido del archivo de auditoría. Solo el administrador accede.
    """
    print("=========================================================================================================")
    print("|                                          AUDITORÍA DEL SISTEMA                                       |")
    print("=========================================================================================================")
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
def ver_auditoria():
    """
    Muestra el contenido del archivo de auditoría.
    Solo debe ser usada por el administrador.
    """
    Interfaz_BuscarUsuario()  # Reutilizo la interfaz, o si querés creo una nueva específica

    try:
        archivo = open("auditoria.txt", "rt")
        print("===== REGISTRO DE AUDITORÍA =====")
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
                # Aquí también se puede registrar si eliminó a alguien
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
def Interfaz_ModificarDatos():
    print("=========================================================================================================")
    print("|                               MODIFICAR DATOS PERSONALES - USUARIO                                    |")
    print("=========================================================================================================")
#########################################################################################################################################
#########################################################################################################################################
def modificar_datos_personales(usuario):
    """
    Permite al usuario modificar su contraseña.
    
    Parámetros:
    usuario (str): Nombre del usuario autenticado.
    """
    print("=========================================================================================================")
    print("|                                 MODIFICAR DATOS PERSONALES                                           |")
    print("=========================================================================================================")

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

    except KeyError:
        print("Error al acceder a los datos del usuario.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
#########################################################################################################################################
#########################################################################################################################################
def Interfaz_MenuUsuario():
    print("=========================================================================================================")
    print("|                                    MENÚ USUARIO - GESTIÓN PERSONAL                                    |")
    print("=========================================================================================================")
    print("|                               1. Modificar mis datos personales                                       |")
    print("|                               2. Gestor de eventos (crear/ver/eliminar)                               |")
    print("|                               3. Cerrar sesión                                                        |")
    print("=========================================================================================================")

#########################################################################################################################################
#########################################################################################################################################
def menu_usuario(nombre):
    while True:
        Interfaz_MenuUsuario()
        try:
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                modificar_datos_personales(nombre)
            elif opcion == "2":
                menu_eventos(nombre)  # Lo desarrollaremos ahora
            elif opcion == "3":
                print("Cierre de sesión del usuario.")
                registrar_auditoria(nombre, "Cerró sesión")
                break
            else:
                print("Opción inválida.")
        except Exception as e:
            print("Error inesperado:", e)
#########################################################################################################################################
#########################################################################################################################################
eventos = {}
#########################################################################################################################################
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
def agregar_evento():
    """
    Permite al usuario crear un nuevo evento y lo guarda en el diccionario.
    """
    print("===== CREAR NUEVO EVENTO =====")
    try:
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        salon = input("Ingrese el nombre del salón: ")
        turno = input("Ingrese el turno (mañana/tarde/noche): ")
        cliente = input("Ingrese nombre del cliente: ")
        tipoevento = input("Ingrese el tipo de evento (cumpleaños, casamiento, etc.): ")
        cantpersonas = input("Ingrese la cantidad estimada de personas: ")

        clave = (fecha, salon, turno)
        if clave in eventos:
            print("Ya existe un evento registrado para esa fecha, salón y turno.")
            return

        eventos[clave] = [cliente, tipoevento, cantpersonas]
        print("Evento agregado correctamente.")
        registrar_auditoria(cliente, f"Agregó un evento en {salon} el {fecha} - {turno}")
        guardar_eventos_en_csv()

    except Exception as e:
        print("Error al crear el evento:", e)
#########################################################################################################################################
#########################################################################################################################################
def ver_eventos(usuario):
    """
    Muestra todos los eventos registrados por un usuario específico.
    """
    print("===== MIS EVENTOS =====")
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
#########################################################################################################################################
def eliminar_evento(usuario):
    """
    Permite al usuario eliminar un evento que haya registrado.
    """
    print("===== ELIMINAR EVENTO =====")
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
        print("=========================================================================================================")
        print("|                                      GESTOR DE EVENTOS                                                |")
        print("=========================================================================================================")
        print("|                             1. Crear nuevo evento                                                     |")
        print("|                             2. Ver mis eventos                                                        |")
        print("|                             3. Eliminar un evento                                                     |")
        print("|                             4. Volver al menú anterior                                                |")
        print("=========================================================================================================")
        
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
def agregar_evento(usuario):
    """
    Permite al usuario crear un nuevo evento y lo guarda en el diccionario.
    """
    print("===== CREAR NUEVO EVENTO =====")
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
#########################################################################################################################################
#########################################################################################################################################
#########################################################################################################################################
# ============================
#        PROGRAMA PRINCIPAL
# ============================
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



















