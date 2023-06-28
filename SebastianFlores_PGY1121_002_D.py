import os
os.system("cls")





Menu = """
1) Registrar producto.
2) Buscar producto.
3) Listar productos.
4) Salir
"""

ListaCodigos = ['12345678','23456788','12312312']
ListaNombres = ['Ferrari','Porche','Autonose']
ListaCategorias = ['300','300','133']
ListaPrecios = [200,300,400]
ListaCantidadDispo = [20,100,10]

def funcion_registrar():
    print("Registrando Producto")
    while True:
            Codigo = (input("Ingrese codigo: "))
            if len(Codigo) != 8:
                print("Codigo tiene que ser igual a 8 numeros")
            else:
                ListaCodigos.append(Codigo)
                print("Codigo ingresado")
                print(ListaCodigos)
                break
    while True:
         Nombres = input("Ingrese nombre: ")
         if len(Nombres) >= 2 and len(Nombres) < 50:
              ListaNombres.append(Nombres)
              print("Nombre agregado")
              print(ListaNombres)
              break
         else:
              print("Nombre tiene que tener entre 2 y 50 caracteres")
    while True:
         Categorias = (input("Ingrese categoria: "))
         if len(Categorias) >= 1:
              ListaCategorias.append(Categorias)
              print("Categoria asignada")
              print(ListaCategorias)
              break
         else:
              print("Categoria no valida")
    while True:
         Precio = int(input("Ingresa Precio: "))
         if Precio > 0:
              ListaPrecios.append(Precio)
              print("Precio añadido")
              print(ListaPrecios)
              break
         else:
              print("Precio no valido")
    while True:
         CantidadDispo = int(input("Ingresa la cantidad disponible: "))
         if CantidadDispo > 0:
              ListaCantidadDispo.append(CantidadDispo)
              print("Cantidad disponible añadida")
              print(ListaCantidadDispo)
              break
         else:
              print("Cantidad no valida o no es un numero entero")

def funcion_buscar():
     print("Buscando Producto")
     Buscar = input("Ingrese el codigo de la categoria a buscar: ")
     print(f" Listado categoria: {Buscar} \n")
     print(" CODiGO   | NOMBRE               | CATEGORIA  |PRECIO| CANTIDAD DISPONIBLE  |")
     print("----------+----------------------+------------+------+----------------------+")
     for i in range(len(ListaNombres)):
          if Buscar.lower() == ListaCategorias[i].lower():
               print(f" {ListaCodigos[i]:6s} | {ListaNombres[i]:20s} | {ListaCategorias[i]:10s} | {ListaPrecios[i]:4d} | {ListaCantidadDispo[i]:20d} |")
               print("----------+----------------------+------------+------+----------------------+")


def funcion_listar():
    print("Opcion 3")
    print(" PRODUCTOS DISPONIBLES PARA LA VENTA \n")
    print(" CODiGO   | NOMBRE               | CATEGORIA  |PRECIO| CANTIDAD DISPONIBLE  | STOCK BAJO")
    print("----------+----------------------+------------+------+----------------------+-----------")
    StockBajo = 0
    for i in range(len(ListaCodigos)):
        if ListaCantidadDispo[i] < 5:
            Stock = "SI"
        else:
            Stock = "NO"
        print(f" {ListaCodigos[i]:6s} | {ListaNombres[i]:20s} | {ListaCategorias[i]:10s} | {ListaPrecios[i]:4d} | {ListaCantidadDispo[i]:20d} | {Stock}")
        print("----------+----------------------+------------+------+----------------------+-----------")
    print(f"Total de productos con bajo stock: {StockBajo}")

        


opc = 0
NombreApellido = input("Hola, Bienvenido al algoritmo de 'SUPERSTORE' Ingrese su nombre y apellido: ")
while True:
        opc = int(input(Menu))
        if opc == 1:
            funcion_registrar()
        elif opc == 2:
             funcion_buscar()
        elif opc == 3:
             funcion_listar()
        elif opc == 4:
             print(f"Adios {NombreApellido}, Vuelva Pronto ^-^")
             break
        else:    print("Opcion no valida")
    
input("Enter para terminar")








        
