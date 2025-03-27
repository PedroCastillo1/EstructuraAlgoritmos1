"""
    Necesitamos un algoritmo que se encargue de realizar las fechas de eventos a realizarse.
    
    Funciomes PRINCIPALES =
        - CREAR un evento en una fecha (Verificar DISPONIBILIDAD)
        - ELIMINAR un evento en una fecha (Verificar EXISTENCIA Y Actualizar DISPONIBILIDAD)
        - BUSCAR un evento si EXISTE
    
    Necesitaremos varias funciones como:
        - Fecha ingresada sea correcta (verificamos rangos de los valores y llamaremos funciones como si es una anio Bisiesto)
        - Fecha Disponible (Si es una fecha a realizarse, no se permiten fechas ya pasadas, y si esta disponible como para realizar un evento ese dia)
        - Una Funcion en la que se pueda visualizar con los dias/meses del anio las fechas para eventos
         
"""
# 📌 Función para verificar si un año es bisiesto
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# 📌 Función para obtener los días de un mes sin usar la librería calendar
def dias_del_mes(anio, mes):
    dias_por_mes = {
        1: 31,  2: 29 if es_bisiesto(anio) else 28,  3: 31,  4: 30,
        5: 31,  6: 30,  7: 31,  8: 31,  9: 30, 10: 31, 11: 30, 12: 31
    }
    return dias_por_mes.get(mes, 0)

# 📌 Función para mostrar el calendario con eventos
def mostrar_calendario(eventos, anio, mes):
    dias_mes = dias_del_mes(anio, mes)
    
    print(f"\n📆 Calendario de {mes:02d}-{anio}\n")
    print(" Lu  Ma  Mi  Ju  Vi  Sa  Do")

    # Algoritmo de Zeller simplificado para determinar el día de la semana del 1° del mes
    dia_semana = (anio + anio//4 - anio//100 + anio//400 + (31*(mes-1))//12) % 7
    dia_semana = (dia_semana + 5) % 7  # Ajuste para que el lunes sea el primer día
    
    print("    " * dia_semana, end="")

    for dia in range(1, dias_mes + 1):
        fecha = f"{anio}-{mes:02d}-{dia:02d}"
        if fecha in eventos:
            print(f"[{dia:02d}]", end=" ")  # Día ocupado con evento
        else:
            print(f" {dia:02d} ", end=" ")  # Día libre
        
        dia_semana += 1
        if dia_semana == 7:
            dia_semana = 0
            print()
    
    print("\n")  # Salto de línea al final

# 📌 Función para agregar un evento
def agregar_evento(eventos):
    fecha = input("📅 Ingresa la fecha del evento (YYYY-MM-DD): ")
    
    if fecha in eventos:
        print(f"⚠️ La fecha {fecha} ya tiene el evento '{eventos[fecha]['nombre']}'.")
        return

    nombre = input("📝 Nombre del evento: ")
    hora = input("⏰ Hora (HH:MM AM/PM): ")
    ubicacion = input("📍 Ubicación: ")

    eventos[fecha] = {"nombre": nombre, "hora": hora, "ubicación": ubicacion}
    print(f"✅ Evento '{nombre}' agregado el {fecha}.")

# 📌 Función para eliminar un evento
def eliminar_evento(eventos):
    fecha = input("📅 Ingresa la fecha del evento a eliminar (YYYY-MM-DD): ")

    if fecha in eventos:
        print(f"🗑️ Eliminando '{eventos[fecha]['nombre']}' el {fecha}.")
        del eventos[fecha]
    else:
        print(f"⚠️ No hay eventos el {fecha}.")

# 📌 Función para buscar un evento
def buscar_evento(eventos):
    fecha = input("📅 Ingresa la fecha del evento a buscar (YYYY-MM-DD): ")

    if fecha in eventos:
        evento = eventos[fecha]
        print(f"🔍 Evento encontrado: '{evento['nombre']}'")
        print(f"   🕒 Hora: {evento['hora']}")
        print(f"   📍 Ubicación: {evento['ubicación']}")
    else:
        print(f"⚠️ No hay eventos el {fecha}.")

# 📌 Diccionario para almacenar los eventos
eventos = {}

# 📌 Menú para interactuar con el sistema
while True:
    print("\n📅 GESTOR DE EVENTOS 📅")
    print("1️⃣ Agregar evento")
    print("2️⃣ Eliminar evento")
    print("3️⃣ Buscar evento")
    print("4️⃣ Mostrar calendario")
    print("5️⃣ Salir")
    
    opcion = input("👉 Elige una opción: ")

    if opcion == "1":
        agregar_evento(eventos)
    elif opcion == "2":
        eliminar_evento(eventos)
    elif opcion == "3":
        buscar_evento(eventos)
    elif opcion == "4":
        anio = int(input("📅 Ingresa el año: "))
        mes = int(input("📅 Ingresa el mes (1-12): "))
        mostrar_calendario(eventos, anio, mes)
    elif opcion == "5":
        print("👋 Saliendo del sistema. ¡Hasta pronto!")
        break
    else:
        print("⚠️ Opción no válida. Intenta nuevamente.")
