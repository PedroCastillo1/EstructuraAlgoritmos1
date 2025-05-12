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
def seleccionarServicios(servicios_disponibles):
    servicios, precios, seleccionados = [], [], []
    while True:
        print("\n🎛 Servicios disponibles para seleccionar:")
        disponibles = [s for s in servicios_disponibles if s not in seleccionados]
        for i, s in enumerate(disponibles, 1):
            print(f"{i}. {s} - ${servicios_disponibles[s]}")
        opt_eliminar = len(disponibles) + 1
        opt_finalizar = len(disponibles) + 2
        print(f"{opt_eliminar}. ❌ Eliminar un servicio elegido")
        print(f"{opt_finalizar}. ✅ Finalizar selección de servicios")
        entrada = input("Elegí una opción: ").strip()
        if not entrada.isdigit():
            print("❌ Entrada inválida.")
            continue
        eleccion = int(entrada)
        if 1 <= eleccion <= len(disponibles):
            s = disponibles[eleccion - 1]
            seleccionados.append(s)
            servicios.append(s)
            precios.append(servicios_disponibles[s])
            print(f"✅ '{s}' agregado.")
        elif eleccion == opt_eliminar:
            if not servicios:
                print("⚠️ Aún no hay servicios que eliminar.")
                continue
            print("\n🗑 Servicios ya elegidos:")
            for idx, s in enumerate(servicios, 1):
                print(f"{idx}. {s}")
            q = input("Número del servicio a eliminar: ").strip()
            if q.isdigit():
                idx = int(q)
                if 1 <= idx <= len(servicios):
                    eliminado = servicios.pop(idx - 1)
                    precios.pop(idx - 1)
                    seleccionados.remove(eliminado)
                    print(f"❌ '{eliminado}' eliminado.")
                else:
                    print("Número inválido.")
            else:
                print("Entrada inválida.")
        elif eleccion == opt_finalizar:
            if not servicios:
                print("⚠️ No podés finalizar sin al menos un servicio.")
            else:
                print("✅ Finalizando selección...")
                break
        else:
            print("❌ Opción no válida.")
    return servicios, precios
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
def eliminarEvento(calendario, fecha, salon, turno):
    # Crea una clave compuesta (una tupla) con los tres datos que identifican un evento único
    clave = (fecha, salon, turno)
    # Verifica si la fecha ingresada es válida llamando a la función validarFecha
    # Si no lo es, se muestra un mensaje y se sale de la función
    if not validarFecha(fecha):
        print("Fecha inválida.")
        return
    # Verifica si la clave existe en el diccionario calendario (es decir, si hay un evento en esa fecha, salón y turno)
    if clave in calendario:
        # Obtiene el nombre del cliente que reservó el evento, accediendo al valor almacenado en esa clave
        cliente = calendario[clave]["cliente"]
        # Elimina del calendario ese evento usando el método pop()
        calendario.pop(clave)
        # Muestra un mensaje confirmando que el evento fue eliminado
        print(f"Eliminando evento de '{cliente}' el {fecha} en Salón {salon}, Turno {turno}.")
    else:
        # Si la clave no existe, muestra un mensaje indicando que no se encontró ningún evento
        print(f"No hay eventos el {fecha} en Salón {salon}, Turno {turno}.")
#===================================================================================================================================
def buscarEvento(calendario, fecha, salon, turno):
    # Crea una clave única con los datos ingresados: fecha, salón y turno
    clave = (fecha, salon, turno)
    # Verifica si la fecha ingresada es válida utilizando la función validarFecha
    # Si la fecha no es válida, muestra un mensaje y finaliza la función
    if not validarFecha(fecha):
        print("Fecha inválida.")
        return
    # Verifica si existe un evento en el calendario con esa clave
    if clave in calendario:
        # Si existe, llama a la función imprimirEvento para mostrar los datos del evento
        imprimirEvento(clave, calendario[clave])
    else:
        # Si no existe, informa al usuario que no se encontró ningún evento en esa fecha, salón y turno
        print(f"No hay eventos el {fecha} en Salón {salon}, Turno {turno}.")
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
def opcionCrearEvento(calendario, servicios_disponibles):
    interfaz_crear_evento()
    
    """
        ACA VAMOS A TENER QUE AGREGAR LOS NUEVOS PARAMETROS QUE VA A TENER EL EVENTO 
                Diccionario {(CLAVE),[VALORES]}
        Diccionario eventos {(fecha,salon,turno),[cliente,tipoevento,cantpersonas]}
        
        (FECHA -- SALON -- TURNO) PARTE DE LA CLAVE
        (CLIENTE -- TIPO DE EVENTO -- CANTIDAD DE PERSONAS -- ETC) PARTE DE LOS VALORES
          
    """
    cliente = input("Ingrese su nombre: ").strip().title()
    tipo = input("Ingrese el tipo de evento: ").strip().capitalize()
    while True:
        val = input("Ingrese la cantidad de personas: ").strip()
        if val.isdigit() and int(val) > 0:
            cant = int(val)
            break
        print("Ingrese un número entero positivo.")
    fecha = input("Ingrese la fecha del evento (YYYY-MM-DD): ").strip()
    while not validarFecha(fecha):
        fecha = input("Fecha inválida. Intente nuevamente (YYYY-MM-DD): ").strip()
    
    """
        MODIFICAR LOS INGRESOS DE POR TECLADO POR OPCIONES (EJ 1,2,3) SIMPLIFICARLO ⚠️⚠️⚠️⚠️⚠️
    """    
        
    salon = input("Ingrese el nombre del salón: ").strip().capitalize()
    turno = input("Ingrese el turno (Mañana/Tarde/Noche): ").strip().capitalize()
    servicios, precios = [f"CantPersonas({cant})"], [cant * 1000]
    sel, pre = seleccionarServicios(servicios_disponibles)
    servicios.extend(sel)
    precios.extend(pre)
    """
        VERIFICAR QUE TODO LO QUE SE USE EN LA FUNCION SE LEGAL ⚠️⚠️⚠️⚠️⚠️
    """ 
    evento = crearEvento(cliente, tipo, cant, servicios, precios)
    agregarEventoACalendario(calendario, fecha, salon, turno, evento)
    imprimirEvento((fecha, salon, turno), evento)
    return
#===================================================================================================================================
##################################  PROGRAMA PRINCIPAL ###########################################
#Creamos el diccionario Calendario
calendario = {}
#Creamos el diccionario con los servicios disponibles
servicios_disponibles = {
    "Catering Caro": 200000,
    "Catering Barato": 75000,
    "DJ": 50000,
    "Fotógrafo": 20000
}
#===================================================================================================================================
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
            f = input("Ingrese la fecha (YYYY-MM-DD): ").strip()
            s = input("Ingrese el salón: ").strip().capitalize()
            t = input("Ingrese el turno (Mañana/Tarde/Noche): ").strip().capitalize()
            eliminarEvento(calendario, f, s, t)
    elif opcion == "4": # ---------------- IMPRIMIR EL CALENDARIO ---------------------
        interfaz_mostrar_calendario()
        while True:
            año_str = input("Ingrese el año a visualizar: ").strip()
            if ((año_str.isdigit() and 1000) <= (int(año_str) <= 9999)):
                año = int(año_str)
                break
            print("Ingrese un año válido (ej: 2025).")
        mostrarCalendario(año, calendario)
    elif opcion == "5": # ---------------- BUSCAR UN EVENTO ---------------------
        interfaz_buscar_evento()
        f = input("Ingrese la fecha (YYYY-MM-DD): ").strip()
        s = input("Ingrese el salón: ").strip().capitalize()
        t = input("Ingrese el turno (Mañana/Tarde/Noche): ").strip().capitalize()
        buscarEvento(calendario, f, s, t)
            
    elif opcion == "6": # ---------------- SALIR DEL PROGRAMA ---------------------
        interfaz_salir_gestor_eventos()
        interfaz_salir_programa()
        break
    else:
        print("Opción inválida. Intente con un número del 1 al 6.")
#===================================================================================================================================
