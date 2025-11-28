"""
Simular el uso de un diccionario cuya clave es el nombre de artículo y el valor será el precio de dicho
artículo, ingresar nombres y precios desde el teclado (input). Posteriormente se efectuará una compra 
requiriendo el producto y la cantidad vendida, para luego mostrar:
• Imprimir el promedio de precios de la lista de artículos. 
• Imprimir el monto total vendido de aquel articulo consultado, previamente solicitando la cantidad 
  vendida. 
"""
articulos = {}
contador = 1    
print("------ REGISTRO DE ARTÍCULOS ------")
# ingresar artículos
while True:
    nombre = input(f"Ingrese el nombre del artículo {contador} (o escriba 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    try:
        precio = float(input(f"Ingrese el precio de '{nombre}': S/ "))
        articulos[nombre] = precio  
        contador += 1
    except ValueError:
        print("Precio inválido. Por favor, ingrese un número válido.")
#proceso
if len(articulos) == 0:
    print("\nNo se ingresaron artículos. Programa finalizado.")
else:
    promedio = sum(articulos.values()) / len(articulos)
    print("\n-------------------------------------------")
    print(f"Promedio de precios de los artículos: S/{promedio:.2f}")
    print("-------------------------------------------")
    # --- SIMULACIÓN DE COMPRAS ---
    print("\n--- SIMULACIÓN DE COMPRAS ---")
    total_general = 0  
    while True:
        articulo = input("\nIngrese el nombre del artículo que desea comprar (o 'fin' para terminar): ")
        if articulo.lower() == "fin":
            break  
        
        if articulo not in articulos:
            print(f"El artículo '{articulo}' no está en el inventario.")
            continue  
       
        while True:
            try:
                cantidad = int(input(f"Ingrese la cantidad de '{articulo}' que desea comprar: "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor que 0.")
                else:
                    break
            except ValueError:
                print("Cantidad inválida. Por favor, ingrese un número entero.")
       
        precio_unitario = articulos[articulo]
        montototal = precio_unitario * cantidad
        total_general += montototal
       
        print("\n-------------------------------------------")
        print(f"Artículo: {articulo}")
        print(f"Cantidad: {cantidad}")
        print(f"Montototal: S/{montototal:.2f}")
        print("-------------------------------------------")
        continuar = input("¿Desea comprar otro artículo? (sí/no): ").strip().lower()
        if continuar not in ["si", "sí"]:
            break
    print(f"\nTotal general de la compra: S/{total_general:.2f}")