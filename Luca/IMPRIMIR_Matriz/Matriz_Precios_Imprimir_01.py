# Matriz de compras por comprador
compras = [
    ["Juan", ["Pan", "Leche", "Huevos"], [100, 200, 150]],
    ["María", ["Arroz", "Aceite"], [300, 450]],
    ["Luis", ["Fideos", "Tomate", "Queso", "Jugo"], [120, 180, 500, 220]]
]

# Función para imprimir las compras ordenadas por total de mayor a menor
def imprimir_compras(matriz):
    total_general = 0
    compras_con_totales = []

    # Calcular el total de cada comprador y agregarlo a una nueva lista
    for fila in matriz:
        nombre = fila[0]
        precios = fila[2]
        total = 0
        for precio in precios:
            total += precio
        compras_con_totales.append([nombre, fila[1], precios, total])

    # Ordenar la nueva lista por total gastado (índice 3) de mayor a menor
    for i in range(len(compras_con_totales)):
        for j in range(i + 1, len(compras_con_totales)):
            if compras_con_totales[j][3] > compras_con_totales[i][3]:
                aux = compras_con_totales[i]
                compras_con_totales[i] = compras_con_totales[j]
                compras_con_totales[j] = aux

    # Imprimir los datos ordenados
    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║             DETALLE DE COMPRAS POR CLIENTE (ORDENADO)              ║")
    print("╚════════════════════════════════════════════════════════════════════╝")
    
    for fila in compras_con_totales:
        nombre = fila[0]
        productos = fila[1]
        precios = fila[2]
        total = fila[3]

        print(f"\nComprador: {nombre}")
        print("┌───────────────┬────────────┐")
        print("│   Producto    │   Precio   │")
        print("├───────────────┼────────────┤")

        for i in range(len(productos)):
            print(f"│ {productos[i]:<13} │ ${precios[i]:<10}│")
        
        print("└───────────────┴────────────┘")
        print(f"TOTAL de {nombre}: ${total}")
        total_general += total

    print("\n════════════════════════════════════════════════════════════════════")
    print(f"TOTAL GENERAL GASTADO POR TODOS LOS COMPRADORES: ${total_general}")
    print("════════════════════════════════════════════════════════════════════")

# Llamar a la función
imprimir_compras(compras)

