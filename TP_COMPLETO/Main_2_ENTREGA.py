from datetime import datetime
import json

# — Constantes —
SALONES = ["Palermo","Puerto Madero","Nordelta","San Telmo","Recoleta"]
TURNOS  = ["Mañana","Tarde","Noche"]
TIPOS_DE_EVENTOS = ["Fiesta de egresados","Casamiento","Cumpleaños","Despedida de soltero","Evento empresarial","Conferencia"]
ATRIBUTOS_DE_EVENTOS = ["Fecha", "Salon", "Turno", "Cliente", "Tipo de evento", "Cantidad de personas", "Servicios"]
USUARIOS = "usuarios.json"
EVENTOS = "eventos.json"
SERVICIOS = "servicios.json"
FACTURAS = "factura.txt"
AUDITORIA = "auditoria.txt"
# Estructura actualizada: diccionario con contraseña y rol
usuarios = {
    #"admin": {"contraseña": "1234", "rol": "admin"},
}

#Creamos el diccionario Calendario
calendario = {}

#Creamos el diccionario con los servicios estaticos disponibles
servicios_disponibles = {}

# — Capacidades máximas por salón (entre 20 y 1000) —
capacidades_salones = {
    "Palermo":        300,
    "Puerto Madero":  700,
    "Nordelta":       150,
    "San Telmo":       80,
    "Recoleta":       500
}

#=================================================== ZONA DE INTERFACEZ ===========================================================
def interfaz_CrearCuenta():
    print("=========================================================================================================")
    print("|                                        CREAR CUENTA (Solo Admin)                                      |")
    print("=========================================================================================================")
def interfaz_ImprimirUsuarios():
    print("=========================================================================================================")
    print("|                                       LISTA DE USUARIOS                                               |")
    print("=========================================================================================================")
def interfaz_BuscarUsuario():
    print("=========================================================================================================")
    print("|                                         BUSCAR USUARIO                                                |")
    print("=========================================================================================================")
def interfaz_EliminarCuenta():
    print("=========================================================================================================")
    print("|                                        ELIMINAR CUENTA (Solo Admin)                                   |")
    print("=========================================================================================================")
def interfaz_MenuAdministrador():
    print("=========================================================================================================")
    print("|                             MENÚ ADMINISTRADOR - Gestión de Usuarios                                  |")
    print("=========================================================================================================")
    print("|                                   1. Crear cuenta                                                     |")
    print("|                                   2. Eliminar cuenta                                                  |")
    print("|                                   3. Ver usuarios                                                     |")
    print("|                                   4. Buscar usuario                                                   |")
    print("|                                   5. Ver Auditoria                                                    |")
    print("|                                   6. Gestionar servicios                                              |")
    print("|                                   7. Cerrar sesión                                                    |")
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
def auditoria_interfaz():
    print("=========================================================================================================")
    print("|                                          AUDITORÍA DEL SISTEMA                                        |")
    print("=========================================================================================================")
def interfaz_ModificarDatos():
    print("=========================================================================================================")
    print("|                               MODIFICAR DATOS PERSONALES - USUARIO                                    |")
    print("=========================================================================================================")
def interfaz_MenuUsuario():
    print("=========================================================================================================")
    print("|                                    MENÚ USUARIO - GESTIÓN PERSONAL                                    |")
    print("=========================================================================================================")
    print("|                               1. Modificar mis datos personales                                       |")
    print("|                               2. Gestor de eventos                                                    |")
    print("|                               3. Cerrar sesión                                                        |")
    print("=========================================================================================================")
def interfaz_MisEventos():
    print("=========================================================================================================")
    print("|                                            MIS EVENTOS                                                |")
    print("=========================================================================================================")
def interfaz_EliminarEvento():
    print("=========================================================================================================")
    print("|                                         ELIMINAR EVENTO                                               |")
    print("=========================================================================================================")
def interfaz_mostrar_servicios():
    print("=========================================================================================================")
    print("|                                         VER SERVICIOS DISPONIBLES                                     |")
    print("=========================================================================================================")
def interfaz_MenuEvento():
    print("=========================================================================================================")
    print("|                                      GESTOR DE EVENTOS                                                |")
    print("=========================================================================================================")
    print("|                             1. Crear un evento                                                        |")
    print("|                             2. Ver todos los eventos                                                  |")
    print("|                             3. Eliminar un evento                                                     |")
    print("|                             4. Mostrar Calendario                                                     |")
    print("|                             5. Buscar Evento                                                          |")
    print("|                             6. Editar Evento                                                          |")  
    print("=========================================================================================================")
    print("|                             7. Volver al menú anterior                                                |")
    print("=========================================================================================================")
def interfaz_CrearEvento():
    print("=========================================================================================================")
    print("|                                           CREAR EVENTO                                                |")
    print("=========================================================================================================")

def interfaz_salir_programa():
    print("=========================================================================================================")
    print("|                                     Gracias por usar el programa                                      |")
    print("|                                            ¡Hasta pronto!                                             |")
    print("=========================================================================================================")
    
def interfaz_ver_evento():
    print("=========================================================================================================")
    print("|                                         VISUALIZAR EVENTO                                             |")
    print("=========================================================================================================")

def interfaz_mostrar_calendario():
    print("=========================================================================================================")
    print("|                                         MOSTRAR CALENDARIO                                            |")
    print("=========================================================================================================")

def interfaz_buscar_evento():
    print("=========================================================================================================")
    print("|                                         BUSCAR EVENTO                                                 |")
    print("=========================================================================================================")

def interfaz_salir_gestor_eventos():
    print("=========================================================================================================")
    print("|                               Saliendo del gestor de eventos....                                      |")
    print("=========================================================================================================")
    
def interfaz_tipo_evento():
    print("=========================================================================================================")
    print("|                                      TIPO DE EVENTO                                                   |")
    print("=========================================================================================================")
    print("|                             1. Fiesta de egresados                                                    |")
    print("|                             2. Casamiento                                                             |")
    print("|                             3. Cumpleaños                                                           |")
    print("|                             4. Despedida de soltero                                                   |")
    print("|                             5. Evento Empresarial                                                     |")
    print("|                             6. Conferencia                                                            |")
    print("=========================================================================================================")
    print("|                             0. Cancelar                                                               |")
    print("=========================================================================================================")
    
def interfaz_tipo_salon():
    print("=========================================================================================================")
    print("|                                      SELECCIONE SALON                                                 |")
    print("=========================================================================================================")
    print("|                             1. Palermo       | capacidad: 300 personas                                |")
    print("|                             2. Puerto Madero | capacidad: 700 personas                                |")
    print("|                             3. Nordelta      | capacidad: 150 personas                                |")
    print("|                             4. San Telmo     | capacidad: 80  personas                                 |")
    print("|                             5. Recoleta:     | capacidad: 500 personas                                 |")
    print("=========================================================================================================")
    print("|                             0. Cancelar                                                               |")
    print("=========================================================================================================")
    
def interfaz_tipo_turno():
    print("=========================================================================================================")
    print("|                                      SELECCIONE TURNO                                                 |")
    print("=========================================================================================================")
    print("|                             1. Mañana                                                                 |")
    print("|                             2. Tarde                                                                  |")
    print("|                             3. Noche                                                                  |")
    print("=========================================================================================================")
    print("|                             0. Cancelar                                                               |")
    print("=========================================================================================================")
def interfazValorAModificar():
    print("=========================================================================================================")
    print("|                                      SELECCIONE VALOR A MODIFICAR                                     |")
    print("=========================================================================================================")
    print("|                             1. Fecha                                                                  |")
    print("|                             2. Salon                                                                  |")
    print("|                             3. Turno                                                                  |")
    print("|                             4. Cliente                                                                |")
    print("|                             5. Tipo de evento                                                         |")
    print("|                             6. Cantidad de personas                                                   |")
    print("|                             7. Servicios                                                              |")
    print("=========================================================================================================")
    print("|                             0. Cancelar                                                               |")
    print("=========================================================================================================")

def interfaz_MenuServicios():
    print("=========================================================================================================")
    print("|                                MENÚ DE GESTIÓN DE SERVICIOS                                           |")
    print("=========================================================================================================")
    print("|                             1. Ver servicios disponibles                                              |")
    print("|                             2. Agregar servicio                                                       |")
    print("|                             3. Eliminar servicio                                                      |")
    print("|                             4. Editar servicio                                                        |")
    print("=========================================================================================================")
    print("|                             0. Volver al menú anterior                                                |")
    print("=========================================================================================================")

def interfazAtributoDeServicioAModificar():
    print("=========================================================================================================")
    print("|                                    SELECCIONE ATRIBUTO A MODIFICAR                                    |")
    print("=========================================================================================================")
    print("|                             1. Nombre                                                                 |")
    print("|                             2. Tipo                                                                   |")
    print("|                             3. Precio                                                                 |")
    print("=========================================================================================================")
    print("|                             0. Cancelar                                                               |")
    print("=========================================================================================================")

def interfazTipoServicio():
    print("=========================================================================================================")
    print("|                                      SELECCIONE TIPO DE SERVICIO                                      |")
    print("=========================================================================================================")
    print("|                             1. Fijo                                                                   |")
    print("|                             2. Variable                                                               |")
    print("=========================================================================================================")
    print("|                             0. Cancelar                                                               |")
    print("=========================================================================================================")
#=================================================== ZONA DE JSON ==================================================================
def cargar_desde_json(nombre_archivo):
    """
        Intenta abrir y procesar un archivo JSON
    """
    try:
        archivo = open(nombre_archivo, "r",encoding="utf-8") # Abre el archivo en modo lectura ("r")
        datos = json.load(archivo) # Carga el contenido JSON del archivo
        reconstruido = {} # Se crea un nuevo diccionario vacío donde se reconstruirán las claves
        for k, v in datos.items(): # Recorre cada par clave-valor del diccionario original
            try:
                clave = json.loads(k) # Intenta decodificar la clave desde una cadena JSON
                if isinstance(clave, list): # verifica si un objeto es de un tipo específico
                    clave = tuple(clave) # Si la clave es una lista, se convierte en tupla (porque las listas no pueden ser claves en diccionarios)
                reconstruido[clave] = v # Asigna el valor al nuevo diccionario
            except json.JSONDecodeError: # Si ocurre un error al intentar decodificar la clave (no era JSON válido)
                reconstruido[k] = v
        return reconstruido
    except FileNotFoundError: # Si el archivo no existe
        print(f"Archivo '{nombre_archivo}' no encontrado. Se usará un diccionario vacío.")
        return {}
    except json.JSONDecodeError as error: # Si ocurre un error al decodificar el JSON del archivo
        print(f"Error al decodificar JSON en '{nombre_archivo}':", error)
        return {}
    except OSError as error: # Si ocurre cualquier otro error relacionado con el sistema operativo
        print(f"Error al leer {nombre_archivo}:", error)
        return {}
    finally:
        try:
            archivo.close() # Cierra el archivo
        except NameError:
            pass
#===================================================================================================================================
def guardar_en_json(nombre_archivo, diccionario):
    """
        guarda el contenido del diccionario en un archivo JSON
    """
    try:
        # Abre el archivo en modo escritura ("w"), Si el archivo ya existe, su contenido será sobrescrito
        archivo = open(nombre_archivo, "w", encoding="utf-8")
        # Se crea un nuevo diccionario en el que:
        #   - Cada clave que sea una tupla se convierte a string JSON con json.dumps (porque JSON no acepta tuplas como claves)
        #   - Las claves que no sean tuplas se dejan como están
        #   - Los valores se mantienen sin cambios
        serializado = {json.dumps(k) if isinstance(k, tuple) else k: v for k, v in diccionario.items()}
        json.dump(serializado, archivo)
        # Se guarda el diccionario serializado en el archivo en formato JSON
    except OSError as error: # Si ocurre un error del sistema al intentar abrir o escribir el archivo
        print(f"No se pudo guardar en {nombre_archivo}:", error)
    finally:
        try:
            archivo.close() # Cierra el archivo
        except NameError:
            pass
#===================================================================================================================================
def crearServiciosPredefinidos(servicios_disponibles):
    """
    Crea servicios por defecto para el sistema si no hay servicios cargados.
    Agrega servicios por defecto
    """
    servicios_disponibles["Catering"] = {"tipo": "variable", "precio": 5000}
    servicios_disponibles["Bartender"] = {"tipo": "fijo", "precio": 25000}
    servicios_disponibles["Decoración básica"] = {"tipo": "fijo", "precio": 80000}
    servicios_disponibles["Pack sonido e iluminación"] = {"tipo": "fijo", "precio": 80000}
    servicios_disponibles["DJ"] = {"tipo": "fijo", "precio": 50000}
    servicios_disponibles["Fotógrafo"] = {"tipo": "fijo", "precio": 20000}

    guardar_en_json(SERVICIOS, servicios_disponibles)  # Guarda los servicios por defecto en el archivo JSON.
#===================================================================================================================================
def guardar_facturacion(clave,evento):
    fecha, salon, turno = clave # Desempaqueta la tupla 'clave' en las variables fecha, salón y turno
    cliente = evento["cliente"] # Extrae del diccionario 'evento' el nombre del cliente
    tipo = evento["tipo"] # Extrae el tipo de evento (Ej: cumpleaños, casamiento, etc.)
    cant = evento["cant_personas"] # Extrae la cantidad de personas que asistirán al evento
    servicios = evento["servicios"] # Extrae la lista de servicios contratados para el evento
    precios = evento["precios"] # Extrae la lista de precios correspondientes a los servicios contratados
    
    
    # 1) Calcular subtotal
    subtotal = 0.0
    for p in precios:
        subtotal += p

    # 2) Definir alícuotas (puedes ajustar según jurisdicción)
    alicuota_iva = 0.21         # IVA 21%
    alicuota_iibb = 0.03        # Ingresos Brutos 3%
    alicuota_sellos = 0.01      # Impuesto de Sellos 1%

    # 3) Calcular montos de impuestos
    monto_iva = round(subtotal * alicuota_iva, 2)
    monto_iibb = round(subtotal * alicuota_iibb, 2)
    monto_sellos = round(subtotal * alicuota_sellos, 2)

    # 4) Total con impuestos
    total_con_impuestos = round(subtotal + monto_iva + monto_iibb + monto_sellos, 2)
    
    try:
        arch = open(FACTURAS, "at", encoding="utf-8")

        arch.write(f"FACTURA - Evento: {tipo}\n")
        arch.write(f"Fecha: {fecha}     Salón: {salon}     Turno: {turno}\n")
        arch.write(f"Cliente: {cliente}     Cant. personas: {cant}\n")
        arch.write("-" * 60 + "\n\n")

     
        arch.write("SERVICIOS CONTRATADOS:\n")
        arch.write(f"{'Descripción':30} {'Precio':>15}\n")
        arch.write("-" * 47 + "\n")
        # Recorremos por índice: de 0 a len(servicios)-1
        for i in range(len(servicios)):
            desc = servicios[i]
            precio = precios[i]
            # Alineamos: descripción a la izquierda 30 cols, precio a la derecha 15 cols
            arch.write(f"{desc:30} {precio:>15.2f}\n")
        arch.write("-" * 47 + "\n\n")

        # --- 6) Escribir totales ---
       # --- Mostrar precios con y sin impuestos ---
        arch.write("PRECIOS:\n")
        # Precio sin impuestos (subtotal)
        arch.write(f"{'Subtotal (sin impuestos):':30} {subtotal:>15.2f}\n")
        # IVA
        arch.write(f"{'IVA 21%:':30} {monto_iva:>15.2f}\n")
        # Ingresos Brutos
        arch.write(f"{'Ingresos Brutos 3%:':30} {monto_iibb:>15.2f}\n")
        # Impuesto de Sellos
        arch.write(f"{'Impuesto de Sellos 1%:':30} {monto_sellos:>15.2f}\n")
        arch.write("-" * 47 + "\n")
        # Total con impuestos
        arch.write(f"{'TOTAL A PAGAR (c/ impuestos):':30} {total_con_impuestos:>15.2f}\n")
        arch.write("\n" + "-" * 60 + "\n")
        arch.write("Gracias por elegirnos. ¡Que disfrute su evento!\n")

        
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:", mensaje)
    except OSError as mensaje:
        print("No se puede leer el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass    
#========================================= ZONA DE FUNCIONES GESTOR DE USUARIO ====================================================
def crear_cuenta(usuarios):
    """
        Función para crear una nueva cuenta de usuario y guardarla
    """
    try:
        interfaz_CrearCuenta()
        nuevo = input("Ingrese nombre del nuevo usuario: ")  # Solicita el nombre del nuevo usuario
        if nuevo in usuarios:  # Verifica si el nombre ya existe
            print("Ese nombre ya está en uso.")
            return usuarios
        clave = input("Ingrese contraseña del nuevo usuario: ")  # Solicita una contraseña
        usuarios[nuevo] = {"contraseña": clave, "rol": "usuario"}  # Agrega al nuevo usuario
        print("Cuenta creada exitosamente.")
        registrar_auditoria("admin", f"Creó cuenta para {nuevo}")  # Registra la acción
        guardar_en_json(USUARIOS, usuarios)  # Guarda los cambios
        return usuarios  # Devuelve el diccionario actualizado
    except Exception as e:
        print("Ocurrió un error al crear la cuenta:", e)
        return usuarios
#==================================================================================================#    
def imprimir_usuarios(usuarios):
    """
        Muestra la lista de usuarios y oculta la contraseña.
    """
    interfaz_ImprimirUsuarios()
    for nombre in sorted(usuarios): # Recorre los nombres de usuarios ordenados alfabéticamente
        clave = usuarios[nombre]["contraseña"] # Obtiene la contraseña del usuario actual
        rol = usuarios[nombre]["rol"] # Obtiene el rol del usuario actual
        print(f"Usuario: {nombre:<15} | Contraseña: {'*' * len(clave):<10} | Rol: {rol}")
#==================================================================================================#     
def buscar_usuario(usuarios):
    """
        Permite buscar si un usuario existe en el sistema.
    """
    interfaz_BuscarUsuario()
    try:
        nombre = input("Ingrese el nombre del usuario a buscar: ")
        if nombre in usuarios: # Verifica si el nombre ingresado está en el diccionario de usuarios
            print("El usuario existe.")
        else:
            print("El usuario NO existe.")
    except Exception as e:
        print(f"Error al buscar usuario: {str(e)}")
#==================================================================================================#        
def eliminar_cuenta(usuarios):
    """
        Función que permite eliminar un usuario del sistema
    """
    try:
        interfaz_EliminarCuenta()
        nombre = input("Ingrese el nombre del usuario que desea eliminar: ")
        if nombre == "admin":
            print("No se puede eliminar el usuario administrador.")
            return usuarios  # Retorna sin cambios
        if nombre in usuarios: # Verifica si el nombre ingresado existe 
            usuarios.pop(nombre)
            print("Usuario eliminado correctamente.")
            registrar_auditoria("admin", f"Eliminó cuenta de {nombre}") # Registra la acción
            guardar_en_json(USUARIOS, usuarios) # Guarda los cambios
        else:
            print("El usuario no existe.")
        return usuarios # Devuelve el diccionario actualizado
    except Exception as e:
        print("Ocurrió un error al eliminar la cuenta:", e)
        return usuarios 
#=================================================== ZONA DE AUDITORIA ===========================================================
def registrar_auditoria(usuario, accion):
    """
        Registra una acción en el archivo de auditoría con fecha y hora.
    
        Parámetros:
            usuario (str): Nombre del usuario que realiza la acción.
            accion (str): Descripción de la acción realizada.
    """
    try:
        arch = open(AUDITORIA, "at",encoding="utf-8")  # 'a' para agregar, 't' para modo texto
        # Abre (o crea) el archivo 'auditoria.txt' en modo de agregar texto al final del archivo.
        # Esto evita sobrescribir el contenido anterior y asegura que cada acción quede registrada.
        
        ahora = datetime.now() # Obtiene la fecha y hora actual del sistema
        fecha = ahora.strftime("%Y-%m-%d") # Formatea la fecha actual en el formato año-mes-día (ej: 2025-06-01)
        hora = ahora.strftime("%H:%M:%S")  # Formatea la hora actual en formato de 24 horas (ej: 14:30:15)
        linea = f"{fecha},{hora},{usuario},{accion}\n"
        arch.write(linea) # Escribe la línea en el archivo de auditoría
    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)
    finally:
        try:
            arch.close() # Cierra el archivo
        except NameError:
            pass
#==================================================================================================#
def ver_auditoria():
    """
        Muestra el contenido del archivo de auditoría. Solo el administrador accede.
    """
    auditoria_interfaz()
    try:
        archivo = open(AUDITORIA, "rt",encoding="utf-8") # archivo 'auditoria.txt' en modo lectura de texto ('rt').
        for linea in archivo:
            print(linea.strip()) # Recorre cada línea del archivo y la imprime eliminando espacios en blanco o saltos de línea.
    except FileNotFoundError: # Captura el error si el archivo no existe.
        print("El archivo de auditoría no existe aún.")
    except OSError as mensaje:
        print("No se pudo abrir el archivo de auditoría:", mensaje)
    finally:
        try:
            archivo.close() # Cierra el archivo
        except NameError:
            pass
#=================================================== ZONA DE FUNCION INICIO DE SESION ===========================================================
def iniciar_sesion(usuarios):
    """
        Esta función permite a un usuario autenticarse ingresando su nombre y contraseña.
        Si las credenciales son correctas, devuelve el nombre del usuario. Si falla 3 veces, retorna None.
    """
    intentos = 0 # contador para llevar el número de intentos fallidos de inicio de sesión.
    while intentos < 3: # 3 intentos de autenticación.
        try:
            nombre = input("Nombre de usuario: ")
            clave = input("Contraseña: ")
            if nombre in usuarios and usuarios[nombre]["contraseña"] == clave: # Verifica que el nombre de usuario exista y que la contraseña coincida.
                print("Inicio de sesión exitoso.")
                registrar_auditoria(nombre, "Inicio de sesión") # Registra la acción de inicio de sesión en el archivo de auditoría.
                return nombre
            else:
                intentos += 1 # Si las credenciales son incorrectas, incrementa el contador de intentos.
                print("Credenciales incorrectas. Intentos restantes:", 3 - intentos)
        except KeyError:
            print("Error al acceder a los datos del usuario.")
            intentos += 1 # Incrementa el contador de intentos incluso si hubo una excepción.
    print("Demasiados intentos fallidos. Sesión bloqueada.")
    return None # Retorna None indicando que no se pudo iniciar sesión correctamente.
#======================================== ZONA DE FUNCION MODIFICAR DATOS PERSONALES ==================================================
def modificar_datos_personales(nombre, usuarios):
    """
        Esta función permite a un usuario cambiar su contraseña,
        verificando primero que su contraseña actual sea correcta.
    """
    interfaz_ModificarDatos()
    try:
        actual = input("Ingrese su contraseña actual: ")
        if usuarios[nombre]["contraseña"] != actual: # Compara la contraseña ingresada con la que está registrada en el sistema.
            print("Contraseña incorrecta. No se realizaron cambios.")
            return
        nueva = input("Ingrese nueva contraseña: ")
        confirmacion = input("Confirme nueva contraseña: ")
        if nueva != confirmacion: # Verifica que ambas contraseñas ingresadas coincidan.
            print("Las contraseñas no coinciden. Intente nuevamente.")
            return
        usuarios[nombre]["contraseña"] = nueva # Actualiza la contraseña del usuario en el diccionario.
        print("Contraseña actualizada correctamente.")
        registrar_auditoria(nombre, "Modificó su contraseña") # Registra la acción en el archivo de auditoría con la fecha y hora correspondiente.
        guardar_en_json(USUARIOS, usuarios) # Guarda los cambios en el archivo JSON persistente que contiene los usuarios.
    except KeyError:
        print("Error al acceder a los datos del usuario.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
#=================================================== ZONA DE MENU ADMIN ===========================================================
def menu_admin(usuarios,servicios_disponibles):
    while True:
        interfaz_MenuAdministrador()
        try:
            opcion = input("Seleccione una opción: ")
            if opcion == "1": # ---------------- CREAR CUENTA ---------------------
                usuarios = crear_cuenta(usuarios)
            elif opcion == "2": # ---------------- ELIMINAR CUENTA ----------------
                usuarios = eliminar_cuenta(usuarios) 
            elif opcion == "3": # ---------------- IMPRIMIR CUENTAS ---------------
                imprimir_usuarios(usuarios)
            elif opcion == "4": # ---------------- BUSCAR CUENTA ------------------
                buscar_usuario(usuarios)
            elif opcion == "5": # ---------------- AUDITORIA ----------------------
                ver_auditoria()
            elif opcion == "6": # ---------------- GESTION SERVICIOS ------------------
                menu_gestion_servicios(servicios_disponibles)
            elif opcion == "7": # ---------------- CIERRE CUENTA ------------------
                print("Cierre de sesión del administrador.")
                registrar_auditoria("admin", "Cerró sesión")
                break
            else:
                print("Opción inválida.")
        except Exception as e:
            print("Error inesperado:", e)
    return usuarios
#=========================================================================================================
def menu_gestion_servicios(servicios_disponibles):
    while True:
        try:
            interfaz_MenuServicios()
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1": # ------------------ MOSTRAR SERVICIOS -------------------
                mostrar_servicios(servicios_disponibles)
            elif opcion == "2": # ------------------ AGREGAR SERVICIO -------------------
                agregar_servicio(servicios_disponibles)
            elif opcion == "3": # ---------------- ELIMINAR SERVICIO ----------------
                eliminar_servicio(servicios_disponibles)
            elif opcion == "4": # ---------------- EDITAR SERVICIO ------------------    
                editar_servicio(servicios_disponibles)
            elif opcion == "0": # ---------------- CIERRE SERVICIOS -----------------
                print("Saliendo del menú de servicios")
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except Exception as e:
            print("Error inesperado:", e)
#=================================================== ZONA DE MENU USUARIO ===========================================================
def menu_usuario(nombre,calendario,usuarios,servicios_disponibles):
    while True:
        interfaz_MenuUsuario()
        try:
            opcion = input("Seleccione una opción: ")
            if opcion == "1": # ---------------- MODIFICAR DATOS -------------------
                modificar_datos_personales(nombre,usuarios)
            elif opcion == "2": # ---------------- MENU EVENTOS --------------------
                menu_eventos(nombre,calendario,servicios_disponibles)
            elif opcion == "3": # ---------------- CIERRE SESION ------------------
                print("Cierre de sesión del usuario.")
                registrar_auditoria(nombre, "Cerró sesión")
                break
            else:
                print("Opción inválida.")
        except Exception as e:
            print("Error inesperado:", e)
#=================================================== ZONA DE MENU EVENTOS ===========================================================
def menu_eventos(usuario,calendario,servicios_disponibles):
    while True:
        interfaz_MenuEvento()
        opcion = input("Seleccione una opción (1-7): ").strip()
        if opcion == "1": # ---------------- CREAR UN EVENTO ---------------------
            agregar_evento(usuario, calendario, servicios_disponibles)
        elif opcion == "2": # ---------------- VER TODOS LOS EVENTOS -------------
            interfaz_ver_evento()
            if calendario:  # si hay eventos
                imprimir_eventos(calendario)
            else:
                print("No hay eventos cargados en el calendario.")
        elif opcion == "3": # ---------------- ELIMINAR UN EVENTO ----------------
            interfaz_EliminarEvento()
            eliminar_evento(usuario,calendario)
        elif opcion == "4": # ---------------- IMPRIMIR EL CALENDARIO -------------
            interfaz_mostrar_calendario()
            while True:
                año_str = input("Ingrese el año a visualizar: ").strip()
                if año_str.isdigit() and 1000 <= int(año_str) <= 9999:
                    año = int(año_str)
                    break
                print("Ingrese un año válido (ej: 2025).")
            mostrarCalendario(año, calendario)
        elif opcion == "5": # ---------------- BUSCAR UN EVENTO -------------
            interfaz_buscar_evento()
            buscarEvento(calendario)
        elif opcion == "6": # ---------------- EDITAR UN EVENTO -------------
            clave, evento = editarEvento(calendario, servicios_disponibles,usuario)
            imprimirEvento(clave, evento)  
        elif opcion == "7": # ---------------- VOLVER AL MENÚ ANTERIOR -------------
            interfaz_salir_gestor_eventos()
            break
        else:
            print("Opción inválida. Intente con un número del 1 al 7.")
#===================================================================================================================================
def agregar_evento(usuario, calendario, servicios_disponibles):
    """
    Permite al usuario crear un nuevo evento y lo guarda en el diccionario.
    """
    try:
        # 1) Ingresar nombre del cliente
        interfaz_CrearEvento()
        cliente = input("Ingrese su nombre: ").strip().title()  # Pide el nombre, lo limpia y capitaliza
        
        # 2) Selección del tipo de evento
        interfaz_tipo_evento() 
        tipo_evento = seleccionar_opciones(TIPOS_DE_EVENTOS)
        if tipo_evento is None:
            return  

        # 3) Ingreso y validación de la fecha del evento
        while True:
            fecha = input("Fecha del evento (YYYY-MM-DD): ").strip()  # Solicita la fecha
            if validarFecha(fecha):  # Verifica si tiene formato correcto y es válida
                break 
            print("Formato inválido. Use YYYY-MM-DD.")

        # 4) Selección del salón
        interfaz_tipo_salon()
        salon = seleccionar_opciones(SALONES)
        if salon is None:
            return

        # 5) Ingreso y validación de la cantidad de personas
        while True:
            val = input("Cantidad de personas: ").strip()  # Solicita la cantidad de asistentes
            if val.isdigit() and int(val) > 0:  # Verifica que sea un número entero positivo
                cant = int(val)  # Convierte a entero y guarda
                break 
            print("Por favor ingrese un número entero positivo.")

        # 6) Validar capacidad máxima del salón elegido
        max_cap = capacidades_salones[salon]  # Obtiene la capacidad máxima del salón
        while cant > max_cap:
            print(f"El salón {salon} admite hasta {max_cap} personas.")
            val = input(f"Ingrese una cantidad ≤ {max_cap}: ").strip()  # Solicita un nuevo número
            if val.isdigit() and 1 <= int(val) <= max_cap:  # Valida el nuevo número
                cant = int(val)
                break
            print("Entrada inválida.")

        # 7) Selección del turno
        interfaz_tipo_turno()
        turno = seleccionar_opciones(TURNOS)
        if turno is None:
            return

        # 8) Construcción del diccionario de servicios personalizados para el evento
        servicios_evento = servicios_disponibles.copy()  # Se hace una copia para no modificar el original
        for servicio, precio in servicios_evento.items(): 
            if precio["tipo"] == "variable":  # Si el servicio es variable (depende de personas)
                servicios_evento[servicio] = precio["precio"] * cant  # Calcula el total por cantidad
            else:
                servicios_evento[servicio] = precio["precio"]  # Si es fijo, mantiene el precio

        # 9) Selección de servicios extra por parte del usuario
        servicios, precios = seleccionar_servicios(servicios_evento)  # Retorna dos listas: nombres y precios
        subtotal = sum(precios)  # Suma los precios para obtener el total sin limpieza
        limpieza = subtotal * 0.05  # Calcula un 5% extra por limpieza postevento
        servicios.append("Limpieza postevento")  # Se agrega este servicio a la lista
        precios.append(limpieza)  # Se agrega el costo de limpieza

        # 10) Registro del evento
        evento = crearEvento(cliente, tipo_evento, cant, servicios, precios)  # Crea el evento con todos los datos
        agregarEventoACalendario(calendario, fecha, salon, turno, evento)  # Guarda el evento en el calendario
        imprimirEvento((fecha, salon, turno), evento)  # Muestra el evento registrado

        guardar_facturacion((fecha, salon, turno), evento)  # Guarda los datos de facturación
        registrar_auditoria(usuario, f"Agregó un evento en {salon} el {fecha} - {turno}")
        guardar_en_json(EVENTOS, calendario)  # Guarda el calendario actualizado en el archivo .json
        
    except Exception as e:
        print("Error al crear el evento:", e)  # Captura e informa cualquier error durante el proceso
#====================================================================================================================================
def crearEvento(cliente, tipoEvento, cant_personas, servicios, precios):
    """
        Crea un evento 
            - se trae los parametros ingresados
            - los agrega al diccionario en cada uno de sus lugares
    """
    return {
        "cliente": cliente,
        "tipo": tipoEvento,
        "cant_personas": cant_personas,
        "servicios": servicios,
        "precios": precios
    }
#===================================================================================================================================
def agregarEventoACalendario(calendario, fecha, salon, turno, evento):
    # Crea una clave única para el evento combinando la fecha, salón y turno en una tupla
    clave = (fecha, salon, turno)
    # Verifica si ya existe un evento en esa clave dentro del calendario
    if clave in calendario:
        # Si ya hay un evento, se pregunta al usuario si desea sobrescribirlo
        opt = input(f"Ya existe un evento en {fecha}, Salón {salon}, Turno {turno}. ¿Sobrescribir? (S/N): ")
        # Si la respuesta no es 's' (de sí), se cancela la operación y se informa
        if opt.lower() != 's':
            print("No se realizó ningún cambio.")
            return
        # Si se elige sobrescribir, se informa que el evento anterior será reemplazado
        print(f"Evento anterior en {clave} eliminado.")
    # Se agrega o actualiza el evento en el calendario usando la clave generada
    calendario[clave] = evento
    # Se informa que el evento fue agregado correctamente, mostrando el nombre del cliente
    print(f"Evento '{evento['cliente']}' agregado el {fecha} en Salón {salon}, Turno {turno}.")
#===================================================================================================================================
def imprimirEvento(clave, evento):
    """
        Función para imprimir los detalles de un evento a partir de su clave y datos.
    """
    fecha, salon, turno = clave # Desempaqueta la tupla 'clave' en las variables fecha, salón y turno
    cliente = evento["cliente"] # Extrae del diccionario 'evento' el nombre del cliente
    tipo = evento["tipo"] # Extrae el tipo de evento (Ej: cumpleaños, casamiento, etc.)
    cant = evento["cant_personas"] # Extrae la cantidad de personas que asistirán al evento
    servicios = evento["servicios"] # Extrae la lista de servicios contratados para el evento
    precios = evento["precios"] # Extrae la lista de precios correspondientes a los servicios contratados
    total = sum(precios) # Calcula el total del evento sumando los precios de los servicios

    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║                    DETALLE DE EVENTO EN SALÓN                      ║")
    print("╚════════════════════════════════════════════════════════════════════╝")
    print(f"Fecha: {fecha} | Salón: {salon} | Turno: {turno}")
    print(f"Cliente: {cliente}")
    print(f"Tipo de Evento: {tipo}")
    print(f"Cantidad de Personas: {cant}")

    print("┌────────────────────────────────┬────────────┐")
    print("│          Servicio              │   Precio   │")
    print("├────────────────────────────────┼────────────┤")

    for s, p in zip(servicios, precios):
        print(f"│ {s:<30} │ ${p:<10}│")

    print("└────────────────────────────────┴────────────┘")
    print(f"TOTAL del evento: ${total}") #Imprime el total calculado del evento

#===================================================================================================================================
def imprimir_eventos(calendario):
    """
    Imprime todos los eventos del calendario, ordenados por el total recaudado (de mayor a menor).
    Además, muestra un resumen con el total general recaudado entre todos los eventos.
    """
    # Inicializa una variable acumuladora para el total recaudado por todos los eventos
    total_general = 0

    # Ordena los eventos del calendario de mayor a menor según el total de precios de cada evento.
    # calendario.items() devuelve una lista de tuplas: (clave, evento)
    # item[1] representa el diccionario del evento (el valor en el calendario)
    # item[1]["precios"] es una lista de precios asociados a ese evento
    # sum(item[1]["precios"]) calcula el total de cada evento
    # reverse=True indica que queremos que el orden sea descendente (mayor a menor total)
    eventos_ordenados = sorted(calendario.items(), key=lambda item: sum(item[1]["precios"]), reverse=True)

    # Imprime el encabezado decorativo para el listado de eventos
    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║                  DETALLE DE EVENTOS CON FECHAS                     ║")
    print("╚════════════════════════════════════════════════════════════════════╝")

    # Recorre cada evento ordenado
    for clave, evento in eventos_ordenados:
        # Llama a la función imprimirEvento para mostrar los datos del evento
        imprimirEvento(clave, evento)
        # Suma el total de ese evento al total general
        total_general += sum(evento["precios"])

    print("\n════════════════════════════════════════════════════════════════════")
    print(f"TOTAL GENERAL INGRESADO POR TODOS LOS EVENTOS: ${total_general}")
    print("════════════════════════════════════════════════════════════════════")
#===================================================================================================================================
def eliminar_evento(usuario, calendario):
    """
        Permite al usuario eliminar un evento que haya registrado.
        Parámetros:
            - usuario: Nombre del usuario que realiza la acción.
            - calendario: Diccionario que contiene los eventos registrados.
    """
    try:
        seleccion = seleccionar_fecha_salon_turno(calendario)
        if not seleccion:
            print("Eliminación cancelada.")
            return
        fecha, salon, turno = seleccion # Desempaqueta la selección en sus tres componentes: fecha, salón y turno.
        clave = (fecha, salon, turno) # Crea la clave con la que se accede al evento en el diccionario `calendario`.
        calendario.pop(clave)
        print("Evento eliminado correctamente.")
        registrar_auditoria(usuario, f"Eliminó un evento en {salon} el {fecha} - {turno}") # Registra la acción en el archivo de auditoría
        guardar_en_json(EVENTOS, calendario) # Guarda el estado actualizado del calendario en el archivo JSON correspondiente.
    except Exception as e:
        print("Error al eliminar el evento:", e)
#===================================================================================================================================
def editarEvento(calendario, servicios_disponibles, usuario):
    # Se selecciona un evento a editar mediante fecha, salón y turno
    clave = seleccionar_fecha_salon_turno(calendario)
    if not clave:
        print("Edición cancelada.")  # Si no se elige ninguna clave, se cancela
        return
    
    fechaNueva, salonNuevo, turnoNuevo = clave  # Se desempaqueta la clave original
    claveNueva = (fechaNueva, salonNuevo, turnoNuevo)  # Se guarda como la clave actual para editar

    evento = calendario[clave]  # Se obtiene el evento original a partir de la clave
    eventoNuevo = evento.copy()  # Se hace una copia para modificar sin alterar el original hasta confirmar

    interfazValorAModificar()
    valorAModificar = seleccionar_opciones(ATRIBUTOS_DE_EVENTOS)  # El usuario elige qué atributo cambiar

    while valorAModificar is not None:
        if valorAModificar == "Cliente":
            #------------------- Modificación del nombre del cliente ---------------------
            nuevo_cliente = input("Ingrese el nuevo nombre del cliente: ").strip().title()
            print(f"Cliente modificado a {nuevo_cliente}.")
            eventoNuevo["cliente"] = nuevo_cliente

        elif valorAModificar == "Tipo de evento":
            #------------------- Cambio del tipo de evento -------------------
            interfaz_tipo_evento()
            nuevo_tipo = seleccionar_opciones(TIPOS_DE_EVENTOS)
            eventoNuevo["tipo"] = nuevo_tipo

        elif valorAModificar == "Cantidad de personas":
            #------------------- Cambio en la cantidad de personas -------------------
            while True:
                val = input("Ingrese la nueva cantidad de personas: ").strip()
                if val.isdigit() and int(val) > 0:
                    cant = int(val)
                    max_cap = capacidades_salones[salonNuevo]
                    if cant <= max_cap:
                        #------------------- Actualiza cantidad en evento original -------------------
                        evento["cant_personas"] = cant  
                        break
                    else:
                        print(f"La cantidad máxima para el salón {salonNuevo} es {max_cap}.")
                else:
                    print("Por favor ingrese un número entero positivo.")
            print(f"Cantidad de personas modificada a {cant}.")
            eventoNuevo["cant_personas"] = cant

            #------------------- Actualiza servicios y precios si la cantidad cambió -------------------
            servicios_evento = calendario[clave]["servicios"].copy()
            precios_evento = calendario[clave]["precios"].copy()
            for i in range(len(servicios_evento)):
                servicio = servicios_evento[i]
                precio = precios_evento[i]
                if servicio in servicios_disponibles:
                    if servicios_disponibles[servicio]["tipo"] == "variable":
                        precios_evento[i] = servicios_disponibles[servicio]["precio"] * cant
                    else:
                        precios_evento[i] = servicios_disponibles[servicio]["precio"]
                elif servicio == "Limpieza postevento":
                    precios_evento[i] = precios_evento[i] * cant * 0.05  # Recalcula limpieza
            eventoNuevo["servicios"] = servicios_evento
            eventoNuevo["precios"] = precios_evento

        elif valorAModificar == "Servicios":
            #------------------- Permite modificar los servicios del evento -------------------
            servicios_evento = servicios_disponibles.copy()
            for servicio, precio in servicios_evento.items():
                if precio["tipo"] == "variable":
                    servicios_evento[servicio] = precio["precio"] * evento["cant_personas"]
                else:
                    servicios_evento[servicio] = precio["precio"]
            nuevos_servicios, nuevos_precios = seleccionar_servicios(servicios_evento)
            subtotal = sum(nuevos_precios)  # Suma los precios para obtener el total sin limpieza
            limpieza = subtotal * 0.05  # Calcula un 5% extra por limpieza postevento
            nuevos_servicios.append("Limpieza postevento")  # Se agrega este servicio a la lista
            nuevos_precios.append(limpieza)  # Se agrega el costo de limpieza
            eventoNuevo["servicios"] = nuevos_servicios # Actualiza la lista de servicios
            eventoNuevo["precios"] = nuevos_precios # Actualiza la lista de precios
            print("Servicios modificados correctamente.")

        elif valorAModificar == "Fecha":
            #------------------- Permite cambiar la fecha del evento -------------------
            while True:
                fechaNueva = input("Ingrese la nueva fecha del evento (YYYY-MM-DD): ").strip()
                if validarFecha(fechaNueva):
                    if (fechaNueva, salonNuevo, turnoNuevo) in calendario:
                        print("Ya existe un evento en esa fecha, salón y turno. No se puede modificar.")
                    else:
                        claveNueva = (fechaNueva, salonNuevo, turnoNuevo)
                        print(f"Fecha modificada a {fechaNueva}.")
                        break

        elif valorAModificar == "Turno":
            #------------------- Cambio del turno -------------------
            interfaz_tipo_turno()
            turnoNuevo = seleccionar_opciones(TURNOS)
            if turnoNuevo is None:
                print("Edición cancelada.")
                break
            if (fechaNueva, salonNuevo, turnoNuevo) in calendario:
                print("Ya existe un evento en esa fecha, salón y turno. No se puede modificar.")
                break
            else:
                print(f"Turno modificado a {turnoNuevo}.")
                claveNueva = (fechaNueva, salonNuevo, turnoNuevo)

        elif valorAModificar == "Salon":
            #------------------- Cambio de salón -------------------
            interfaz_tipo_salon()
            salonNuevo = seleccionar_opciones(SALONES)
            while capacidades_salones[salonNuevo] < evento["cant_personas"]:
                print(f"El salón {salonNuevo} no admite {evento['cant_personas']} personas. Elija otro salón.")
                salonNuevo = seleccionar_opciones(SALONES)
            if salonNuevo is None:
                print("Edición cancelada.")
                break
            if (fechaNueva, salonNuevo, turnoNuevo) in calendario:
                print("Ya existe un evento en esa fecha, salón y turno. No se puede modificar.")
                break
            else:
                print(f"Salón modificado a {salonNuevo}.")
                claveNueva = (fechaNueva, salonNuevo, turnoNuevo)
        else:
            print("Opción no válida.")
            break

        interfazValorAModificar()
        valorAModificar = seleccionar_opciones(ATRIBUTOS_DE_EVENTOS)  # Se repite el proceso si se desea

    # Se finaliza la edición: se reemplaza el evento original por el modificado
    calendario.pop(clave)  # Elimina el evento viejo
    calendario[claveNueva] = eventoNuevo  # Inserta el evento modificado con la nueva clave

    # Auditoría: se registra el cambio detallando qué atributos se modificaron
    lineaDeAuditoria = f"Editó el evento de {evento['cliente']} en {clave} a {claveNueva}"
    for atributo in ["cliente", "tipo", "cant_personas", "servicios", "precios"]:
        if evento[atributo] != eventoNuevo[atributo]:
            lineaDeAuditoria += f", {atributo} de '{evento[atributo]}' a '{eventoNuevo[atributo]}'"
    registrar_auditoria(usuario, lineaDeAuditoria)
    guardar_en_json(EVENTOS, calendario) # Se guarda el nuevo estado del calendario en el archivo JSON
    return claveNueva, eventoNuevo  # Devuelve la nueva clave del evento y sus datos actualizados
#===================================================================================================================================
def agregar_servicio(servicios_disponibles):
    nombre = input("Nombre del nuevo servicio: ").strip().title() #Solicita al usuario el nombre del nuevo servicio
    
    if nombre in servicios_disponibles: # Verifica si el servicio ya existe en el diccionario
        print("Ese servicio ya existe.")
        return servicios_disponibles 
    
    opciones_tipo = ["Fijo", "Variable"] # Define las opciones disponibles para el tipo de servicio
    interfazTipoServicio()
    tipo = seleccionar_opciones(opciones_tipo)
    if tipo is None:
        print("Operación cancelada.")
        return servicios_disponibles
    while True:
        try:
            precio = float(input("Ingrese el nuevo precio del servicio: "))
            while precio <= 0:
                print("El precio no puede ser negativo. Intente nuevamente.")
                precio = float(input("Ingrese el nuevo precio del servicio: "))
            break
        except ValueError:
            print("Precio inválido. Ingrese un número.")
    servicios_disponibles[nombre] = {"tipo": tipo.lower(), "precio": precio} # Agrega el nuevo servicio al diccionario
    guardar_en_json(SERVICIOS, servicios_disponibles) # Guarda el diccionario actualizado en el archivo JSON correspondiente
    registrar_auditoria("admin", f"Agregó el servicio '{nombre}'")
    print(f"Servicio '{nombre}' agregado correctamente.")
#===================================================================================================================================
def mostrar_servicios(servicios_disponibles):
    """
    Muestra todos los servicios disponibles en el sistema.
    Si no hay servicios, informa al usuario.
    """
    try:
        interfaz_mostrar_servicios()  # Muestra la interfaz de servicios
        if not servicios_disponibles:  # Verifica si el diccionario de servicios está vacío
            print("No hay servicios registrados.")
        else: # Si hay servicios, los muestra en una tabla
            print("┌────────────────────────────────┬────────────┬────────────┐")
            print("│          Servicio              │   Precio   │   Tipo     │")
            print("├────────────────────────────────┼────────────┼────────────┤")
            for servicio, datos in servicios_disponibles.items(): # Recorre cada servicio en el diccionario
                # Muestra el nombre del servicio, su precio y tipo (fijo o variable) en formato de tabla
                nombre = servicio
                precio = datos['precio']
                tipo = datos['tipo']
                print(f"│ {nombre:<30} │ ${precio:<9.2f} │ {tipo:<10} │")
            print("└────────────────────────────────┴────────────┴────────────┘")
        registrar_auditoria("admin", "Mostró la lista de servicios")  # Registra la acción en el archivo de auditoría
    except Exception as e: # Captura cualquier error al mostrar los servicios
        print("Error al mostrar la interfaz de servicios:", e)

#===================================================================================================================================
def eliminar_servicio(servicios_disponibles):
    if not servicios_disponibles: # Verifica si el diccionario de servicios está vacío
        print("No hay servicios registrados.")
        return servicios_disponibles
    
    print("Servicios disponibles para eliminar:")
    for indice, servicio in enumerate(servicios_disponibles, 1):
        # Muestra cada servicio con su número, nombre, precio y tipo (fijo o variable)
        print(f"{indice}: {servicio} - ${servicios_disponibles[servicio]['precio']} ({servicios_disponibles[servicio]['tipo']})")
    print("0: Cancelar eliminación")

    # Permite al usuario seleccionar el servicio a eliminar
    servicio_a_eliminar = seleccionar_opciones(list(servicios_disponibles.keys()))

    if servicio_a_eliminar is None:
        print("Operación cancelada.")
        return servicios_disponibles
    else:# Elimina el servicio seleccionado del diccionario (si existe)
        servicios_disponibles.pop(servicio_a_eliminar, None)
        guardar_en_json(SERVICIOS, servicios_disponibles) # Guarda el diccionario actualizado en el archivo JSON
        registrar_auditoria("admin", f"Eliminó el servicio '{servicio_a_eliminar}'")
        print(f"Servicio '{servicio_a_eliminar}' eliminado correctamente.")
#===================================================================================================================================
def editar_servicio(servicios_disponibles):
    if not servicios_disponibles: # Verifica si el diccionario de servicios está vacío
        print("No hay servicios registrados.")
        return servicios_disponibles

    print("Servicios disponibles para editar:")
    for indice, servicio in enumerate(servicios_disponibles, 1):
        # Muestra cada servicio con su número, nombre, precio y tipo (fijo o variable)
        print(f"{indice}: {servicio} - ${servicios_disponibles[servicio]['precio']} ({servicios_disponibles[servicio]['tipo']})")
    print("0: Cancelar edición")

    # Permite al usuario seleccionar el servicio a editar
    servicio_a_editar = seleccionar_opciones(list(servicios_disponibles.keys()))

    if servicio_a_editar is None:
        print("Operación cancelada.")
        return servicios_disponibles

    interfazAtributoDeServicioAModificar()
    opciones_modificar = ["Nombre", "Tipo", "Precio"]  # Opciones disponibles para editar
    opcion_modificar = seleccionar_opciones(opciones_modificar)

    if opcion_modificar is None:
        print("Operación cancelada.")
        return servicios_disponibles

    #------------------- EDICIONES MULTIPLES -------------------
    while True:
        if opcion_modificar is not None:
            #------------------- CAMBIO DE NOMBRE DEL SERVICIO -------------------
            if opcion_modificar == "Nombre":
                nuevo_nombre = input("Ingrese el nuevo nombre del servicio: ").strip().title()

                if nuevo_nombre in servicios_disponibles:
                    print("Ese nombre ya existe.")
                    break
                # Copia los datos al nuevo nombre y elimina el antiguo
                servicios_disponibles[nuevo_nombre] = servicios_disponibles.pop(servicio_a_editar)
                print(f"Nombre del servicio cambiado a '{nuevo_nombre}'.")
                # Actualiza el nombre en la variable de referencia
                servicio_a_editar = nuevo_nombre

            #------------------- CAMBIO DE TIPO DEL SERVICIO -------------------
            elif opcion_modificar == "Tipo":
                opciones_tipo = ["Fijo", "Variable"]
                interfazTipoServicio()
                nuevo_tipo = seleccionar_opciones(opciones_tipo)
                if nuevo_tipo is None:
                    print("Operación cancelada.")
                    break

                servicios_disponibles[servicio_a_editar]["tipo"] = nuevo_tipo.lower()
                print(f"Tipo del servicio cambiado a '{nuevo_tipo}'.")

            #------------------- CAMBIO DE PRECIO DEL SERVICIO -------------------
            elif opcion_modificar == "Precio":
                while True:
                    try:
                        nuevo_precio = float(input("Ingrese el nuevo precio del servicio: "))
                        # Asigna el nuevo precio
                        servicios_disponibles[servicio_a_editar]["precio"] = nuevo_precio
                        print(f"Precio del servicio cambiado a ${nuevo_precio}.")
                        break
                    except ValueError:
                        print("Precio inválido. Ingrese un número.")
            else:
                print("Opción no válida.")
            interfazAtributoDeServicioAModificar()
            opcion_modificar = seleccionar_opciones(opciones_modificar)
        else:
            print("Operación terminada.")
            break
    #------------------- FINALIZACIÓN DE EDICIÓN -------------------
    registrar_auditoria("admin", f"Editó el servicio '{servicio_a_editar}'")
    print(f"Servicio '{servicio_a_editar}' editado correctamente.")
    guardar_en_json(SERVICIOS, servicios_disponibles) # Guarda los cambios en el archivo JSON
#===================================================================================================================================
def seleccionar_fecha_salon_turno(calendario):
    """
    Permite seleccionar una fecha, salón y turno de entre los eventos existentes en el calendario.
    Valida cada paso mostrando solo las opciones disponibles.
    Devuelve: (fecha, salon, turno) o None si se cancela.
    """
    if not calendario:# Verifica si el calendario está vacío
        print("No hay eventos registrados en el calendario.")
        return None

    #------------------- Paso 1: Mostrar fechas disponibles -------------------
    # Se crea una lista ordenada sin duplicados con todas las fechas disponibles en el calendario
    lista_fechas = sorted(set(clave_evento[0] for clave_evento in calendario))
    print("\nFechas disponibles:")
    
    for indice, fecha in enumerate(lista_fechas, 1): # Se enumeran las fechas para que el usuario pueda elegir una
        print(f"{indice}) {fecha}")
    print("0) Cancelar")

    #------------------- SELECION FECHA VALIDA -------------------
    while True:
        entrada = input(f"Seleccione una fecha (1-{len(lista_fechas)}): ").strip()
        if entrada == "0":
            return None
        if entrada.isdigit() and 1 <= int(entrada) <= len(lista_fechas):
            fecha_seleccionada = lista_fechas[int(entrada) - 1]  # Se toma la fecha seleccionada
            break
        print("Opción inválida. Intente nuevamente.")

    #------------------- Paso 2: Mostrar salones disponibles para esa fecha -------------------
    # Se crea una lista ordenada de salones asociados a la fecha elegida
    lista_salones = sorted(set(clave_evento[1] for clave_evento in calendario if clave_evento[0] == fecha_seleccionada))
    print(f"\nSalones disponibles para {fecha_seleccionada}:")
    
    for indice, salon in enumerate(lista_salones, 1): # Se enumeran los salones disponibles
        print(f"{indice}) {salon}")
    print("0) Cancelar")  # Opción para cancelar
    
    #------------------- SELECION SALON VALIDO -------------------
    while True:
        entrada = input(f"Seleccione un salón (1-{len(lista_salones)}): ").strip()
        if entrada == "0":
            return None
        if entrada.isdigit() and 1 <= int(entrada) <= len(lista_salones):
            salon_seleccionado = lista_salones[int(entrada) - 1]  # Se toma el salón seleccionado
            break
        print("Opción inválida. Intente nuevamente.")

    #------------------- Paso 3: Mostrar turnos disponibles para esa fecha y salón -------------------
    # Se crea una lista ordenada de turnos asociados a la fecha y salón elegidos
    lista_turnos = sorted(set(clave_evento[2] for clave_evento in calendario if clave_evento[0] == fecha_seleccionada and clave_evento[1] == salon_seleccionado))
    print(f"\nTurnos disponibles para {salon_seleccionado} el {fecha_seleccionada}:")
    
    for indice, turno in enumerate(lista_turnos, 1): # Se enumeran los turnos disponibles
        print(f"{indice}) {turno}")
    print("0) Cancelar")
    
    #------------------- SELECION TURNO VALIDO -------------------
    while True:
        entrada = input(f"Seleccione un turno (1-{len(lista_turnos)}): ").strip()
        if entrada == "0":
            return None
        if entrada.isdigit() and 1 <= int(entrada) <= len(lista_turnos):
            turno_seleccionado = lista_turnos[int(entrada) - 1]  # Se toma el turno seleccionado
            break
        print("Opción inválida. Intente nuevamente.")
    # Devuelve la combinación seleccionada como una tupla
    return (fecha_seleccionada, salon_seleccionado, turno_seleccionado)
#===================================================================================================================================
def buscarEvento(calendario):
    """
        Esta función permite buscar un evento específico dentro del calendario 
        solicitando al usuario que seleccione una fecha, un salón y un turno.
    """
    seleccion = seleccionar_fecha_salon_turno(calendario)
    if not seleccion:
        print("Búsqueda cancelada.")
        return
    fecha, salon, turno = seleccion # Extrae la fecha, el salón y el turno de la selección realizada.
    clave = (fecha, salon, turno) # Crea la clave que permite acceder al evento correspondiente en el diccionario `calendario`.
    imprimirEvento(clave, calendario[clave])
#===================================================================================================================================
def mostrar_menu_servicios(servicios_disponibles, servicios_seleccionados):
    """
        Muestra un menú con los servicios disponibles (excluyendo los ya seleccionados)
        y devuelve:
        
            - lista de servicios disponibles para esta iteración
            - opción para eliminar un servicio
            - opción para finalizar la selección
    """
    print("\n+--------------------------------------------------+")
    print("|        SELECCIÓN DE SERVICIOS DISPONIBLES        |")
    print("+--------------------------------------------------+")

    # Crea una lista con los servicios que aún no fueron seleccionados
    servicios_para_mostrar = [
        servicio for servicio in servicios_disponibles 
        if servicio not in servicios_seleccionados
    ]

    # Recorre la lista de servicios disponibles y los imprime con su precio
    for indice, servicio in enumerate(servicios_para_mostrar, 1):
        nombre_formateado = servicio.ljust(30)  # Ajusta el nombre para alineación
        precio_formateado = f"${servicios_disponibles[servicio]}"  # Precio del servicio
        print(f"|{indice}: {nombre_formateado} {precio_formateado.rjust(14)}  |")

    # Define las opciones adicionales: eliminar servicio o finalizar selección
    opcion_eliminar = len(servicios_para_mostrar) + 1
    opcion_finalizar = len(servicios_para_mostrar) + 2

    # Muestra las opciones adicionales
    print("+--------------------------------------------------+")
    print(f"| {opcion_eliminar}: Eliminar un servicio elegido                 |")
    print(f"| {opcion_finalizar}: Finalizar selección de servicios             |")
    print("+--------------------------------------------------+")

    # Devuelve las opciones necesarias para que la función principal las utilice
    return servicios_para_mostrar, opcion_eliminar, opcion_finalizar

def seleccionar_servicios(servicios_disponibles):
    """
    Permite al usuario seleccionar, eliminar y confirmar servicios desde un listado.
    Devuelve:
    - Lista de servicios seleccionados
    - Lista de precios correspondientes
    """

    # Lista que almacenará los servicios que el usuario seleccione
    servicios_seleccionados = []

    # Bucle principal: se repite hasta que el usuario finalice la selección
    while True:
        # Muestra el menú con los servicios disponibles y recibe las opciones válidas
        servicios_para_elegir, opcion_eliminar, opcion_finalizar = mostrar_menu_servicios(servicios_disponibles, servicios_seleccionados)

        # Pide al usuario que elija una opción
        entrada_usuario = input("Elegí una opción: ").strip()

        # Si la entrada no es un número, se informa el error
        if not entrada_usuario.isdigit():
            print("Entrada inválida.")
            continue
        # Convierte la entrada a entero para comparar
        opcion_elegida = int(entrada_usuario)

        # Si elige un número válido de servicio, lo agrega a la selección
        if 1 <= opcion_elegida <= len(servicios_para_elegir):
            servicio_elegido = servicios_para_elegir[opcion_elegida - 1]
            servicios_seleccionados.append(servicio_elegido)
            print(f"'{servicio_elegido}' agregado.")

        # Si elige la opción para eliminar un servicio ya seleccionado
        elif opcion_elegida == opcion_eliminar:
            # Verifica si hay servicios para eliminar
            if not servicios_seleccionados:
                print("Aún no hay servicios que eliminar.")
                continue
            # Muestra los servicios seleccionados
            print("\n Servicios seleccionados:")
            for indice, servicio in enumerate(servicios_seleccionados, 1):
                print(f"{indice}. {servicio}")

            # Pide el número del servicio a eliminar
            entrada_eliminar = input("Número del servicio a eliminar: ")

            # Si es un número válido, lo elimina
            if entrada_eliminar.isdigit():
                indice_eliminar = int(entrada_eliminar)
                if 1 <= indice_eliminar <= len(servicios_seleccionados):
                    servicio_eliminado = servicios_seleccionados.pop(indice_eliminar - 1)
                    print(f" '{servicio_eliminado}' eliminado.")
                else:
                    print("Número inválido.")
            else:
                print("Entrada inválida.")
        # Si elige finalizar
        elif opcion_elegida == opcion_finalizar:
            # Solo permite finalizar si hay al menos un servicio seleccionado
            if not servicios_seleccionados:
                print("No podés finalizar sin al menos un servicio.")
            else:
                print("Finalizando selección...")
                break  # Sale del bucle principal
        # Si elige una opción que no existe
        else:
            print("Opción no válida.")

    # Crea una lista de precios según los servicios seleccionados
    precios_seleccionados = [servicios_disponibles[servicio] for servicio in servicios_seleccionados]

    # Devuelve las dos listas: nombres y precios de los servicios
    return servicios_seleccionados, precios_seleccionados
#===================================================================================================================================
def seleccionar_opciones(lista_de_opciones):
    """
    Versión recursiva que presenta una lista de opciones y devuelve la elegida.
    Vuelve a llamarse a sí misma si la opción es inválida.
    """
    opcion = input(f"Seleccione una opción (1-{len(lista_de_opciones)} o 0 para cancelar): ").strip()

    # ---- CASO BASE 1: El usuario cancela la operación ----
    if opcion == "0":
        return None
    
    # ---- CASO BASE 2: El usuario ingresa una opción válida ----
    if opcion.isdigit() and 1 <= int(opcion) <= len(lista_de_opciones):
        return lista_de_opciones[int(opcion) - 1]
    
    # ---- PASO RECURSIVO: La opción no es válida ----
    else:
        print("Opción inválida. Intente nuevamente.")
        # La función se llama a sí misma para repetir la pregunta.
        return seleccionar_opciones(lista_de_opciones)
#===================================================================================================================================
# Validación y calendario
def esBisiesto(año):
    """
    	Un año es bisiesto si es divisible por 4 y no divisible por 100, a menos que también sea divisible por 400.
    """
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)
#===================================================================================================================================
def diadelasemana(dia, mes, año):
    """
        Función que devuelve el día de la semana usando el algoritmo de Zeller
    """
    # Para enero y febrero, se consideran como meses 13 y 14 del año anterior
    if mes < 3:
        mes += 10
        año -= 1
    else:
        mes -= 2
    # Se separa el siglo y el año
    siglo = año // 100
    anio2 = año % 100
    # Fórmula de Zeller para obtener el día de la semana (0=domingo, ..., 6=sábado)
    diassem = (((26 * mes - 2) // 10) + dia + anio2 + (anio2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    # Si es negativo, se ajusta sumando 7
    if diassem < 0:
        diassem += 7
    return diassem
#===================================================================================================================================
def diasDelMes(año, mes):
    """
        Lista de días por mes. Febrero depende de si es bisiesto.
    """
    dias_en_mes = [31, 29 if esBisiesto(año) else 28, 31, 30, 31, 30,
                   31, 31, 30, 31, 30, 31]
    return dias_en_mes[mes - 1]
#===================================================================================================================================
def validarFecha(fecha):
    """
        Función para validar una fecha ingresada
    """
    partes = fecha.split("-") #  "2025-04-10" -----> ["2025", "04", "10"]
    if len(partes) != 3: # Si el usuario ingresa mal la fecha (falta un parametro) retorna FALSE
        return False

    #Separamos en partes la fecha ingresada en 3 Variables
    anio_str = partes[0]
    mes_str = partes[1]
    dia_str = partes[2]

    # Validar que todos sean dígitos
    if not (anio_str.isdigit() and mes_str.isdigit() and dia_str.isdigit()):
        return False

    #Convertimos para una de las partes en numeros enteros
    año = int(anio_str)
    mes = int(mes_str)
    dia = int(dia_str)

    #Verificamos el rango del MES
    if mes < 1 or mes > 12:
        return False

    #Verificamos el rango del DIA ----> Llamamos a la funcioin dias_del_mes
    if dia < 1 or dia > diasDelMes(año, mes):
        return False
    return True
#===================================================================================================================================
def mostrarCalendario(año, eventos):
    """
        Función para mostrar el calendario anual.
        Recibe un año y un diccionario de eventos.
        Muestra mes por mes los días y marca con corchetes [ ] si hay un evento en esa fecha.
    """
    # Lista de nombres de los meses, para mostrar en el calendario.
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    # Prepara una lista vacía que almacenará solo las fechas de los eventos para facilitar la búsqueda.
    fechas_eventos = []
    # Recorre cada clave del diccionario de eventos.
    for clave in eventos:
        fecha = clave[0]  # Extrae la fecha (está en la posición 0 de la tupla clave)
        # Agrega la fecha a la lista fechas_eventos.
        fechas_eventos.append(fecha)

    # Recorre todos los meses del año, del 1 al 12.
    for mes in range(1, 13):  # recorre los meses (1 hasta 12)
        # Imprime el nombre del mes y el año, por ejemplo: "Enero 2025".
        print("\n" + meses[mes - 1] + " " + str(año))
        # Imprime el encabezado de los días de la semana.
        print("Dom\tLun\tMar\tMie\tJue\tVie\tSab")  # Encabezado de días

        # Llama a la función diadelasemana para saber en qué día de la semana empieza el mes.
        primer_dia_semana = diadelasemana(1, mes, año)
        # Si el primer día no es domingo (0), imprime espacios tabulados para alinear el primer día correctamente.
        if primer_dia_semana != 0:
            print("\t" * primer_dia_semana, end="")  # Espacios iniciales

        # Llama a la función diasDelMes para saber cuántos días tiene el mes (28, 29, 30 o 31).
        dias_mes = diasDelMes(año, mes)

        # Recorre cada día del mes, desde el 1 hasta el último día.
        for dia in range(1, dias_mes + 1):
            # Genera la fecha en formato "YYYY-MM-DD" para comparar con las fechas de eventos.
            fecha_actual = f"{año:04d}-{mes:02d}-{dia:02d}"
            # Llama a diadelasemana para saber qué día de la semana corresponde a la fecha.
            num_dia_semana = diadelasemana(dia, mes, año)

            # Si la fecha actual coincide con una fecha de evento, la imprime con corchetes.
            if fecha_actual in fechas_eventos:
                print(f"[{dia:2d}]", end="\t")
            else:
                # Si no es un evento, imprime el número de día normalmente.
                print(f"{dia:2d}", end="\t")

            # Si es sábado (6), imprime un salto de línea para iniciar una nueva fila.
            if num_dia_semana == 6:
                print()
        # Imprime una línea en blanco al terminar cada mes.
        print()
#===================================================================================================================================

def programaPrincipal(usuarios, calendario, servicios_disponibles):
    """
        Función principal que coordina el funcionamiento del sistema completo.
        Carga los datos desde archivos JSON, muestra el menú principal e invoca
        los submenús según el tipo de usuario (admin o usuario común).
    """
    usuarios = cargar_desde_json(USUARIOS) # Carga los usuarios desde el archivo JSON. Sobrescribe la variable local `usuarios`.
    if len(usuarios) == 0: # Si no se encontraron usuarios cargados
        usuarios["admin"] = {"contraseña": "1234", "rol": "admin"} # Se crea un usuario administrador por defecto para asegurar el acceso inicial al sistema.
    calendario = cargar_desde_json("eventos.json") # Carga el calendario de eventos desde archivo JSON.
    servicios_disponibles = cargar_desde_json(SERVICIOS) # Carga los servicios disponibles desde archivo JSON.
    if len(servicios_disponibles) == 0: # Si no se encontraron servicios cargados
        crearServiciosPredefinidos(servicios_disponibles) # Se crean servicios por defecto para asegurar que haya al menos uno disponible.
    while True:
        menu_interactivo()
        try:
            entrada = input("Ingrese una opción: ")
            if entrada == "1": # ---------------- INICIO SESION -------------
                usuario_actual = iniciar_sesion(usuarios)
                if usuario_actual:
                    if usuarios[usuario_actual]["rol"] == "admin": # Si el usuario tiene rol de administrador
                        usuarios = menu_admin(usuarios,servicios_disponibles)
                    else: # usuario común.
                        menu_usuario(usuario_actual, calendario, usuarios, servicios_disponibles)
            elif entrada == "-1": # ---------------- SALIR SESION -------------
                print("USTED HA FINALIZADO EL PROGRAMA. HASTA LUEGO.")
                break
            else:
                print("Opción inválida.")
        except Exception as e:
            print(f"Error inesperado: {e}")
            print("Error inesperado en el menú principal.")

## PROGRAMA PRINCIPAL ##
programaPrincipal(usuarios,calendario,servicios_disponibles)
