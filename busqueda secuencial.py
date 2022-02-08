#Importamos la libreria para generar numeros random y la funcion para crear vectores, de otro programa
from crear_vector import crear_vector
from random import randint
#Pedimos la longitud que va a tener la lista, para crearla
longitud=int(input("Ingresa la longitud para el vector  "))
#Asignamos el la respuesta de la funcion para crear, a una variable
vector=crear_vector(longitud)
#Pedimos un numero para buscar en la lista
numero=int(input("Vector creado, ahora ingresa un numero para buscar "))
#La funcion tiene dos parametros, el numero para buscar y el vector en donde va a buscar
def busqueda(n,v):
    #Declara una variable de tipo booleana, inciada en false
    bandera=False
    posicion=0
    #Por cada vuelta en la longitud del vector en contexto
    for i in range(len(v)):
        #Si el numero a buscar, es igual al vector en la vuelta actual
        if n==v[i]:
            #Bandera cambia su valor a true
            bandera=True
            #La posicion es la vuelta actual mas uno, ya que las vueltas del for comienzan en 0 y quedaria una atras.
            posicion=i+1
    #Retorna un valor doble para descomponerlo despues
    return bandera,posicion
#Descompone la respuesta de la funcion en dos variables
respuesta,pos=busqueda(numero,vector)
#Si la respuesta es true, imprime que si se encuentra y tambien la posicion
if respuesta:
    print(f"El numero si se encuentra en la posicion {pos}")
#Si no, dice que no se encuentra.
else:
    print("El numero no se encuentra en el vector")



