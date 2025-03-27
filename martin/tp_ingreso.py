def eventos(lis_de_eventos):
    """ingresando una lista de eventos, permite seleccionar de la lista el evento a realizar"""
    seleccion = int(input("presione un numero para inicir el programa de ingreso de evento o -1 para salir "))
    if seleccion != -1:
        print(f"los eventos son: {lis_de_eventos} ")
        el_evento = int(input(f"eliga el evento, la lista arranca en 0 "))
        while el_evento < 0 or el_evento >= len(lis_de_eventos):
            print("error numero de fiesta desconocido")
            print(f"los eventos son: {lis_de_eventos} ")
            el_evento = int(input(f"eliga el evento, la lista arranca en 0  "))
        decision = lis_de_eventos[el_evento]
        return decision   
    else:
        print("se cerro el programa")      
        
def ingresar_eventos (lista_esperada):
    """se le entrega como parametro una lista vacia y permite ingresar al usuario los eventos que quiera"""
    a = int(input("si desea agregar un evento presione un numero sino presione -1 "))
    print("los eventos actuales son [] ")
    while a != -1:
        lista_esperada.append(input("ingrese un evento "))
        a = int(input("si desea agregar un evento presione un numero sino presione -1 "))
    return lista_esperada

lista_vacia = []
lisa_de_eventos = ingresar_eventos(lista_vacia)
elegir_fiesta = eventos(lista_vacia) 

print(elegir_fiesta)

    
    
    