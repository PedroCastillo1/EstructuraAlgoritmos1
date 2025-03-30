# Variables globales
salones = []  # Matriz para datos de salones
servicios_incluidos = ["Seguridad privada", "Personal de limpieza", "Transporte", "Valet parking"]
servicios_disponibles = {
    "Catering": [("Básico", 100), ("Intermedio", 150), ("Premium", 200)],
    "Decoración": ["Elegante", "Rústico", "Vintage", "Moderno"],
    "Entretenimiento y Tecnología": ["DJ", "Fiesta de espuma", "Pantallas LED", "Fotocabina"],
}
tipos_eventos = ["Sociales", "Corporativos", "Culturales y Especiales"]
eventos = {}

# Función recursiva para cálculo de mesas
def calcular_mesas(invitados, capacidad_mesa):
    return 1 if invitados <= capacidad_mesa else 1 + calcular_mesas(invitados - capacidad_mesa, capacidad_mesa)

# Validación de entrada numérica
def validar_entero(valor):
    return valor.isdigit()

# Configuración de salones
def agregar_salon():
    nombre = input("Nombre del salón: ")
    ubicacion = input("Ubicación del salón: ")
    capacidad = input("Capacidad máxima: ")

    while not validar_entero(capacidad):
        print("Error: La capacidad debe ser un número entero.")
        capacidad = input("Capacidad máxima: ")
    
    precio = input("Costo por evento: ")
    
    while not validar_entero(precio):
        print("Error: El costo debe ser un número entero.")
        precio = input("Costo por evento: ")

    salones.append([nombre, ubicacion, int(capacidad), int(precio)])

# Registro de eventos
def registrar_evento():
    nombre_evento = input("\nNombre del evento: ")
    fecha = input("Fecha (DD/MM/AAAA): ")
    tipo_evento = input("Tipo de evento (Sociales/Corporativos/Culturales y Especiales): ")

    while tipo_evento not in tipos_eventos:
        print("Tipo de evento no válido. Intente nuevamente.")
        tipo_evento = input("Tipo de evento (Sociales/Corporativos/Culturales y Especiales): ")

    invitados = input("Número de invitados: ")

    while not validar_entero(invitados):
        print("Error: Debe ser un número entero.")
        invitados = input("Número de invitados: ")

    invitados = int(invitados)
    capacidad_mesa = 10  # Asumimos mesas de 10 personas
    num_mesas = calcular_mesas(invitados, capacidad_mesa)

    # Selección de salón
    print("\nSeleccione un salón:")
    for i, salon in enumerate(salones):
        print(f"{i + 1}. {salon[0]} - Capacidad: {salon[2]} - Costo: {salon[3]}")
    opcion_salon = input("Elija un salón: ")

    # Selección de catering
    print("\nOpciones de Catering:")
    for i, (opcion, precio) in enumerate(servicios_disponibles["Catering"]):
        print(f"{i + 1}. {opcion} - Costo por plato: {precio}")
    opcion_catering = input("Elija una opción de catering: ")

    # Selección de entretenimiento y tecnología
    seleccion_servicios = []
    print("\nSeleccione entretenimiento y tecnología (puede elegir más de uno):")
    for i, servicio in enumerate(servicios_disponibles["Entretenimiento y Tecnología"]):
        print(f"{i + 1}. {servicio}")
    
    # Solicitamos la selección de entretenimiento y tecnología
    opciones_entretenimiento = input("Ingrese los números separados por comas: ").split(",")
    for opcion in opciones_entretenimiento:
        if validar_entero(opcion) and 1 <= int(opcion) <= len(servicios_disponibles["Entretenimiento y Tecnología"]):
            seleccion_servicios.append(servicios_disponibles["Entretenimiento y Tecnología"][int(opcion) - 1])
    
    # Cálculo de presupuesto
    costo_salon = salones[int(opcion_salon) - 1][3]
    costo_catering = servicios_disponibles["Catering"][int(opcion_catering) - 1][1] * invitados
    costo_servicios = len(seleccion_servicios) * 300  # Ejemplo: Cada servicio adicional cuesta $300
    costo_total = costo_salon + costo_catering + costo_servicios

    # Registro del evento
    eventos[nombre_evento] = {
        "fecha": fecha,
        "tipo": tipo_evento,
        "salon": salones[int(opcion_salon) - 1][0],
        "invitados": invitados,
        "mesas": num_mesas,
        "catering": servicios_disponibles["Catering"][int(opcion_catering) - 1][0],
        "servicios": seleccion_servicios,
        "costo_total": costo_total
    }

# Guardar datos en archivo
def guardar_datos():
    with open("eventos.txt", "w") as archivo:
        archivo.write(str(salones) + "\n")
        archivo.write(str(eventos) + "\n")

# Cargar datos desde archivo
def cargar_datos():
    global salones, eventos
    try:
        with open("eventos.txt", "r") as archivo:
            lineas = archivo.readlines()
            salones = eval(lineas[0].strip())
            eventos = eval(lineas[1].strip())
        print("Datos cargados correctamente.")
    except:
        print("No se encontraron datos previos.")

# Mostrar resumen de eventos
def mostrar_resumen():
    print("\nResumen de eventos registrados:")
    for nombre, detalles in eventos.items():
        print(f"Evento: {nombre}")
        print(f"Fecha: {detalles['fecha']}")
        print(f"Tipo: {detalles['tipo']}")
        print(f"Salón: {detalles['salon']}")
        print(f"Invitados: {detalles['invitados']}")
        print(f"Mesas: {detalles['mesas']}")
        print(f"Catering: {detalles['catering']}")
        print(f"Servicios adicionales: {', '.join(detalles['servicios'])}")
        print(f"Costo total: ${detalles['costo_total']}")
        print("-" * 30)

# Flujo de la aplicación
cargar_datos()
print("\n--- CONFIGURACIÓN INTERNA DE LA EMPRESA ---")
agregar_salon()

while True:
    print("\n--- GESTIÓN DE EVENTOS ---")
    registrar_evento()
    guardar_datos()
    mostrar_resumen()
    
    continuar = input("\n¿Registrar otro evento? (si/no): ").lower()
    if continuar != "si":
        break
