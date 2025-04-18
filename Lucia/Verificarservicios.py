#####################################################################################################################################################################################
#####################################################################################################################################################################################
#####################################################################################################################################################################################
def esBisiesto(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    return False

def diadelasemana(dia, mes, año):
    if mes < 3:
        mes += 10
        año -= 1
    else:
        mes -= 2
    siglo = año // 100
    anio2 = año % 100
    diassem = (((26 * mes - 2) // 10) + dia + anio2 + (anio2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    if diassem < 0:
        diassem += 7
    return diassem

def validarFecha(fecha):
    partes = fecha.split("-")
    if len(partes) != 3:
        return False
    anio_str = partes[0]
    mes_str = partes[1]
    dia_str = partes[2]
    if not (anio_str.isdigit() and mes_str.isdigit() and dia_str.isdigit()):
        return False
    año = int(anio_str)
    mes = int(mes_str)
    dia = int(dia_str)
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > diasDelMes(año, mes):
        return False
    return True

def diasDelMes(año, mes):
    dias_en_mes = [31, 29 if esBisiesto(año) else 28, 31, 30, 31, 30,
                   31, 31, 30, 31, 30, 31]
    return dias_en_mes[mes - 1]

def mostrarCalendario(año, eventos):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    for mes in range(1, 13):
        print("\n" + meses[mes - 1] + " " + str(año))
        print("Dom\tLun\tMar\tMie\tJue\tVie\tSab")

        primer_dia_semana = diadelasemana(1, mes, año)
        if primer_dia_semana != 0:
            print("\t" * primer_dia_semana, end="")

        dias_mes = diasDelMes(año, mes)

        for dia in range(1, dias_mes + 1):
            fecha_actual = f"{año:04d}-{mes:02d}-{dia:02d}"
            num_dia_semana = diadelasemana(dia, mes, año)

            if fecha_actual in eventos:
                print(f"[{dia:2d}]", end="\t")
            else:
                print(f"{dia:2d}", end="\t")

            if num_dia_semana == 6:
                print()
        print()

def agregarEventoACalendario(calendario, fecha, eventoAAgregar):
    if fecha in calendario:
        opcion = input(f"Ya existe un evento en {fecha}. ¿Desea sobrescribirlo? (S/N): ")
        if opcion != "S" and opcion != "s":
            return print(" No se realizó ningún cambio.")

    cliente = eventoAAgregar [0]
    tipoEvento = eventoAAgregar [1]
    servicios = eventoAAgregar [2]
    precio = eventoAAgregar [3]

    calendario[fecha] = {"cliente": cliente, "tipoDeEvento": tipoEvento, "servicios": servicios, "precio": precio}
    print(f"Evento '{cliente}' agregado el {fecha}.")

def eliminarEvento(calendario, fechaAEliminar):
    if not validarFecha(fechaAEliminar):
        return print("Fecha invalida")

    if fechaAEliminar in calendario:
        print(f"Eliminando '{calendario[fechaAEliminar]['cliente']}' el {fechaAEliminar}.")
        del calendario[fechaAEliminar]
    else:
        print(f"No hay eventos el {fechaAEliminar}.")

def buscarEvento(calendario, fecha):
    if not validarFecha(fecha):
        return print("Fecha invalida")

    if fecha in calendario:
        eventoEncontrado = calendario[fecha]
        evento = []
        evento.append(eventoEncontrado['cliente'])
        evento.append(eventoEncontrado['tipoDeEvento'])
        evento.append(eventoEncontrado['servicios'])
        evento.append(eventoEncontrado['precio'])
        return imprimirEvento(evento)
    else:
        print(f"No hay eventos el {fecha}.")

def crearEvento(listaEventos,cliente,tipoEvento,servicios,precios):
    evento = []
    evento.append(cliente)
    evento.append(tipoEvento)
    evento.append(servicios)
    evento.append(precios)
    listaEventos.append(evento)
    return evento

def imprimirEvento(matriz):
    cliente = matriz[0]
    tipo_evento = matriz[1]
    servicios = matriz[2]
    precios = matriz[3]
    total = 0
    for precio in precios:
          total += precio

    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║                    DETALLE DE EVENTO EN SALÓN                      ║")
    print("╚════════════════════════════════════════════════════════════════════╝")

    print(f"\nCliente: {cliente}")
    print(f"Tipo de Evento: {tipo_evento}")
    print("┌────────────────────────────────┬────────────┐")
    print("│          Servicio              │   Precio   │")
    print("├────────────────────────────────┼────────────┤")

    for i in range(len(servicios)):
        print(f"│ {servicios[i]:<30} │ ${precios[i]:<10}│")

    print("└────────────────────────────────┴────────────┘")
    print(f"TOTAL del evento: ${total}")

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

# Función que verifica si un servicio ya fue elegido
def verificarServiciosElegidos(serviciosElegidos, servicioAAgregar):
    # Verifica si ese nombre ya está en la lista de servicios elegidos
    resultado = True
    if servicioAAgregar in serviciosElegidos:
        resultado = False
    return resultado

def imprimirServicios(servicios):
    print("\n+--------------------------+-------------+")
    print("|        SERVICIO         |   PRECIO    |")
    print("+--------------------------+-------------+")
    for i in range(len(servicios)):
        nombre = servicios[i][0]
        precio = servicios[i][1]
        print(f"| {i}: {nombre:<22} | ${precio:<9} |")
    print("+--------------------------+-------------+")

def programaPrincipal():
    listaEventos = []
    calendario = {}
    servicios = [["Catering Caro", 200000], ["Catering Barato", 75000], ["Dj", 50000], ["Fotografo", 20000]]
    interfaz_bienvenida_gestor_eventos()
    opcion = int(input("Seleccione una opcion: "))
    while (0 < opcion < 7):
        if opcion == 1:
            interfaz_crear_evento()
            cliente = input("Ingrese su nombre: ")
            tipoEvento = input("Ingrese el tipo de evento: ")
            serviciosElegidos = []
            precios = []
            imprimirServicios(servicios)  
            opcionServ = int(input("Elija por favor un servicio a agregar, si no quiere agregar servicios presiona -1: "))
            while opcionServ != -1:
                if (0 <= opcionServ < len(servicios)):
                    if verificarServiciosElegidos(serviciosElegidos, servicios[opcionServ][0]) == True:
                        serviciosElegidos.append(servicios[opcionServ][0])
                        precios.append(servicios[opcionServ][1])
                    else:
                        print("Este servicio ya esta seleccionado!")
                    opcionServ = int(input("Elija por favor un servicio a agregar, si no quiere agregar servicios presiona -1: "))
                else:
                    opcionServ = int(input("Numero no valido por favor elija otro, si no quiere agregar servicios presiona -1: "))
            evento = crearEvento(listaEventos, cliente, tipoEvento, serviciosElegidos, precios)
            imprimirEvento(evento)
            fecha = input("Ingrese la fecha del evento en este formato YYYY-MM-DD: ")
            while validarFecha(fecha) == False:
                fecha = input("Fecha invalida ingrese una fecha valida en este formato YYYY-MM-DD: ")
            agregarEventoACalendario(calendario, fecha, evento)
            interfaz_bienvenida_gestor_eventos()
            opcion = int(input("Seleccione una opcion: "))
        if opcion == 2:
            interfaz_ver_evento()
            break
        if opcion == 3:
            interfaz_eliminar_evento()
            fechaAEliminar = input("Ingresa la fecha del evento a eliminar en YYYY-MM-DD: ")
            eliminarEvento(calendario, fechaAEliminar)
            interfaz_bienvenida_gestor_eventos()
            opcion = int(input("Seleccione una opcion: "))
        if opcion == 4:
            interfaz_mostrar_calendario()
            año = int(input("Ingrese el año a visualizar: "))
            mostrarCalendario(año, calendario)
            interfaz_bienvenida_gestor_eventos()
            opcion = int(input("Seleccione una opcion: "))
        if opcion == 5:
            interfaz_buscar_evento()
            fechaABuscar = input("Ingresa la fecha del evento a buscar en YYYY-MM-DD: ")
            buscarEvento(calendario, fechaABuscar)
            interfaz_bienvenida_gestor_eventos()
            opcion = int(input("Seleccione una opcion: "))
        if opcion == 6:
            interfaz_salir_gestor_eventos()
            opcion = -1
            break
    interfaz_salir_programa()

programaPrincipal()
