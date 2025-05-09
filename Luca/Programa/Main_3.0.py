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

# Validación y calendario

def esBisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

def diadelasemana(dia, mes, año):
    if mes < 3:
        mes += 10
        año -= 1
    else:
        mes -= 2
    siglo = año // 100
    anio2 = año % 100
    diassem = (((26 * mes - 2) // 10) + dia + anio2 + (anio2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    return diassem if diassem >= 0 else diassem + 7

def validarFecha(fecha):
    partes = fecha.split("-")
    if len(partes) != 3:
        return False
    anio_str, mes_str, dia_str = partes
    if not (anio_str.isdigit() and mes_str.isdigit() and dia_str.isdigit()):
        return False
    año, mes, dia = int(anio_str), int(mes_str), int(dia_str)
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > diasDelMes(año, mes):
        return False
    return True

def diasDelMes(año, mes):
    dias_en_mes = [31, 29 if esBisiesto(año) else 28, 31, 30, 31, 30,
                   31, 31, 30, 31, 30, 31]
    return dias_en_mes[mes - 1]

def mostrarCalendario(año, calendario):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    fechas_eventos = {fecha for fecha, _, _ in calendario}

    for mes in range(1, 13):
        print(f"\n{meses[mes-1]} {año}")
        print("Dom\tLun\tMar\tMie\tJue\tVie\tSab")
        inicio = diadelasemana(1, mes, año)
        if inicio:
            print("\t" * inicio, end="")
        dias_mes = diasDelMes(año, mes)
        for d in range(1, dias_mes + 1):
            fecha = f"{año:04d}-{mes:02d}-{d:02d}"
            marcado = f"[{d:2d}]" if fecha in fechas_eventos else f"{d:2d}"
            dia_sem = diadelasemana(d, mes, año)
            print(f"{marcado}\t", end="")
            if dia_sem == 6:
                print()
        print()

# Gestión de eventos

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

def crearEvento(cliente, tipoEvento, cant_personas, servicios, precios):
    return {
        "cliente": cliente,
        "tipo": tipoEvento,
        "cant_personas": cant_personas,
        "servicios": servicios,
        "precios": precios
    }

def agregarEventoACalendario(calendario, fecha, salon, turno, evento):
    clave = (fecha, salon, turno)
    if clave in calendario:
        opt = input(f"Ya existe un evento en {fecha}, Salón {salon}, Turno {turno}. ¿Sobrescribir? (S/N): ")
        if opt.lower() != 's':
            print("No se realizó ningún cambio.")
            return
        print(f"Evento anterior en {clave} eliminado.")
    calendario[clave] = evento
    print(f"Evento '{evento['cliente']}' agregado el {fecha} en Salón {salon}, Turno {turno}.")

def eliminarEvento(calendario, fecha, salon, turno):
    clave = (fecha, salon, turno)
    if not validarFecha(fecha):
        print("Fecha inválida.")
        return
    if clave in calendario:
        cliente = calendario[clave]["cliente"]
        del calendario[clave]
        print(f"Eliminando evento de '{cliente}' el {fecha} en Salón {salon}, Turno {turno}.")
    else:
        print(f"No hay eventos el {fecha} en Salón {salon}, Turno {turno}.")

def buscarEvento(calendario, fecha, salon, turno):
    clave = (fecha, salon, turno)
    if not validarFecha(fecha):
        print("Fecha inválida.")
        return
    if clave in calendario:
        imprimirEvento(clave, calendario[clave])
    else:
        print(f"No hay eventos el {fecha} en Salón {salon}, Turno {turno}.")

def imprimirEvento(clave, evento):
    fecha, salon, turno = clave
    cliente = evento["cliente"]
    tipo = evento["tipo"]
    cant = evento["cant_personas"]
    servicios = evento["servicios"]
    precios = evento["precios"]
    total = sum(precios)
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
    print(f"TOTAL del evento: ${total}")

def imprimir_eventos(calendario):
    total_general = 0
    eventos_ordenados = sorted(
        calendario.items(),
        key=lambda item: sum(item[1]["precios"]),
        reverse=True
    )
    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║                  DETALLE DE EVENTOS CON FECHAS                     ║")
    print("╚════════════════════════════════════════════════════════════════════╝")
    for clave, evento in eventos_ordenados:
        imprimirEvento(clave, evento)
        total_general += sum(evento["precios"])
    print("\n════════════════════════════════════════════════════════════════════")
    print(f"TOTAL GENERAL INGRESADO POR TODOS LOS EVENTOS: ${total_general}")
    print("════════════════════════════════════════════════════════════════════")

# Flujo principal

def opcionCrearEvento(calendario, servicios_disponibles):
    interfaz_crear_evento()
    cliente = input("Ingrese su nombre: ").strip().title()
    tipo = input("Ingrese el tipo de evento: ").strip().capitalize()
    while True:
        val = input("Ingrese la cantidad de personas: ").strip()
        if val.isdigit() and int(val) > 0:
            cant = int(val)
            break
        print("⚠️ Ingrese un número entero positivo.")
    fecha = input("Ingrese la fecha del evento (YYYY-MM-DD): ").strip()
    while not validarFecha(fecha):
        fecha = input("Fecha inválida. Intente nuevamente (YYYY-MM-DD): ").strip()
    salon = input("Ingrese el nombre del salón: ").strip().capitalize()
    turno = input("Ingrese el turno (Mañana/Tarde/Noche): ").strip().capitalize()
    servicios, precios = [f"CantPersonas({cant})"], [cant * 1000]
    sel, pre = seleccionarServicios(servicios_disponibles)
    servicios.extend(sel)
    precios.extend(pre)
    evento = crearEvento(cliente, tipo, cant, servicios, precios)
    agregarEventoACalendario(calendario, fecha, salon, turno, evento)
    imprimirEvento((fecha, salon, turno), evento)

def gestorEventos():
    calendario = {}
    servicios_disponibles = {
        "Catering Caro": 200000,
        "Catering Barato": 75000,
        "DJ": 50000,
        "Fotógrafo": 20000
    }
    while True:
        interfaz_bienvenida_gestor_eventos()
        opt = input("Seleccione una opción (1-6): ").strip()
        if opt == "1":
            opcionCrearEvento(calendario, servicios_disponibles)
        elif opt == "2":
            interfaz_ver_evento()
            if calendario:
                imprimir_eventos(calendario)
            else:
                print("📭 No hay eventos registrados.")
        elif opt == "3":
            interfaz_eliminar_evento()
            f = input("Ingrese la fecha (YYYY-MM-DD): ").strip()
            s = input("Ingrese el salón: ").strip().capitalize()
            t = input("Ingrese el turno (Mañana/Tarde/Noche): ").strip().capitalize()
            eliminarEvento(calendario, f, s, t)
        elif opt == "4":
            interfaz_mostrar_calendario()
            while True:
                año_str = input("Ingrese el año a visualizar: ").strip()
                if año_str.isdigit() and 1000 <= int(año_str) <= 9999:
                    año = int(año_str)
                    break
                print("⚠️ Ingrese un año válido (ej: 2025).")
            mostrarCalendario(año, calendario)
        elif opt == "5":
            interfaz_buscar_evento()
            f = input("Ingrese la fecha (YYYY-MM-DD): ").strip()
            s = input("Ingrese el salón: ").strip().capitalize()
            t = input("Ingrese el turno (Mañana/Tarde/Noche): ").strip().capitalize()
            buscarEvento(calendario, f, s, t)
        elif opt == "6":
            interfaz_salir_gestor_eventos()
            interfaz_salir_programa()
            break
        else:
            print("❌ Opción inválida. Intente con un número del 1 al 6.")

# Punto de entrada
if __name__ == "__main__":
    gestorEventos()
