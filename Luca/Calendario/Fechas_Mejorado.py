# 📌 Función para verificar si un año es bisiesto

def es_bisiesto(anio):
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return True
    return False

# 📌 Función para validar una fecha ingresada

def validar_fecha(fecha):
    partes = fecha.split("-")
    if len(partes) != 3:
        print("⚠️ Formato de fecha incorrecto. Use el formato YYYY-MM-DD.")
        return False

    anio = int(partes[0])
    mes = int(partes[1])
    dia = int(partes[2])

    if mes < 1 or mes > 12:
        print("⚠️ Mes inválido. Debe estar entre 1 y 12.")
        return False

    if dia < 1 or dia > dias_del_mes(anio, mes):
        print("⚠️ Día inválido para el mes ingresado.")
        return False

    return True

# 📌 Función para obtener los días de un mes

def dias_del_mes(anio, mes):
    dias_por_mes = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if mes == 2 and es_bisiesto(anio):
        return 29
    return dias_por_mes[mes]

# 📌 Función para mostrar el calendario con eventos

def mostrar_calendario(eventos, anio, mes):
    if mes < 1 or mes > 12 or anio < 1:
        print("⚠️ Año o mes inválido.")
        return

    dias_mes = dias_del_mes(anio, mes)
    print(f"\n📆 Calendario de {mes:02d}-{anio}\n")
    print(" Lu  Ma  Mi  Ju  Vi  Sa  Do")

    dia_semana = (anio + anio//4 - anio//100 + anio//400 + (31*(mes-1))//12) % 7
    dia_semana = (dia_semana + 5) % 7
    print("    " * dia_semana, end="")

    for dia in range(1, dias_mes + 1):
        fecha = f"{anio}-{mes:02d}-{dia:02d}"
        if fecha in eventos:
            print(f"[{dia:02d}]", end=" ")
        else:
            print(f" {dia:02d} ", end=" ")

        dia_semana += 1
        if dia_semana == 7:
            dia_semana = 0
            print()
    print("\n")

# 📌 Función para agregar un evento

def agregar_evento(eventos):
    fecha = input("📅 Ingresa la fecha del evento (YYYY-MM-DD): ")

    if not validar_fecha(fecha):
        return

    if fecha in eventos:
        opcion = input(f"⚠️ Ya existe un evento en {fecha}. ¿Desea sobrescribirlo? (S/N): ")
        if opcion != "S" and opcion != "s":
            print("❌ No se realizó ningún cambio.")
            return

    nombre = input("📝 Nombre del evento: ")
    hora = input("⏰ Hora (HH:MM AM/PM): ")
    ubicacion = input("📍 Ubicación: ")

    eventos[fecha] = {"nombre": nombre, "hora": hora, "ubicación": ubicacion}
    print(f"✅ Evento '{nombre}' agregado el {fecha}.")

# 📌 Función para eliminar un evento

def eliminar_evento(eventos):
    fecha = input("📅 Ingresa la fecha del evento a eliminar (YYYY-MM-DD): ")

    if not validar_fecha(fecha):
        return

    if fecha in eventos:
        print(f"🗑️ Eliminando '{eventos[fecha]['nombre']}' el {fecha}.")
        del eventos[fecha]
    else:
        print(f"⚠️ No hay eventos el {fecha}.")

# 📌 Función para buscar un evento

def buscar_evento(eventos):
    fecha = input("📅 Ingresa la fecha del evento a buscar (YYYY-MM-DD): ")

    if not validar_fecha(fecha):
        return

    if fecha in eventos:
        evento = eventos[fecha]
        print(f"🔍 Evento encontrado: '{evento['nombre']}'")
        print(f"   🕒 Hora: {evento['hora']}")
        print(f"   📍 Ubicación: {evento['ubicación']}")
    else:
        print(f"⚠️ No hay eventos el {fecha}.")

# 📌 Diccionario para almacenar eventos

eventos = {}

# 📌 Menú interactivo con recursividad
def menu(eventos):
    print("\n📅 GESTOR DE EVENTOS 📅")
    print("1️⃣ Agregar evento")
    print("2️⃣ Eliminar evento")
    print("3️⃣ Buscar evento")
    print("4️⃣ Mostrar calendario")
    print("5️⃣ Salir")

    opcion = input("👉 Elige una opción: ")

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
        anio = int(input("📅 Ingresa el año: "))
        mes = int(input("📅 Ingresa el mes (1-12): "))
        mostrar_calendario(eventos, anio, mes)
        menu(eventos)
    elif opcion == "5":
        print("👋 Saliendo del sistema. ¡Hasta pronto!")
    else:
        print("⚠️ Opción no válida. Intenta nuevamente.")
        menu(eventos)


# Llamada inicial (asumiendo que ya existe una lista llamada eventos)


#PROGRAMA PRINCIPAL
menu(eventos)
