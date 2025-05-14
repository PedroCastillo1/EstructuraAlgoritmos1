def encajan(ficha1, ficha2):
    """Devuelve True si ficha1 y ficha2 comparten al menos un valor, False si no comparten ninguno"""
      
    cumple = False
    if (set(ficha1) & set(ficha2)) :
        cumple = True
    return cumple




ficha1 = (3, 4)
ficha2 = (5, 4)
print(f"{ficha1} y {ficha2} = {encajan(ficha1, ficha2)}")


