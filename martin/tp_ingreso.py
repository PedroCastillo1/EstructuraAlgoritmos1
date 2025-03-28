def input_int(prompt):
    """
    Solicita al usuario un número entero y continúa solicitándolo hasta que la entrada sea válida.
    (No utiliza while True, sino un ciclo controlado con una condición).
    """
    valid = False
    result = None
    while not valid:
        user_input = input(prompt)
        try:
            result = int(user_input)
            valid = True
        except ValueError:
            print("Error: por favor ingrese un número válido.")
    return result


def input_nonnegative_int(prompt):
    """
    Solicita al usuario un número entero no negativo.
    Si se ingresa un número negativo, se vuelve a pedir la entrada.
    """
    result = input_int(prompt)
    while result < 0:
        print("Por favor ingrese un número entero no negativo.")
        result = input_int(prompt)
    return result


def eventos(lista_de_eventos):
    """Permite seleccionar un evento de la lista ingresada."""
    if not lista_de_eventos:
        print("No hay eventos disponibles. Primero ingrese eventos.")
        return None

    seleccion = input_int("Presione un número para iniciar el programa de ingreso de evento o -1 para salir: ")
    # Valida que, si se ingresa un número negativo, solo se permita -1
    while seleccion < -1:
        print("Por favor ingrese un número positivo o -1 para salir.")
        seleccion = input_int("Presione un número para iniciar el programa de ingreso de evento o -1 para salir: ")

    if seleccion != -1:
        print(f"Los eventos son: {lista_de_eventos}")
        indice_evento = input_nonnegative_int("Elija el evento (la lista arranca en 0): ")
        while indice_evento < 0 or indice_evento >= len(lista_de_eventos):
            print("Error: número de evento desconocido.")
            print(f"Los eventos son: {lista_de_eventos}")
            indice_evento = input_nonnegative_int("Elija el evento (la lista arranca en 0): ")
        return lista_de_eventos[indice_evento]
    else:
        print("Se cerró el programa de selección de eventos.")
        return None


def ingresar_eventos(lista_esperada):
    """
    Permite al usuario ingresar eventos y los agrega a la lista recibida.
    Se valida que la opción ingresada sea -1 o un número positivo.
    """
    a = input_int("Si desea agregar un evento presione un número, sino presione -1: ")
    while a < -1:
        print("Por favor ingrese un número positivo o -1 para salir.")
        a = input_int("Si desea agregar un evento presione un número, sino presione -1: ")
    print("Los eventos actuales son:", lista_esperada)
    while a != -1:
        evento = input("Ingrese un evento: ")
        lista_esperada.append(evento)
        a = input_int("Si desea agregar otro evento presione un número, sino presione -1: ")
        while a < -1:
            print("Por favor ingrese un número positivo o -1 para salir.")
            a = input_int("Si desea agregar otro evento presione un número, sino presione -1: ")
    return lista_esperada


def ingresar_salones(lista_vacia_salones):
    """
    Permite al usuario ingresar salones y los agrega a la lista recibida.
    Se valida que la opción ingresada sea -1 o un número positivo.
    """
    a = input_int("Si desea agregar un nuevo salón presione un número, sino presione -1: ")
    while a < -1:
        print("Por favor ingrese un número positivo o -1 para salir.")
        a = input_int("Si desea agregar un nuevo salón presione un número, sino presione -1: ")
    print("Los salones actuales son:", lista_vacia_salones)
    while a != -1:
        salon = input("Ingrese un salón: ")
        lista_vacia_salones.append(salon)
        a = input_int("Si desea agregar otro salón presione un número, sino presione -1: ")
        while a < -1:
            print("Por favor ingrese un número positivo o -1 para salir.")
            a = input_int("Si desea agregar otro salón presione un número, sino presione -1: ")
    return lista_vacia_salones


def calcular_comida(invitados):
    """Calcula las cantidades de comida en función del número de invitados."""
    gramos_snacks = 250
    plato_principal = invitados      # 1 plato por invitado
    entradas = invitados * 2         # 2 entradas por invitado
    postre = invitados               # 1 postre por invitado
    bocadillos_kg = (invitados * gramos_snacks) / 1000  # Conversión a kg
    return {
        "plato_principal": plato_principal,
        "entradas": entradas,
        "postre": postre,
        "bocadillos_kg": bocadillos_kg
    }


def calcular_personal(num_invitados):
    """Calcula la cantidad de personal necesaria (aproximadamente 1 por cada 10 invitados)."""
    return num_invitados / 10 if num_invitados else 0


def calcular_mesas(num_invitados):
    """Calcula la cantidad de mesas necesarias (aproximadamente 1 por cada 5 invitados)."""
    return num_invitados / 5 if num_invitados else 0


def seleccionar_salon(lista_de_salones):
    """Permite seleccionar un salón de la lista ingresada."""
    if not lista_de_salones:
        print("No hay salones disponibles. Primero ingrese salones.")
        return None

    seleccion = input_int("Presione un número para iniciar el programa de selección de salón o -1 para salir: ")
    while seleccion < -1:
        print("Por favor ingrese un número positivo o -1 para salir.")
        seleccion = input_int("Presione un número para iniciar el programa de selección de salón o -1 para salir: ")

    if seleccion != -1:
        print(f"Los salones son: {lista_de_salones}")
        indice_salon = input_nonnegative_int("Elija el salón (la lista arranca en 0): ")
        while indice_salon < 0 or indice_salon >= len(lista_de_salones):
            print("Error: número de salón desconocido.")
            print(f"Los salones son: {lista_de_salones}")
            indice_salon = input_nonnegative_int("Elija el salón (la lista arranca en 0): ")
        return lista_de_salones[indice_salon]
    else:
        print("Se cerró el programa de selección de salón.")
        return None


def cotizar_evento(num_invitados, comida, personal_necesario, mesas_necesarias):
    """
    Calcula el costo total del evento basándose en:
      - Alimentos: plato principal, entradas, postre y bocadillos
      - Personal: costo por cada miembro
      - Mesas: costo por mesa
      - Renta del salón: costo fijo

    Devuelve la cotización en forma de matriz (lista de listas), donde cada fila es [concepto, costo].
    """
    # Supuestos de costos (ajustables según requerimientos)
    costo_plato_principal = 20         # costo por plato principal
    costo_entrada_unitario = 5         # costo por cada entrada
    costo_postre = 8                   # costo por postre
    costo_bocadillos_kg = 30           # costo por kg de bocadillos
    costo_personal_unit = 50           # costo por cada miembro de personal
    costo_mesa_unit = 20               # costo por mesa
    costo_salon_renta = 200            # costo fijo de renta del salón

    costo_alimentos = (
        comida["plato_principal"] * costo_plato_principal +
        comida["entradas"] * costo_entrada_unitario +
        comida["postre"] * costo_postre +
        comida["bocadillos_kg"] * costo_bocadillos_kg
    )
    costo_personal = personal_necesario * costo_personal_unit
    costo_mesas = mesas_necesarias * costo_mesa_unit
    total = costo_alimentos + costo_personal + costo_mesas + costo_salon_renta

    matriz_cotizacion = [
        ["Costo de alimentos", costo_alimentos],
        ["Costo de personal", costo_personal],
        ["Costo de mesas", costo_mesas],
        ["Costo de renta del salón", costo_salon_renta],
        ["Total a pagar", total]
    ]
    return matriz_cotizacion


def imprimir_matriz_cotizacion(matriz):
    """
    Imprime la matriz de cotización en formato cuadriculado.
    """
    col1_width = max(len(str(fila[0])) for fila in matriz)
    col2_width = max(len(str(fila[1])) for fila in matriz)
    
    header1, header2 = "Concepto", "Costo"
    col1_width = max(col1_width, len(header1))
    col2_width = max(col2_width, len(header2))
    
    total_width = col1_width + col2_width + 7

    def imprimir_linea():
        print("+" + "-" * (total_width - 2) + "+")

    imprimir_linea()
    print(f"| {header1:<{col1_width}} | {header2:>{col2_width}} |")
    imprimir_linea()
    for fila in matriz:
        print(f"| {fila[0]:<{col1_width}} | {fila[1]:>{col2_width}} |")
    imprimir_linea()


def personalizar_evento(num_invitados, lista_de_eventos, lista_salones):
    """Personaliza el evento: selección de salón y evento, cálculos de necesidades y cotización final."""
    salon_elegido = seleccionar_salon(lista_salones)
    if salon_elegido is None:
        return

    evento_elegido = eventos(lista_de_eventos)
    if evento_elegido is None:
        return

    comida = calcular_comida(num_invitados)
    personal_necesario = calcular_personal(num_invitados)
    mesas_necesarias = calcular_mesas(num_invitados)
    cotizacion = cotizar_evento(num_invitados, comida, personal_necesario, mesas_necesarias)

    print("\n--- Resumen del Evento Personalizado ---")
    print(f"Evento: {evento_elegido}")
    print(f"Salón: {salon_elegido}")
    print(f"Número de invitados: {num_invitados}")
    print("\nCálculo de alimentos:")
    for key, value in comida.items():
        print(f"  {key}: {value}")
    print(f"\nCantidad de personal necesaria: {personal_necesario}")
    print(f"Cantidad de mesas necesarias: {mesas_necesarias}")
    
    print("\n--- Cotización Final ---")
    imprimir_matriz_cotizacion(cotizacion)


def main():
    # Se solicita el número de invitados asegurando que sea no negativo.
    invitados_totales = input_nonnegative_int("Ingrese el número de invitados: ")

    lista_de_salones = ingresar_salones([])
    lista_de_eventos = ingresar_eventos([])

    if not lista_de_salones or not lista_de_eventos:
        print("No se completó el ingreso de salones o eventos. Finalizando el programa.")
        return

    personalizar_evento(invitados_totales, lista_de_eventos, lista_de_salones)


if __name__ == "__main__":
    main()
