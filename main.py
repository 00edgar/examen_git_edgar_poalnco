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
menu()
separador()
    
