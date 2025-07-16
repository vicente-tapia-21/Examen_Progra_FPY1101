#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
        '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
        'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
        'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
        'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
        '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
        '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
        'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
                }
#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
        }

def funcion_stock():
    marca = input("Ingrese maraca a consultar: ")
    marca = marca.lower()
    total = 0
    for modelo in productos:
        if productos[modelo][0].lower() == marca:
            total = total + stock[modelo][1]
            print(f"El stock es: {total}")

def funcion_busqueda():
    while True:
        try:
            precio_min = int(input("Ingrese precio minimo: "))
            precio_max = int(input("Ingrese precio máximo: "))
            break
        except:
            print("Debe ingresar valores enteros!!")
            
        lista_resultado = []

        for modelo in stock:
            precio = stock[modelo][0]
            cantidad = stock[modelo][1]
            if precio >= precio_min and precio_max <= precio_max and cantidad > 0:
                nombre_marca = productos[modelo][0]
                lista_resultado.append(nombre_marca + "--" + modelo)
                
        if len(lista_resultado) == 0:
            print("No hay notebooks en ese rango de precios.")
        else:
            lista_resultado.sort()
            print(f"Los notebooks entre los precios consutados son: {lista_resultado}")

def funcion_actualizar():
    seguir = "si"
    while seguir == "si":
        modelo = (input("Ingrese modelo a actualizar: "))
        if modelo in productos:
            del productos[modelo]
            del stock[modelo]
            print("Producto eliminado!!")
        else:
            print("El producto no existe!!")
        
        seguir = input("¿Desea eliminar otro producto? (s/n): ")
        seguir = seguir.lower()

while True:
    print("""
    ***MENÚ PRINCIPAL
    1. Stock marca.
    2. Búsqueda por precio.
    3. Actualizar precio.
    4. Salir.""")
    
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        funcion_stock
        continue
        
    elif opcion == "2":
        funcion_busqueda
        continue

    elif opcion == "3":
        funcion_actualizar
        continue

    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Debe ingresar una opción válida.")