# Función para verificar si un año es bisiesto
def es_bisiesto(anio):
    # Un año es bisiesto si es divisible por 4 y no divisible por 100,
    # a menos que también sea divisible por 400.
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return True
    return False

# Función que devuelve el día de la semana usando el algoritmo de Zeller
def diadelasemana(dia, mes, anio):
    # Para enero y febrero, se consideran como meses 13 y 14 del año anterior
    if mes < 3:
        mes += 10
        anio -= 1
    else:
        mes -= 2
    # Se separa el siglo y el año
    siglo = anio // 100
    anio2 = anio % 100
    # Fórmula de Zeller para obtener el día de la semana (0=domingo, ..., 6=sábado)
    diassem = (((26 * mes - 2) // 10) + dia + anio2 + (anio2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    # Si es negativo, se ajusta sumando 7
    if diassem < 0:
        diassem += 7
    return diassem




# Función para validar una fecha ingresada
def validar_fecha(fecha):
    """
        En esta funcion se estaran validando la fecha ingresada si cumple con los rangos permitidos,
        Tomando como fecha desde una cadena de texto en formato "YYYY-MM-DD" pasa a ["2025", "04", "10"]
    
    """
    partes = fecha.split("-") #  "2025-04-10" -----> ["2025", "04", "10"]
    if len(partes) != 3: # Si el usuario ingresa mal la fecha (falta un parametro) retorna FALSE
        print("Formato de fecha incorrecto. Use el formato YYYY-MM-DD.")
        return False

    #Separamos en partes la fecha ingresada en 3 Variables
    anio_str = partes[0]
    mes_str = partes[1]
    dia_str = partes[2]

    # Validar que todos sean dígitos
    if not (anio_str.isdigit() and mes_str.isdigit() and dia_str.isdigit()):
        print("La fecha debe contener solo números en el formato YYYY-MM-DD.")
        return False

    #Convertimos para una de las partes en numeros enteros
    anio = int(anio_str)
    mes = int(mes_str)
    dia = int(dia_str)

    #Verificamos el rango del MES
    if mes < 1 or mes > 12:
        print("Mes inválido. Debe estar entre 1 y 12.")
        return False

    #Verificamos el rango del DIA ----> Llamamos a la funcioin dias_del_mes
    if dia < 1 or dia > dias_del_mes(anio, mes):
        print("Día inválido para el mes ingresado.")
        return False
    return True


# Función para obtener los días de un mes según si es bisiesto o no
def dias_del_mes(anio, mes):
    # Lista de días por mes. Febrero depende de si es bisiesto.
    dias_en_mes = [31, 29 if es_bisiesto(anio) else 28, 31, 30, 31, 30,
                   31, 31, 30, 31, 30, 31]
    return dias_en_mes[mes - 1]

# Función para mostrar el calendario anual
def mostrar_calendario(anio):
    # Nombres de los meses
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    # Recorre cada mes del año
    for mes in range(1, 13):
        print("\n" + meses[mes - 1] + " " + str(anio))
        print("Do Lu  Ma  Mi Ju  Vi  Sa")  # Encabezado de días

        primer_dia_semana = diadelasemana(1, mes, anio)  # Día de la semana del 1° del mes
        print("   " * primer_dia_semana, end="")  # Espacios hasta el primer día

        dia_actual = 1
        dias_mes = dias_del_mes(anio, mes)
        dia_semana = primer_dia_semana

        # Imprimir todos los días del mes
        while dia_actual <= dias_mes:
            fecha_actual = f"{anio:04d}-{mes:02d}-{dia_actual:02d}"  # Formato completo

            # Si la fecha está en eventos, se marca entre corchetes
            if fecha_actual in eventos:
                print(f"[{dia_actual:2d}]", end=" ")
            else:
                print(f" {dia_actual:2d} ", end="")

            dia_semana += 1
            if dia_semana == 7:
                print()  # Salto de línea al terminar la semana
                dia_semana = 0
            dia_actual += 1
        print()  # Línea en blanco al final de cada mes

# Función para agregar un evento
def agregar_evento(eventos):
    fecha = input("Ingresa la fecha del evento (YYYY-MM-DD): ")
    if not validar_fecha(fecha):
        return

    if fecha in eventos:
        opcion = input(f"Ya existe un evento en {fecha}. ¿Desea sobrescribirlo? (S/N): ")
        if opcion != "S" and opcion != "s":
            print(" No se realizó ningún cambio.")
            return

    nombre = input("- Nombre del evento: ")
    hora = input("- Hora (HH:MM AM/PM): ")
    ubicacion = input("- Ubicación: ")

    eventos[fecha] = {"nombre": nombre, "hora": hora, "ubicación": ubicacion}
    print(f"Evento '{nombre}' agregado el {fecha}.")


# Función para eliminar un evento
def eliminar_evento(eventos):
    fecha = input("Ingresa la fecha del evento a eliminar (YYYY-MM-DD): ")
    if not validar_fecha(fecha):
        return

    if fecha in eventos:
        print(f"Eliminando '{eventos[fecha]['nombre']}' el {fecha}.")
        del eventos[fecha]
    else:
        print(f"No hay eventos el {fecha}.")

# Función para buscar un evento
def buscar_evento(eventos):
    fecha = input("Ingresa la fecha del evento a buscar (YYYY-MM-DD): ")
    if not validar_fecha(fecha):
        return

    if fecha in eventos:
        evento = eventos[fecha]
        print(f"- Evento encontrado: '{evento['nombre']}'")
        print(f"   - Hora: {evento['hora']}")
        print(f"   - Ubicación: {evento['ubicación']}")
    else:
        print(f"No hay eventos el {fecha}.")


# Diccionario para almacenar eventos
eventos = {}

# Menú principal con recursividad
def menu(eventos):
    print("\n================================")
    print("     GESTOR DE EVENTOS")
    print("================================")
    print("1. Agregar evento")
    print("2. Eliminar evento")
    print("3. Buscar evento")
    print("4. Mostrar calendario")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_evento(eventos)
        menu(eventos)
    elif opcion == "2":
        eliminar_evento(eventos)
        menu(eventos)
    elif opcion == "3":
        buscar_evento(eventos)
        menu(eventos)
    elif opcion == "4":
        anio = int(input("Ingresa el año: "))
        mostrar_calendario(anio)
        menu(eventos)
    elif opcion == "5":
        print("Saliendo del sistema. ¡Hasta pronto!")
    else:
        print("Opción no válida. Intenta nuevamente.")
        menu(eventos)


# Llamada inicial (asumiendo que ya existe una lista llamada eventos)

#PROGRAMA PRINCIPAL
menu(eventos)
