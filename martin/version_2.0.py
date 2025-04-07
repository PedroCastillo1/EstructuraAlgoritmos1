def menu ():
    """este menu se encarga de mostrar las diferentes opciones del programa"""


    print("#######################################################################")
    print("Bienvenido al programa de organizacion de eventos desarrollado por UADE")
    print("#######################################################################")

    print("################################################################################################")
    print("Tenemos las siguientes opciones :")
    print("1 - Crear evento")
    print("2 - Ver eventos")
    print("3 - Eliminar evento")
    print("4 - Salir del programa")

    print("################################################################################################")

    opcion = int(input("Que desea hacer ? "))

    while opcion < 1 or opcion > 4: #en caso que el usuario ingrese un numero no valido, vuelve a preguntar
        print("Error opcion no existente ")
        opcion = int(input("Que desea hacer? = "))

    if opcion == 4: #SI OPCION ES IGUAL A 4 RETORNA FALSO 
        return False    

    return opcion # retorna la decision del usuario

def verificar_disponibilidad(fecha_evento, cant_personas, nombre_salon, lista_eventos):
    """verifica si la fecha esta disponible """

    capacidad_max = {"La Plata": 120, "Puerto Madero": 200}
    verificado = 0
    #se ejecuta el while hasta que se cumplan los cambios de fecha #

    while verificado == 0:
        ocupado = 0

        #verifica si la fecha del evento en el salon esta ocupado#
        for i in range(len(lista_eventos)):
            if lista_eventos[i][1] == fecha_evento and lista_eventos[i][4] == nombre_salon:
                ocupado = 1

        if ocupado == 1:
            print(f"El salón {nombre_salon} ya está reservado para la fecha {fecha_evento}.")
            print("¿Qué desea hacer?")
            print("1 - Cambiar la fecha del evento")
            print("2 - Cambiar el salón del evento")
            decision = int(input("Ingrese opción: "))

            while decision != 1 and decision != 2:
                print("Opción inválida.")
                decision = int(input("Ingrese opción: "))

            if decision == 1:
                fecha_evento = input("Ingrese la nueva fecha (ej: 1/1/2025): ")
            else:
                # Elegimos automáticamente el otro salón
                if nombre_salon == "La Plata":
                    nombre_salon = "Puerto Madero"
                else:
                    nombre_salon = "La Plata"

                print(f"Ahora se intentará reservar en el salón {nombre_salon}.")

                #verifica la capacidad maxima del salon elegido#
                capacidad = capacidad_max[nombre_salon]

                #si se supera #
                if cant_personas > capacidad:
                    print(f"❌ El salón {nombre_salon} no soporta esa cantidad. Máximo {capacidad}.")
                    print("¿Qué desea hacer?")
                    print("1 - Cambiar cantidad de personas")
                    
                    subdecision = int(input("Ingrese opción: "))
                    while subdecision != 1:
                        print("Opción inválida.")
                        subdecision = int(input("Ingrese opción: "))

                    if subdecision == 1:
                        cant_personas = int(input("Ingrese nueva cantidad de personas: "))
                   
        else:
            verificado = 1  # Todo válido

    return fecha_evento, nombre_salon, cant_personas

    
def crear_evento(lista_eventos):
    """se encarga de pedir todos los datos y crear el evento """
    lista_evento = []

    print("####################################")
    print("Bienvenido a la creacion de eventos")
    print("####################################")

    #############################################################################################
    nombre_evento = input("ingresa el nombre del evento ") #pide el nombre del evento

    seguro = int(input("esta seguro que desea poner ese nombre : 1- SI 2- NO ")) #verifica la decision del usuario

    while seguro < 1 or seguro > 2:
        print("Error opcion no existente ")
        seguro = int(input("esta seguro que desea poner ese nombre : 1- SI 2- NO ")) #comprueba que se cumplan los parametros de si y no

    if seguro == 1:
        print("nombre de evento agregado con exito ")   #si la decision fue correcta se agrega el nombre del evento
        lista_evento.append(nombre_evento)
    else : 
        print("Que nombre desea poner ")
        nombre_evento = input("ingresa el nombre del evento ")   # en caso que no fue la decision correcta pide de nuevo el nombre del evento
        lista_evento.append(nombre_evento)

    ##############################################################################################
    fecha_evento = input("ingrese una fecha como en el ejemplo: 1/1/2025 ") # pide la fecha del evento

    seguro_2 = int(input("esta seguro que desea poner esa fecha : 1- SI 2- NO "))

    while seguro_2 < 1 or seguro_2 > 2:
        print("Error opcion no existente ")
        seguro = int(input("esta seguro que desea poner esa fecha : 1- SI 2- NO ")) #comprueba que se cumplan los parametros de si y no

    if seguro_2 == 1:
        print("fecha de evento agregado con exito ")   #si la decision fue correcta se agrega la fecha  del evento
        lista_evento.append(fecha_evento) # agrega la fecha a la lista
    else : 
        print("Que fecha desea poner ")
        fecha_evento = input("ingrese una fecha como en el ejemplo: 1/1/2025 ") #si la fecha fue equivocada pide de nuevo la fecha
        lista_evento.append(fecha_evento)

    ##################################################################################################


    tipo_evento = input("ingrese el tipo de evento que quiere ") # pide el tipo de evento

    seguro_3 = int(input("esta seguro que desea poner ese evento : 1- SI 2- NO "))

    while seguro_3 < 1 or seguro_3 > 2:
        print("Error opcion no existente ")
        seguro = int(input("esta seguro que desea poner ese evento : 1- SI 2- NO ")) #comprueba que se cumplan los parametros de si y no

    if seguro_3 == 1:
        print(" El evento fue agregado con exito ")   #si la decision fue correcta se agrega el tipo  de evento
        lista_evento.append(tipo_evento) # agrega el evento a la lista
    else : 
        print("Que evento desea poner ")
        tipo_evento = input("ingrese el tipo de evento que quiere ") # pide el tipo de evento
        lista_evento.append(tipo_evento)

    #####################################################################################################

    cant_personas = int(input("ingrese la cantidad de personas para el evento")) # pide el tipo de evento

    seguro_4 = int(input("esta seguro que desea ingresar ese numero de personas : 1- SI 2- NO "))

    while seguro_4 < 1 or seguro_4 > 2:
        print("Error opcion no existente ")
        seguro = int(input("esta seguro que desea ingresar ese numero de personas : 1- SI 2- NO ")) #comprueba que se cumplan los parametros de si y no

    if seguro_4 == 1:
        print(" la cantidad de personas fueron agregadas con exito ")   #si la decision fue correcta se agrega el tipo  de evento
        lista_evento.append(cant_personas) # agrega el evento a la lista
    else : 
        print("diga la cantidad de personas ")
        cant_personas = int(input("ingrese la cantidad de personas para el evento, maximo 200 personas "))
        lista_evento.append(cant_personas)

    #######################################################################################################

    # Repetimos hasta que elija un salón válido según la cantidad de personas
    # Repetimos hasta que elija un salón válido según la cantidad de personas y lo confirme
    confirmado = 0

    while confirmado == 0:
        salon_elegido = int(input("Ingrese el salón deseado: 1- La Plata, 2- Puerto Madero "))
        while salon_elegido < 1 or salon_elegido > 2:
            print("Error opción no existente.")
            salon_elegido = int(input("Ingrese el salón deseado: 1- La Plata, 2- Puerto Madero "))

        if salon_elegido == 1:
            nombre_salon = "La Plata"
            capacidad_maxima = 120
        else:
            nombre_salon = "Puerto Madero"
            capacidad_maxima = 200

        print(f"Capacidad máxima del salón {nombre_salon}: {capacidad_maxima} personas")

        # Si se supera la capacidad
        if cant_personas > capacidad_maxima:
            print(f"Error: se supera la capacidad del salón por {cant_personas - capacidad_maxima} personas.")
            print("¿Qué desea hacer?")
            print("1 - Cambiar cantidad de personas")
            print("2 - Elegir otro salón")

            decision = int(input("Ingrese opción: "))
            while decision < 1 or decision > 2:
                print("Opción no válida.")
                decision = int(input("Ingrese opción: "))

            if decision == 1:
                cant_personas = int(input("Ingrese nueva cantidad de personas: "))
                lista_evento[3] = cant_personas  # actualizamos en la lista
                # sigue dentro del mismo bucle, repite validación del mismo salón
            else:
                # volverá al inicio del while sin hacer nada, reelige salón
                pass
        else:
            if cant_personas == capacidad_maxima:
                print("El evento llega justo al límite del salón.")
            else:
                print(f"Todo bien. Quedan {capacidad_maxima - cant_personas} lugares.")

            seguro_5 = int(input(f"¿Está seguro que desea elegir el salón {nombre_salon}? 1- SI 2- NO "))
            while seguro_5 < 1 or seguro_5 > 2:
                print("Error opción no válida.")
                seguro_5 = int(input("¿Está seguro que desea elegir ese salón? 1- SI 2- NO "))

            if seguro_5 == 1:
                confirmado = 1  # rompe el while
            # si elige 2, no hace nada, vuelve a empezar

    ########################################################################################################

    # Verificamos disponibilidad del salón en la fecha
    fecha_evento, nombre_salon, cant_personas = verificar_disponibilidad(fecha_evento, cant_personas, nombre_salon, lista_eventos)

    # Actualizamos en la lista
    lista_evento[1] = fecha_evento
    lista_evento[3] = cant_personas
    lista_evento.append(nombre_salon)

    presupuesto = None    
    lista_evento.append(presupuesto)    #agrega el presupuesto a la lista


    return lista_evento
    ###########################################################################################################

def mostrar_evento(lista_eventos):
    
    if len(lista_eventos) == 0:
        print("No hay eventos cargados.") #si la lista esta vacia se le avisa al usuario
    else:
        datos = ["Nombre del evento", "Fecha del evento", "Tipo de evento", "Cantidad de invitados", "Salón elegido", "Presupuesto" ]

        for titulo in datos: #imprime el encabezado de la matriz
            print(titulo, end="\t")
        print()  # Salto de línea

    
        for evento in lista_eventos: #rellena cada fila y si un dato esta vacio lo pone como sin calcular
             for dato in evento:
                if dato == None:
                    print("Sin calcular", end="\t")
                else:
                    print(dato, end="\t")
             print()  # Salto de línea entre eventos


def eliminar_evento(lista_eventos):
    if len(lista_eventos) == 0:
        print("No hay eventos cargados para eliminar.")
        return

    print("Estos son los eventos disponibles:\n")

    # Mostrar eventos numerados
    for i in range(len(lista_eventos)):
        print(f"{i + 1}. {lista_eventos[i][0]} - {lista_eventos[i][1]} - {lista_eventos[i][4]}")

    # Pedir número de evento a eliminar
    opcion = int(input("Ingrese el número del evento que desea eliminar: "))

    while opcion < 1 or opcion > len(lista_eventos):
        print("Número inválido. Intente de nuevo.")
        opcion = int(input("Ingrese el número del evento que desea eliminar: "))

    # Confirmación
    seguro = int(input(f"¿Está seguro que desea eliminar el evento '{lista_eventos[opcion - 1][0]}'? 1-SI / 2-NO: "))
    while seguro < 1 or seguro > 2:
        print("Opción no válida.")
        seguro = int(input("¿Está seguro que desea eliminar el evento? 1-SI / 2-NO: "))

    if seguro == 1:
        eliminado = lista_eventos.pop(opcion - 1)
        print(f"El evento '{eliminado[0]}' fue eliminado con éxito.")
    else:
        print("El evento no fue eliminado.")

    #programa principal#

eventos = []

seguir = 1

while seguir == 1:
    opcion = menu()

    if opcion == False:
        print("Gracias por usar el sistema.")
        seguir = 0

    elif opcion == 1:
        evento = crear_evento(eventos)
        eventos.append(evento)

    elif opcion == 2:
        mostrar_evento(eventos)

    elif opcion == 3:
        eliminar_evento(eventos)
