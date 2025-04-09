# Diccionario de eventos por cliente
eventos = {
    "Martina": {
        "evento": "Casamiento",
        "fecha": "2025-05-12",
        "servicios": ["Cant_personas (100)", "Catering", "DJ", "Decoración", "Fotografía"],
        "precios": [5000, 200000, 80000, 60000, 45000]
    },
    "Carlos": {
        "evento": "Cumpleaños",
        "fecha": "2025-06-01",
        "servicios": ["Cant_personas (50)", "Catering", "DJ"],
        "precios": [2500, 90000, 50000]
    },
    "Lucía": {
        "evento": "Conferencia",
        "fecha": "2025-04-25",
        "servicios": ["Cant_personas (150)", "Sonido", "Pantalla gigante", "Catering"],
        "precios": [7500, 30000, 45000, 150000]
    }
}

# Función para imprimir los eventos ordenados por costo total
def imprimir_eventos(diccionario):
    total_general = 0
    lista_eventos = []

    # Crear lista auxiliar con totales
    for cliente, datos in diccionario.items():
        total = 0
        for precio in datos["precios"]:
            total += precio
        lista_eventos.append({
            "cliente": cliente,
            "evento": datos["evento"],
            "fecha": datos["fecha"],
            "servicios": datos["servicios"],
            "precios": datos["precios"],
            "total": total
        })

    # Ordenar eventos por total (mayor a menor)
    for i in range(len(lista_eventos)):
        for j in range(i + 1, len(lista_eventos)):
            if lista_eventos[j]["total"] > lista_eventos[i]["total"]:
                aux = lista_eventos[i]
                lista_eventos[i] = lista_eventos[j]
                lista_eventos[j] = aux

    # Imprimir eventos
    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║                  DETALLE DE EVENTOS CON FECHAS                     ║")
    print("╚════════════════════════════════════════════════════════════════════╝")
    
    for e in lista_eventos:
        print(f"\nCliente: {e['cliente']}")
        print(f"Tipo de Evento: {e['evento']}")
        print(f"Fecha: {e['fecha']}")
        print("┌────────────────────────────────┬────────────┐")
        print("│          Servicio              │   Precio   │")
        print("├────────────────────────────────┼────────────┤")
        for i in range(len(e["servicios"])):
            print(f"│ {e['servicios'][i]:<30} │ ${e['precios'][i]:<10}│")
        print("└────────────────────────────────┴────────────┘")
        print(f"TOTAL del evento: ${e['total']}")
        total_general += e["total"]

    print("\n════════════════════════════════════════════════════════════════════")
    print(f"TOTAL GENERAL INGRESADO POR TODOS LOS EVENTOS: ${total_general}")
    print("════════════════════════════════════════════════════════════════════")

# Llamada a la función
imprimir_eventos(eventos)
