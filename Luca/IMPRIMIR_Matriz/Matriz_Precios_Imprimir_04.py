# Diccionario base de eventos
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


# Función para imprimir todos los eventos ordenados por total
def imprimir_eventos(diccionario):
    total_general = 0
    lista_eventos = []

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

    for i in range(len(lista_eventos)):
        for j in range(i + 1, len(lista_eventos)):
            if lista_eventos[j]["total"] > lista_eventos[i]["total"]:
                aux = lista_eventos[i]
                lista_eventos[i] = lista_eventos[j]
                lista_eventos[j] = aux

    print("\n╔════════════════════════════════════════════════════════════════════╗")
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

# Función para agregar un nuevo evento
def agregar_evento(diccionario):
    print("\n🆕 Agregar nuevo evento")
    cliente = input("Nombre del cliente: ")
    if cliente in diccionario:
        print("Ese cliente ya tiene un evento registrado.")
        return

    tipo_evento = input("Tipo de evento (Ej: Casamiento, Cumpleaños): ")
    fecha = input("Fecha del evento (formato AAAA-MM-DD): ")

    servicios_disponibles = {
        "Catering": 200000,
        "DJ": 80000,
        "Decoración": 60000,
        "Fotografía": 45000,
        "Pantalla gigante": 45000,
        "Sonido": 30000,
        "Cant_personas (50)": 2500,
        "Cant_personas (100)": 5000,
        "Cant_personas (150)": 7500
    }

    servicios = []
    precios = []
    seleccionados = []

    while True:
        print("\n🎛 Servicios disponibles para seleccionar:")
        opciones = []
        i = 1
        for servicio, precio in servicios_disponibles.items():
            if servicio not in seleccionados:
                print(f"{i}. {servicio} - ${precio}")
                opciones.append(servicio)
                i += 1

        opcion_eliminar = i
        opcion_finalizar = i + 1

        print(f"{opcion_eliminar}. ❌ Eliminar un servicio elegido")
        print(f"{opcion_finalizar}. ✅ Finalizar selección de servicios")

        eleccion = input("Elegí una opción: ")

        if eleccion.isdigit():
            eleccion = int(eleccion)
            if 1 <= eleccion <= len(opciones):
                servicio_elegido = opciones[eleccion - 1]
                seleccionados.append(servicio_elegido)
                servicios.append(servicio_elegido)
                precios.append(servicios_disponibles[servicio_elegido])
                print(f"✅ '{servicio_elegido}' agregado.")
            elif eleccion == opcion_eliminar:
                if not servicios:
                    print("⚠️ Aún no hay servicios que eliminar.")
                else:
                    print("\n🗑 Servicios ya elegidos:")
                    for idx, s in enumerate(servicios):
                        print(f"{idx + 1}. {s}")
                    quitar = input("Número del servicio a eliminar: ")
                    if quitar.isdigit():
                        quitar = int(quitar)
                        if 1 <= quitar <= len(servicios):
                            eliminado = servicios.pop(quitar - 1)
                            precios.pop(quitar - 1)
                            seleccionados.remove(eliminado)
                            print(f"❌ '{eliminado}' eliminado.")
                        else:
                            print("Número inválido.")
                    else:
                        print("Entrada inválida.")
            elif eleccion == opcion_finalizar:
                if not servicios:
                    print("⚠️ No podés finalizar sin al menos un servicio.")
                else:
                    print("✅ Finalizando selección...")
                    break
            else:
                print("❌ Opción no válida.")
        else:
            print("❌ Entrada inválida.")

    diccionario[cliente] = {
        "evento": tipo_evento,
        "fecha": fecha,
        "servicios": servicios,
        "precios": precios
    }
    print(f"\n🎉 Evento agregado exitosamente para {cliente}.")


# Función para buscar eventos por fecha
def buscar_eventos_por_fecha(diccionario, fecha_buscada):
    print(f"\n📅 Buscando eventos en la fecha: {fecha_buscada}")
    encontrados = False
    for cliente, datos in diccionario.items():
        if datos["fecha"] == fecha_buscada:
            print(f"\nCliente: {cliente}")
            print(f"Tipo de Evento: {datos['evento']}")
            print("Servicios contratados:")
            for i in range(len(datos["servicios"])):
                print(f"  - {datos['servicios'][i]}: ${datos['precios'][i]}")
            encontrados = True
    if not encontrados:
        print("❌ No se encontraron eventos en esa fecha.")

# Menú simple
def menu():
    while True:
        print("\n╔════════ MENÚ SALÓN DE EVENTOS ════════╗")
        print("1. Ver eventos ordenados por total")
        print("2. Agregar nuevo evento")
        print("3. Buscar evento por fecha")
        print("4. Salir")
        print("╚═══════════════════════════════════════╝")
        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            imprimir_eventos(eventos)
        elif opcion == "2":
            agregar_evento(eventos)
        elif opcion == "3":
            fecha = input("Ingresá la fecha a buscar (AAAA-MM-DD): ")
            buscar_eventos_por_fecha(eventos, fecha)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

# Iniciar el programa
menu()
