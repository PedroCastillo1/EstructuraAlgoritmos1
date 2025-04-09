# Matriz de eventos por cliente
eventos = [
    ["Martina", "Casamiento", ["Cant_personas (100)", "Catering", "DJ", "Decoración", "Fotografía"], [5000, 200000, 80000, 60000, 45000]],
    ["Carlos", "Cumpleaños", ["Cant_personas (50)", "Catering", "DJ"], [2500, 90000, 50000]],
    ["Lucía", "Conferencia", ["Cant_personas (150)", "Sonido", "Pantalla gigante", "Catering"], [7500, 30000, 45000, 150000]]
]

# Función para imprimir los eventos ordenados por costo total
def imprimir_eventos(matriz):
    total_general = 0
    eventos_con_totales = []

    # Calcular el total por evento y agregarlo a una lista nueva
    for fila in matriz:
        cliente = fila[0]
        tipo_evento = fila[1]
        servicios = fila[2]
        precios = fila[3]
        total = 0
        for precio in precios:
            total += precio
        eventos_con_totales.append([cliente, tipo_evento, servicios, precios, total])

    # Ordenar los eventos por total gastado (mayor a menor)
    for i in range(len(eventos_con_totales)):
        for j in range(i + 1, len(eventos_con_totales)):
            if eventos_con_totales[j][4] > eventos_con_totales[i][4]:
                aux = eventos_con_totales[i]
                eventos_con_totales[i] = eventos_con_totales[j]
                eventos_con_totales[j] = aux

    # Imprimir los eventos ordenados
    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║                 DETALLE DE EVENTOS EN SALÓN (ORDENADOS)            ║")
    print("╚════════════════════════════════════════════════════════════════════╝")
    
    for fila in eventos_con_totales:
        cliente = fila[0]
        tipo_evento = fila[1]
        servicios = fila[2]
        precios = fila[3]
        total = fila[4]

        print(f"\nCliente: {cliente}")
        print(f"Tipo de Evento: {tipo_evento}")
        print("┌────────────────────────────────┬────────────┐")
        print("│          Servicio              │   Precio   │")
        print("├────────────────────────────────┼────────────┤")

        for i in range(len(servicios)):
            print(f"│ {servicios[i]:<30} │ ${precios[i]:<10}│")
        
        print("└────────────────────────────────┴────────────┘")
        print(f"TOTAL del evento: ${total}")
        total_general += total

    print("\n════════════════════════════════════════════════════════════════════")
    print(f"TOTAL GENERAL INGRESADO POR TODOS LOS EVENTOS: ${total_general}")
    print("════════════════════════════════════════════════════════════════════")

# Llamada a la función
imprimir_eventos(eventos)
