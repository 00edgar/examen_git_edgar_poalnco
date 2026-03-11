import json

def leer_datos():
    with open("datos.json", "r" )as registro:
        datos= json.load (registro)
        return datos

def separador():
    print ("*****************************************")
    
separador()
def menu():
    print("""
          1: para agregar servicio 
          2: para editar servicio
          3: para eliminar servicio
          4: para salir
          """)
    
def guardar(datos):
    with open("datos.json", "" )as registro: 
        json.dump(datos ,registro ,indent=4  )
        
        
    
def agregar_servicio(datos):

    servicio= input ("ingrese nombre del el servicio")
    definicion= input ("ingrese una descripcion del producto")
    precio= float (input("ingrese el costo del servicio"))
    
    nuevo_servicio={  
        "id_servicio": len(datos) + 1,
        "servicio":servicio,
        "definicion":definicion,
        "precio":precio
    }
    datos.apened(nuevo_servicio)
    guardar(datos) 
    print ("agregacion de srvicio completada")
    
def editar_servicio(datos, campo):
    id_buscar = int(input("Ingrese el ID del elemento a editar: "))

    for elemento in datos:
        if elemento["id servicio"] == id_buscar:
            nuevo_valor = input("Ingrese el nuevo valor: ")
            elemento[campo] = nuevo_valor
            guardar(datos)
            print("Elemento actualizado correctamente.\n")
            return

    print("Elemento no encontrado.\n")



    
menu()
separador()
while True:
    opc=int (input("ingrese su opcion deseada"))
    if opc==1:
        agregar_servicio()
    elif opc==2:
        editar_servicio()