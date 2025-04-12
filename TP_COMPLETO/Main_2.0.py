def esBisiesto(año):
    # Un año es bisiesto si es divisible por 4 y no divisible por 100,
    # a menos que también sea divisible por 400.
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    return False

# Función que devuelve el día de la semana usando el algoritmo de Zeller
def diadelasemana(dia, mes, año):
    # Para enero y febrero, se consideran como meses 13 y 14 del año anterior
    if mes < 3:
        mes += 10
        año -= 1
    else:
        mes -= 2
    # Se separa el siglo y el año
    siglo = año // 100
    anio2 = año % 100
    # Fórmula de Zeller para obtener el día de la semana (0=domingo, ..., 6=sábado)
    diassem = (((26 * mes - 2) // 10) + dia + anio2 + (anio2 // 4) + (siglo // 4) - (2 * siglo)) % 7
    # Si es negativo, se ajusta sumando 7
    if diassem < 0:
        diassem += 7
    return diassem

# Función para validar una fecha ingresada
def validarFecha(fecha):
    partes = fecha.split("-") #  "2025-04-10" -----> ["2025", "04", "10"]
    if len(partes) != 3: # Si el usuario ingresa mal la fecha (falta un parametro) retorna FALSE
        return False

    #Separamos en partes la fecha ingresada en 3 Variables
    anio_str = partes[0]
    mes_str = partes[1]
    dia_str = partes[2]

    # Validar que todos sean dígitos
    if not (anio_str.isdigit() and mes_str.isdigit() and dia_str.isdigit()):
        return False

    #Convertimos para una de las partes en numeros enteros
    año = int(anio_str)
    mes = int(mes_str)
    dia = int(dia_str)

    #Verificamos el rango del MES
    if mes < 1 or mes > 12:
        return False

    #Verificamos el rango del DIA ----> Llamamos a la funcioin dias_del_mes
    if dia < 1 or dia > diasDelMes(año, mes):
        return False
    return True

def diasDelMes(año, mes):
    # Lista de días por mes. Febrero depende de si es bisiesto.
    dias_en_mes = [31, 29 if esBisiesto(año) else 28, 31, 30, 31, 30,
                   31, 31, 30, 31, 30, 31]
    return dias_en_mes[mes - 1]

# Función para mostrar el calendario anual
def mostrarCalendario(año, eventos):
    # Nombres de los meses
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    for mes in range(1, 13):
        print("\n" + meses[mes - 1] + " " + str(año))
        print("Dom\tLun\tMar\tMie\tJue\tVie\tSab")  # Encabezado de días

        primer_dia_semana = diadelasemana(1, mes, año)
        if primer_dia_semana != 0:
            print("\t" * primer_dia_semana, end="")  # Espacios iniciales

        dias_mes = diasDelMes(año, mes)
        
        for dia in range(1, dias_mes + 1):
            fecha_actual = f"{año:04d}-{mes:02d}-{dia:02d}"
            num_dia_semana = diadelasemana(dia, mes, año)

            # Marca con corchetes si hay evento
            if fecha_actual in eventos:
                print(f"[{dia:2d}]", end="\t")
            else:
                print(f"{dia:2d}", end="\t")

            # Si es sábado, salta de línea (porque domingo es 0)
            if num_dia_semana == 6:
                print()
        print()  # Línea en blanco al final de cada mes


#################################################################################################################################################
def agregarEventoACalendario(calendario, fecha, eventoAAgregar):
    if fecha in calendario:
        opcion = input(f"Ya existe un evento en {fecha}. ¿Desea sobrescribirlo? (S/N): ")
        if opcion != "S" and opcion != "s":
            return print(" No se realizó ningún cambio.")

    cliente = eventoAAgregar["cliente"]
    tipoEvento = eventoAAgregar["tipoEvento"]
    servicios = eventoAAgregar["servicios"]
    precios = eventoAAgregar["precios"]

    calendario[fecha] = {
        "cliente": cliente,
        "tipoEvento": tipoEvento,
        "servicios": servicios,
        "precios": precios
    }
    print(f"Evento '{cliente}' agregado el {fecha}.")

#################################################################################################################################################
def eliminarEvento(calendario, fechaAEliminar):
    if not validarFecha(fechaAEliminar):
        return print("Fecha invalida")

    if fechaAEliminar in calendario:
        print(f"Eliminando '{calendario[fechaAEliminar]['cliente']}' el {fechaAEliminar}.")
        del calendario[fechaAEliminar]
    else:
        print(f"No hay eventos el {fechaAEliminar}.")

# Función para buscar un evento
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
########################################Funciones Calendario################################################
def crearEvento(listaEventos, cliente, tipoEvento, servicios, precios):
    evento = {
        "cliente": cliente,
        "tipoEvento": tipoEvento,
        "servicios": servicios,
        "precios": precios
    }
    listaEventos.append(evento)
    return evento
"""
    ¿Por qué usar un diccionario?
        Claridad: Es más claro acceder a las propiedades del evento usando claves como evento["cliente"] en lugar de tener que recordar qué índice corresponde a cada atributo.

        Flexibilidad: Si en el futuro decides agregar más información al evento (como una fecha, ubicación o presupuesto), puedes hacerlo fácilmente sin cambiar la estructura.

        Escalabilidad: Si trabajas con muchos eventos, un diccionario es mucho más fácil de manejar y leer que una lista con posiciones que dependen del orden
"""
####################################################Funciones Impresion#########################################################################
# Función para imprimir los evento
def imprimirEvento(evento):
    # Calcular el total por evento
    cliente = evento["cliente"]
    tipo_evento = evento["tipoEvento"]
    servicios = evento["servicios"]
    precios = evento["precios"]
    total = 0
    for precio in precios:
        total += precio

    # Imprimir los eventos ordenados
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


    
########################################################## AGREGAR EVENTO #############################################################



def ImprimirEncabezadoEventos():
    print("\n╔════════════════════════════════════════╗")
    print("║         LISTA DE TODOS LOS EVENTOS      ║")
    print("╚════════════════════════════════════════╝")

def ImprimirEvento(nombre_evento, detalles, numero):
    print(f"\nEvento {numero}: {nombre_evento}")
    print(f"  Tipo de Evento: {detalles['Tipo']}")
    print(f"  Fecha: {detalles['Fecha']}")
    print(f"  Cantidad de Invitados: {detalles['Invitados']}")
    print(f"  Servicios Contratados: {', '.join(detalles['Servicios']) if detalles['Servicios'] else 'Ninguno'}")
    print(f"  Presupuesto Total: ${detalles['Presupuesto']}")

def ImprimirMensajeSinEventos():
    print("\n╔════════════════════════════════════════╗")
    print("║      NO HAY EVENTOS REGISTRADOS        ║")
    print("╚════════════════════════════════════════╝\n")

def VerTodosLosEventos(calendario):
    if not calendario:
        ImprimirMensajeSinEventos()
        return  # <- Esto evita que siga ejecutando abajo.
    
    ImprimirEncabezadoEventos()
    numero = 1
    for fecha, detalles in calendario.items():
        print(f"\nEvento {numero}:")
        print(f"  Fecha: {fecha}")
        print(f"  Cliente: {detalles['cliente']}")
        print(f"  Tipo de Evento: {detalles['tipoEvento']}")
        print(f"  Servicios Contratados: {', '.join(detalles['servicios'])}")
        total = sum(detalles['precios'])
        print(f"  Presupuesto Total: ${total}")
        numero += 1
    print("\n══════════════════════════════════════════\n")




#######################################################Interfaces###################################################################################
# Interfaces generales

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

# Interfaces individuales
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

#Programa Principal
def programaPrincipal():
    listaEventos = []
    calendario = {}
    servicios = [["Catering Caro", 200000], ["Catering Barato", 75000], ["Dj", 50000], ["Fotografo", 20000]]
    interfaz_bienvenida_gestor_eventos()
    opcion = int(input("Seleccione una opcion: "))
    while (0 < opcion < 7):
        ############################################################################################
        if opcion == 1:
            interfaz_crear_evento()
            cliente = input("Nombre del cliente: ")
            tipoEvento = input("Tipo de evento (Ej: Casamiento, Cumpleaños): ")
            
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
                        if servicio_elegido not in seleccionados:  # Verificar que no se haya seleccionado previamente
                            seleccionados.append(servicio_elegido)
                            servicios.append(servicio_elegido)
                            precios.append(servicios_disponibles[servicio_elegido])
                            print(f"✅ '{servicio_elegido}' agregado.")
                        else:
                            print("⚠️ Este servicio ya ha sido seleccionado.")
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
                            break  # Aquí se finaliza la selección si hay al menos un servicio.
                    else:
                        print("❌ Opción no válida.")
                else:
                    print("❌ Entrada inválida.")

            # Ahora utilizamos servicios y precios, no serviciosElegidos
            evento = crearEvento(listaEventos, cliente, tipoEvento, servicios, precios)
            imprimirEvento(evento)
            
            fecha = input("Ingrese la fecha del evento en este formato YYYY-MM-DD: ")
            while validarFecha(fecha) == False:
                fecha = input("Fecha invalida ingrese una fecha valida en este formato YYYY-MM-DD: ")
            agregarEventoACalendario(calendario, fecha, evento)
            interfaz_bienvenida_gestor_eventos()
            opcion = int(input("Seleccione una opción: "))

            
            
        ############################################################################################
            
        if(opcion == 2):
            interfaz_ver_evento()
            VerTodosLosEventos(calendario)
        if(opcion == 3):
            interfaz_eliminar_evento()
            fechaAEliminar = input("Ingresa la fecha del evento a eliminar en YYYY-MM-DD: ")
            eliminarEvento(calendario,fechaAEliminar)
            interfaz_bienvenida_gestor_eventos()
            opcion = int(input("Seleccione una opcion: "))
        if(opcion == 4):
            interfaz_mostrar_calendario()
            año = int(input("Ingrese el año a visualizar: "))
            mostrarCalendario(año,calendario)
            interfaz_bienvenida_gestor_eventos()
            opcion = int(input("Seleccione una opcion: "))
        if(opcion == 5):
            interfaz_buscar_evento()
            fechaABuscar = input("Ingresa la fecha del evento a buscar en YYYY-MM-DD: ")
            buscarEvento(calendario, fechaABuscar)
            interfaz_bienvenida_gestor_eventos()
            opcion = int(input("Seleccione una opcion: "))
        if(opcion == 6):
            interfaz_salir_gestor_eventos()
            opcion = -1
            break
    interfaz_salir_programa()          

programaPrincipal()



