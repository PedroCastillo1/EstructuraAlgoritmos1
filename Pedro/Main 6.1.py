
import math

# — Constantes —
PRECIO_CATERING_BASIC    = 2500
PRECIO_CATERING_STD      = 3500
PRECIO_CATERING_PREMIUM  = 5000
PRECIO_MOSO              = 20000
PRECIO_BARTENDER         = 25000
PRECIO_SEGURIDAD         = 22000
PRECIO_DECORACION_BASE   = 80000
PORCENTAJE_LIMPIEZA      = 0.05
PRECIO_TRANSPORTE          = 50000
PRECIO_SOUND_LIGHTS      = 80000
PRECIO_DJ          = 50000
PRECIO_FOTOGRAFO   = 20000

# — Capacidades máximas por salón (entre 20 y 1000) —
capacidades_salones = {
    "Palermo":        300,
    "Puerto Madero":  700,
    "Nordelta":       150,
    "San Telmo":       80,
    "Recoleta":       500
}

#Creamos el diccionario Calendario
calendario = {}
#Creamos el diccionario con los servicios estaticos disponibles
servicios_disponibles = {
    "DJ":                        PRECIO_DJ,
    "Fotógrafo":                 PRECIO_FOTOGRAFO,
    "Decoración básica":         PRECIO_DECORACION_BASE,
    "Transporte":                PRECIO_TRANSPORTE ,
    "Pack sonido e iluminación": PRECIO_SOUND_LIGHTS
}

# Interfaces visuales
def interfaz_bienvenida_gestor_eventos():
    print("\n+--------------------------------------------------+")
    print("|           BIENVENIDO AL GESTOR DE EVENTOS        |")
    print("+--------------------------------------------------+")
    print("| 1: Crear un evento                               |")
    print("| 2: Ver todos los eventos                         |")
    print("| 3: Eliminar evento                               |")
    print("| 4: Mostrar calendario                            |")
    print("| 5: Buscar evento                                 |")
    print("| 6: Salir del gestor de eventos                   |")
    print("+--------------------------------------------------+")

def interfaz_salir_programa():
    print("\n+--------------------------------------+")
    print("|     Gracias por usar el programa.    |")
    print("|            ¡Hasta pronto!            |")
    print("+--------------------------------------+")
    
def interfaz_crear_evento():
    print("\n+--------------------------------------------------+")
    print("|              CREAR NUEVO EVENTO                  |")
    print("+--------------------------------------------------+")

def interfaz_ver_evento():
    print("\n+--------------------------------------------------+")
    print("|               VISUALIZAR EVENTO                  |")
    print("+--------------------------------------------------+")

def interfaz_eliminar_evento():
    print("\n+--------------------------------------------------+")
    print("|                ELIMINAR EVENTO                   |")
    print("+--------------------------------------------------+")

def interfaz_mostrar_calendario():
    print("\n+--------------------------------------------------+")
    print("|              MOSTRAR CALENDARIO                  |")
    print("+--------------------------------------------------+")

def interfaz_buscar_evento():
    print("\n+--------------------------------------------------+")
    print("|                BUSCAR EVENTO                     |")
    print("+--------------------------------------------------+")

def interfaz_salir_gestor_eventos():
    print("\n+--------------------------------------------------+")
    print("|       Saliendo del gestor de eventos...          |")
    print("+--------------------------------------------------+")
    
def interfaz_tipo_evento():
    print("\n+--------------------------------------------------+")
    print("|                  TIPO DE EVENTO                  |")
    print("+--------------------------------------------------+")
    print("| 1) Fiesta de egresados                           |")
    print("| 2) Casamiento                                    |")
    print("| 3: Cumple de XV                                  |")
    print("| 4: Despedida de soltero                          |")
    print("| 5: Evento empresarial                            |")
    print("| 6: Conferencia                                   |")
    print("|--------------------------------------------------|")
    print("| 0) Cancelar                                      |")
    print("+--------------------------------------------------+")
    
def interfaz_tipo_salon():
    print("\n+--------------------------------------------------+")
    print("|                SELECCIONE SALÓN                  |")
    print("+--------------------------------------------------+")
    print("| 1) Palermo                                       |")
    print("| 2) Puerto Madero                                 |")
    print("| 3: Nordelta                                      |")
    print("| 4: San Telmo                                     |")
    print("| 5: Recoleta                                      |")
    print("|--------------------------------------------------|")
    print("| 0) Cancelar                                      |")
    print("+--------------------------------------------------+")
    
def interfaz_tipo_turno():
    print("\n+--------------------------------------------------+")
    print("|                SELECCIONE TURNO                  |")
    print("+--------------------------------------------------+")
    print("| 1) Mañana                                        |")
    print("| 2) Tarde                                         |")
    print("| 3: Noche                                         |")
    print("|--------------------------------------------------|")
    print("| 0) Cancelar                                      |")
    print("+--------------------------------------------------+")
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
def diasDelMes(año, mes):
    """
        Lista de días por mes. Febrero depende de si es bisiesto.
    """
    dias_en_mes = [31, 29 if esBisiesto(año) else 28, 31, 30, 31, 30,
                   31, 31, 30, 31, 30, 31]
    return dias_en_mes[mes - 1]
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
            entrada_eliminar = input("Número del servicio a eliminar: ").strip()

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
def eliminarEvento(calendario):
    seleccion = seleccionar_fecha_salon_turno(calendario)
    if not seleccion:
        print("Eliminación cancelada.")
        return
    fecha, salon, turno = seleccion
    clave = (fecha, salon, turno)
    cliente = calendario[clave]["cliente"]
    calendario.pop(clave)
    print(f"Eliminando evento de '{cliente}' el {fecha} en Salón {salon}, Turno {turno}.")

#===================================================================================================================================
def traerDeArchivoLosServicios():#***
    servicios = {}
    try:
        archivo = open("servicios.csv", "rt")
        for linea in archivo:
            partes = linea.strip().split(",")
            if len(partes) == 3:
                nombre,precio,tipo = partes
                servicios[nombre] = {"precio": precio, "tipo": tipo}
    except FileNotFoundError:
        print("Archivo de servicios no encontrado. por favor cargue el archivo")
    except OSError as mensaje:
        print("Error al buscar servicios", mensaje)
    finally:
        try:
            archivo.close()
        except NameError:
            pass
    return servicios    
#===================================================================================================================================
def cargarNuevoServicioACsv(servicioACargar):
    try:
        archivo = open("servicios.csv", "at")
        nombre = servicioACargar[0]
        precio = servicioACargar[1]
        tipo = servicioACargar[2]
        linea = f"{nombre},{precio},{tipo}\n"
        archivo.write(linea)
    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)
    finally:
        try:
            archivo.close()
        except NameError:
            pass
#===================================================================================================================================
def buscarEvento(calendario):
    seleccion = seleccionar_fecha_salon_turno(calendario)
    if not seleccion:
        print("Búsqueda cancelada.")
        return
    fecha, salon, turno = seleccion
    clave = (fecha, salon, turno)
    imprimirEvento(clave, calendario[clave])

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
def seleccionar_tipo_evento():#***
    """
    Muestra un menú para seleccionar el tipo de evento.
    Devuelve el nombre del evento seleccionado o None si se cancela.
    """
    tipos_evento = ["Fiesta de egresados","Casamiento","Cumple de XV","Despedida de soltero","Evento empresarial","Conferencia"]
    interfaz_tipo_evento()

    while True:
        opcion = input(f"Seleccione una opción (1-{len(tipos_evento)} o 0 para cancelar): ").strip()
        if opcion == "0":
            return None
        if opcion.isdigit() and 1 <= int(opcion) <= len(tipos_evento):
            return tipos_evento[int(opcion) - 1]
        print("Opción inválida. Intente nuevamente.")
        
def seleccionar_salon():#***
    """
    Muestra un menú para seleccionar un salón.
    Devuelve el nombre del salón seleccionado o None si se cancela.
    """
    SALONES = ["Palermo","Puerto Madero","Nordelta","San Telmo","Recoleta"]
    interfaz_tipo_salon()

    while True:
        opcion = input(f"Seleccione un salón (1-{len(SALONES)} o 0 para cancelar): ").strip()
        if opcion == "0":
            return None
        if opcion.isdigit() and 1 <= int(opcion) <= len(SALONES):
            return SALONES[int(opcion) - 1]
        print("Opción inválida. Intente nuevamente.")

def seleccionar_turno(): #***
    """
    Muestra un menú para seleccionar un turno.
    Devuelve el nombre del turno seleccionado o None si se cancela.
    """
    TURNOS  = ["Mañana","Tarde","Noche"]
    interfaz_tipo_turno()

    while True:
        opcion = input(f"Seleccione un salón (1-{len(TURNOS)} o 0 para cancelar): ").strip()
        if opcion == "0":
            return None
        if opcion.isdigit() and 1 <= int(opcion) <= len(TURNOS):
            return TURNOS[int(opcion) - 1]
        print("Opción inválida. Intente nuevamente.")

#===================================================================================================================================
def opcionCrearEvento(calendario, servicios_disponibles):
    # 1) Cliente
    interfaz_crear_evento()
    cliente = input("Ingrese su nombre: ").strip().title()

    # 2) Tipo de evento
    tipo_evento = seleccionar_tipo_evento()
    if tipo_evento is None:
        return
    
    # 3) Cantidad de personas
    while True:
        val = input("Cantidad de personas: ").strip()
        if val.isdigit() and int(val) > 0:
            cant = int(val)
            break
        print("Por favor ingrese un número entero positivo.")

    # 4) Fecha
    while True:
        fecha = input("Fecha del evento (YYYY-MM-DD): ").strip()
        if validarFecha(fecha):
            break
        print("Formato inválido. Use YYYY-MM-DD.")

    # 5) Salón
    salon = seleccionar_salon()
    if salon is None:
        return

    # 6) Turno
    turno = seleccionar_turno()
    if turno is None:
        return

    # 7) Validar capacidad
    max_cap = capacidades_salones[salon]
    while cant > max_cap:
        print(f"El salón {salon} admite hasta {max_cap} personas.")
        val = input(f"Ingrese una cantidad ≤ {max_cap}: ").strip()
        if val.isdigit() and 1 <= int(val) <= max_cap:
            cant = int(val)
            break
        print("Entrada inválida.")

    # 8) Construir servicios
    servicios_evento = servicios_disponibles.copy()
    servicios_evento[f"Catering Básico   ({cant}×)"]   = PRECIO_CATERING_BASIC   * cant
    servicios_evento[f"Catering Estándar ({cant}×)"]   = PRECIO_CATERING_STD     * cant
    servicios_evento[f"Catering Premium  ({cant}×)"]   = PRECIO_CATERING_PREMIUM * cant
    m = math.ceil(cant / 4)
    servicios_evento[f"Moso x{m}"]      = PRECIO_MOSO      * m
    b = math.ceil(cant / 20)
    servicios_evento[f"Bartender x{b}"] = PRECIO_BARTENDER * b
    g = math.ceil(cant / 30)
    servicios_evento[f"Guardia x{g}"]   = PRECIO_SEGURIDAD * g

    # 9) Selección de servicios
    servicios, precios = seleccionar_servicios(servicios_evento)
    subtotal = sum(precios)
    limpieza = subtotal * PORCENTAJE_LIMPIEZA
    servicios.append("Limpieza post-evento (5%)")
    precios.append(limpieza)

    # 10) Registrar y mostrar evento
    evento = crearEvento(cliente, tipo_evento, cant, servicios, precios)
    agregarEventoACalendario(calendario, fecha, salon, turno, evento)
    imprimirEvento((fecha, salon, turno), evento)
    return

#===================================================================================================================================
def seleccionar_fecha_salon_turno(calendario):
    """
    Permite seleccionar una fecha, salón y turno de entre los eventos existentes en el calendario.
    Valida cada paso mostrando solo las opciones disponibles.
    Devuelve: (fecha, salon, turno) o None si se cancela.
    """

    if not calendario:
        print("No hay eventos registrados en el calendario.")
        return None

    # Paso 1: Mostrar fechas disponibles
    lista_fechas = sorted(set(clave_evento[0] for clave_evento in calendario))
    print("\nFechas disponibles:")
    for indice, fecha in enumerate(lista_fechas, 1):
        print(f"{indice}) {fecha}")
    print("0) Cancelar")

    while True:
        entrada = input(f"Seleccione una fecha (1-{len(lista_fechas)}): ").strip()
        if entrada == "0":
            return None
        if entrada.isdigit() and 1 <= int(entrada) <= len(lista_fechas):
            fecha_seleccionada = lista_fechas[int(entrada) - 1]
            break
        print("Opción inválida. Intente nuevamente.")

    # Paso 2: Mostrar salones disponibles para esa fecha
    lista_salones = sorted(set(clave_evento[1] for clave_evento in calendario if clave_evento[0] == fecha_seleccionada))
    print(f"\nSalones disponibles para {fecha_seleccionada}:")
    for indice, salon in enumerate(lista_salones, 1):
        print(f"{indice}) {salon}")
    print("0) Cancelar")

    while True:
        entrada = input(f"Seleccione un salón (1-{len(lista_salones)}): ").strip()
        if entrada == "0":
            return None
        if entrada.isdigit() and 1 <= int(entrada) <= len(lista_salones):
            salon_seleccionado = lista_salones[int(entrada) - 1]
            break
        print("Opción inválida. Intente nuevamente.")

    # Paso 3: Mostrar turnos disponibles para esa fecha y salón
    lista_turnos = sorted(set(clave_evento[2] for clave_evento in calendario if clave_evento[0] == fecha_seleccionada and clave_evento[1] == salon_seleccionado))
    print(f"\nTurnos disponibles para {salon_seleccionado} el {fecha_seleccionada}:")
    for indice, turno in enumerate(lista_turnos, 1):
        print(f"{indice}) {turno}")
    print("0) Cancelar")

    while True:
        entrada = input(f"Seleccione un turno (1-{len(lista_turnos)}): ").strip()
        if entrada == "0":
            return None
        if entrada.isdigit() and 1 <= int(entrada) <= len(lista_turnos):
            turno_seleccionado = lista_turnos[int(entrada) - 1]
            break
        print("Opción inválida. Intente nuevamente.")

    return (fecha_seleccionada, salon_seleccionado, turno_seleccionado)
##################################  PROGRAMA PRINCIPAL ###########################################
# Mientras la opción sea distinta de 6 (Salir)
while True:
    interfaz_bienvenida_gestor_eventos()
    # Ingresamos por teclado la opcion a elegir
    opcion = input("Seleccione una opción (1-6): ").strip()
    # Si la opción es válida entre 1 y 5
    if opcion == "1":  # ---------------- CREAR UN EVENTO ---------------------
        opcionCrearEvento(calendario, servicios_disponibles)
    elif opcion == "2":  # ---------------- VER TODOS LOS EVENTOS ---------------------
        interfaz_ver_evento()
        if calendario:  # si hay eventos
            imprimir_eventos(calendario)
        else:
            print("No hay eventos cargados en el calendario.")
    elif opcion == "3": # ---------------- ELIMINAR UN EVENTO ---------------------
        interfaz_eliminar_evento()
        eliminarEvento(calendario)
    elif opcion == "4": # ---------------- IMPRIMIR EL CALENDARIO ---------------------
        interfaz_mostrar_calendario()
        while True:
            año_str = input("Ingrese el año a visualizar: ").strip()
            if año_str.isdigit() and 1000 <= int(año_str) <= 9999:
                año = int(año_str)
                break
            print("Ingrese un año válido (ej: 2025).")
        mostrarCalendario(año, calendario)
    elif opcion == "5": # ---------------- BUSCAR UN EVENTO ---------------------
        interfaz_buscar_evento()
        buscarEvento(calendario)
           
    elif opcion == "6": # ---------------- SALIR DEL PROGRAMA ---------------------
        interfaz_salir_gestor_eventos()
        interfaz_salir_programa()
        break
    else:
        print("Opción inválida. Intente con un número del 1 al 6.")
#===================================================================================================================================
