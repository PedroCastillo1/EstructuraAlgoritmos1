def esBisiesto(año):
    """
    	Un año es bisiesto si es divisible por 4 y no divisible por 100, a menos que también sea divisible por 400.
    """
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    return False

def diadelasemana(dia, mes, año):
    """
        Función que devuelve el día de la semana usando el algoritmo de Zeller
    """
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

def validarFecha(fecha):
    """
        Función para validar una fecha ingresada
    """
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
    """
        Lista de días por mes. Febrero depende de si es bisiesto.
    """
    dias_en_mes = [31, 29 if esBisiesto(año) else 28, 31, 30, 31, 30,
                   31, 31, 30, 31, 30, 31]
    return dias_en_mes[mes - 1]

def mostrarCalendario(año, eventos):
    """
        Función para mostrar el calendario anual
    """
    # Nombres de los meses en una lista
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    for mes in range(1, 13): # recorre los meses (1 hasta 12)
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

def agregarEventoACalendario(calendario, fecha, eventoAAgregar):
    """
        Verifica si la dicha fecha esta dentro del calendario 
            - si esta pregunta de sobrescribirlo si/no
                -No : No realiza ningin cambio
                -Si: agrega el evento con cada parametro ( Cliente - TipoEvento - Servicios - Precio)
        imprime un mensaje de que se cumplio la carga
    """

    if fecha in calendario: # si la fecha ingresada se encuentra en el calendario
        #Ingresa por teclado la opcion a elegir

        # AGREGAR LA FUNCION .LOWER!!!!!!!!!! (PARA SACAR EL IF DE ABAJO POR TEMAS DE MAYUS/MINUS)
        opcion = input(f"Ya existe un evento en {fecha}. ¿Desea sobrescribirlo? (S/N): ")
        if opcion != "S" and opcion != "s":
            return print(" No se realizó ningún cambio.")

    # Agregamos cada parametro del evento a cada posicion de la lista
    cliente = eventoAAgregar [0]
    tipoEvento = eventoAAgregar [1]
    servicios = eventoAAgregar [2]
    precio = eventoAAgregar [3]

    
    calendario[fecha] = {"cliente": cliente, "tipoDeEvento": tipoEvento, "servicios": servicios, "precio": precio}
    print(f"Evento '{cliente}' agregado el {fecha}.")

def eliminarEvento(calendario, fechaAEliminar):
    """ 
        Elimina eventos
            - Verifica que la fecha pasada por parametro sea valida
            - verifica que dicha fecha este dentro del calendario
                - sino informa y no realiza dicha funcion
            
    
    """
    # Sino se cumple la funcion de validarFecha informa que se ingreso una fecha invalida
    if not validarFecha(fechaAEliminar):
        return print("Fecha invalida")
    # Si la fecha a eliminar esta dentro del calendario, realiza la eliminacion de la fecha 
    if fechaAEliminar in calendario:
        print(f"Eliminando '{calendario[fechaAEliminar]['cliente']}' el {fechaAEliminar}.")

        #No se que realiza esta linea de codigo (ver en grupo)
        del calendario[fechaAEliminar]

    #Si no esta dentro del calendario informa que no existe tal evento
    else:
        print(f"No hay eventos el {fechaAEliminar}.")


def buscarEvento(calendario, fecha):
    """
        Funcion para buscar un evento
            - validamos que la fecha sea ingresada correctamente
            - Validamos que dicha fecha se encuentre dentro del calendario
            
            ????
            - agrega cada parametro del evento encontrado a la lista Evento []
            - sino informa que no hay dicho evento en calendario


            HAY QUE MODIFICAR ESTE CODIGO PORQUE REALIZA MUCHAS COSAS EN VEZ DE UNA SOLA COSA ESPECIFICA <3

    
    """
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

def verificarServiciosElegidos(serviciosElegidos, servicioAAgregar):
    """
        Verifica si es nombre ya esta en la lista de servicios elegidos

    """
    #creo una variable booleana
    resultado = True
    # Si Servicio a agregar se encuentra en servicios elegidos
    if servicioAAgregar in serviciosElegidos:
        # Se actualiza la variable a false --> significa que ya esta como servicio elegido
        resultado = False
    return resultado # Retorna si se encuentra o no se encuentra
########################################Funciones Calendario################################################
def crearEvento(listaEventos,cliente,tipoEvento,servicios,precios):
    """
        Crea un evento
            - genera una lista vacia
            - agrega cada parametro enviado a la lista 
            - Retorna la lista cargada
    """
    evento = [] # Crea una lista vacia
    # Agrega cada parametro a la lista
    evento.append(cliente)
    evento.append(tipoEvento)
    evento.append(servicios)
    evento.append(precios)
    listaEventos.append(evento)
    return evento
####################################################Funciones Impresion######################################
def imprimirEvento(evento):
    """
        Función para imprimir los evento
    """
    # Calcular el total por evento
    cliente = evento[0]
    tipo_evento = evento[1]
    servicios = evento[2]
    precios = evento[3]
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

def imprimirServicios(servicios):
    print("\n+--------------------------+-------------+")
    print("|        SERVICIO         |   PRECIO    |")
    print("+--------------------------+-------------+")
    for i in range(len(servicios)):
        nombre = servicios[i][0]
        precio = servicios[i][1]
        print(f"| {i}: {nombre:<22} | ${precio:<9} |")
    print("+--------------------------+-------------+")

def imprimir_eventos(diccionario):
    total_general = 0
    lista_eventos = []

    # Crear lista auxiliar con totales
    for fecha, datos in diccionario.items():
        total = 0
        for precio in datos["precio"]:
            total += precio
        lista_eventos.append({
            "fecha": fecha,
            "cliente": datos["cliente"],
            "tipoDeEvento": datos["tipoDeEvento"],
            "servicios": datos["servicios"],
            "precio": datos["precio"],
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
        print(f"Tipo de Evento: {e['tipoDeEvento']}")
        print(f"Fecha: {e['fecha']}")
        print("┌────────────────────────────────┬────────────┐")
        print("│          Servicio              │   Precio   │")
        print("├────────────────────────────────┼────────────┤")
        for i in range(len(e["servicios"])):
            print(f"│ {e['servicios'][i]:<30} │ ${e['precio'][i]:<10}│")
        print("└────────────────────────────────┴────────────┘")
        print(f"TOTAL del evento: ${e['total']}")
        total_general += e["total"]

    print("\n════════════════════════════════════════════════════════════════════")
    print(f"TOTAL GENERAL INGRESADO POR TODOS LOS EVENTOS: ${total_general}")
    print("════════════════════════════════════════════════════════════════════")

# Llamada a la función

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
        if opcion == 1:
            interfaz_crear_evento()
            cliente = input("Ingrese su nombre: ")
            tipoEvento = input("Ingrese el tipo de evento: ")
            cantPersonas = int(input("Ingrese la cantidad de personas que vendran al evento: "))
            serviciosElegidos = []
            precios = []
            serviciosElegidos.append(f"CantPersonas({cantPersonas})")
            precios.append(cantPersonas*1000)
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
            evento = crearEvento(listaEventos, cliente, tipoEvento,serviciosElegidos,precios)
            imprimirEvento(evento)
            fecha = input("Ingrese la fecha del evento en este formato YYYY-MM-DD: ")
            while validarFecha(fecha) == False:
                fecha = input("Fecha invalida ingrese una fecha valida en este formato YYYY-MM-DD: ")
            agregarEventoACalendario(calendario, fecha, evento)
            interfaz_bienvenida_gestor_eventos()
            opcion = int(input("Seleccione una opcion: "))
        
        if(opcion == 2):
            interfaz_ver_evento()
            imprimir_eventos(calendario)
            interfaz_bienvenida_gestor_eventos()
            opcion = int(input("Seleccione una opcion: "))
        
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