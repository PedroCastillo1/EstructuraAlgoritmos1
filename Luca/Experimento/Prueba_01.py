# Variables globales
salones = []  # Matriz para almacenar salones
eventos = {}  # Diccionario para gestionar eventos y participantes
servicios = []  # Lista de servicios seleccionados

# Función recursiva para calcular asistencia
def calcular_asistencia(asistentes, index=0):
    return 0 if index >= len(asistentes) else asistentes[index] + calcular_asistencia(asistentes, index + 1)

# Validación de entrada numérica
def validar_entero(valor):
    return valor.isdigit()

# Registro de salones
def registrar_salon():
    nombre = input("Nombre del salón: ")
    ubicacion = input("Ubicación del salón: ")
    capacidad = input("Capacidad máxima: ")
    
    while not validar_entero(capacidad):
        print("Error: La capacidad debe ser un número entero.")
        capacidad = input("Capacidad máxima: ")
    
    disponibilidad = input("¿Está disponible? (si/no): ").lower()
    salones.append([nombre, ubicacion, int(capacidad), disponibilidad])

# Selección de servicios
def seleccionar_servicios():
    opciones = ["Catering", "Decoración", "Entretenimiento", "Logística"]
    print("\nSeleccione los servicios para el evento (1-4, separados por comas):")
    print("1. Catering\n2. Decoración\n3. Entretenimiento\n4. Logística")

    seleccion = input("Ingrese opciones: ").split(",")
    for opcion in seleccion:
        if validar_entero(opcion) and 1 <= int(opcion) <= 4:
            servicios.append(opciones[int(opcion) - 1])

# Registro de eventos
def registrar_evento():
    nombre = input("Nombre del evento: ")
    fecha = input("Fecha (DD/MM/AAAA): ")
    asistentes = input("Número de asistentes: ")

    while not validar_entero(asistentes):
        print("Error: El número de asistentes debe ser un entero positivo.")
        asistentes = input("Número de asistentes: ")

    participantes = []
    for i in range(int(asistentes)):
        participante = input(f"Ingrese el nombre del participante {i + 1}: ")
        participantes.append(participante)

    eventos[nombre] = {
        "fecha": fecha,
        "asistentes": participantes,
        "servicios": servicios,
        "confirmados": calcular_asistencia([1 for _ in participantes])  # Uso de recursividad
    }

# Guardar datos en archivo
def guardar_datos():
    archivo = open("eventos.txt", "w")
    archivo.write(str(salones) + "\n")
    archivo.write(str(eventos) + "\n")
    archivo.close()
    print("Datos guardados exitosamente.")

# Cargar datos desde archivo
def cargar_datos():
    global salones, eventos
    try:
        archivo = open("eventos.txt", "r")
        lineas = archivo.readlines()
        salones = eval(lineas[0].strip())
        eventos = eval(lineas[1].strip())
        archivo.close()
        print("Datos cargados correctamente.")
    except:
        print("Error al cargar el archivo.")

# Mostrar resumen de eventos
def mostrar_resumen():
    print("\nResumen de eventos:")
    for nombre, detalles in eventos.items():
        print(f"Evento: {nombre}")
        print(f"Fecha: {detalles['fecha']}")
        print(f"Asistentes: {len(detalles['asistentes'])}")
        print(f"Confirmados: {detalles['confirmados']}")
        print(f"Servicios: {', '.join(detalles['servicios'])}")
        print("-" * 30)

# Flujo de la aplicación
cargar_datos()
registrar_salon()
seleccionar_servicios()
registrar_evento()
guardar_datos()
mostrar_resumen()

