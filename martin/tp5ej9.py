def generar_tabla_diccionario(n):
    """
    crea un diccionario  
    """
    return {i: n * i for i in range(1, 13)}



   
n = int(input("ingresa un numero entero : "))
while n < 0 :
    print(" número  no valido.")
    n = int(input("ingresa un numero entero: "))
    

tabla = generar_tabla_diccionario(n)
print(f"\nTabla de multiplicar de {n} (1 a 12):")
for i, producto in tabla.items():

    print(f"{n} x {i:2d} = {producto:3d}")



