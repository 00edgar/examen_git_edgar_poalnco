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
        
        
    
def agregar_servicio():
    id_servicio= input ("ingrese identificador")
    servicio= input ("ingrese nombre del el servicio")
    definicion= input ("ingrese una descripcion del producto")
    precio= float (input("ingrese el costo del servicio"))
    
    nuevo_servicio={
        "id_servicio",id_servicio,
        "servicio",servicio,
        "definicion",definicion,
        "precio",precio
    }
    datos.apened(nuevo_servicio)
    guardar(datos) 
    print ("agregacion de srvicio completada")
    
    
menu()
separador()
while True:
    opc=int (input("ingrese su opcion deseada"))
    if opc==1:
        agregar_servicio()