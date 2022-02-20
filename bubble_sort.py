from crear_vector import crear_vector
v=crear_vector(10)
#Version 1
def bubble_sort(vector):
    for i in range(0,len(vector)-1):
        for j in range(0,len(vector)-1-i):
            if(vector[j]>vector[j+1]):
                vector[j],vector[j+1]=vector[j+1],vector[j]
    return vector
#Version 2
def bubble_sort_mejorado(vector):
    i=0
    bandera=True
    while(i<=len(vector)-2) and bandera:
        bandera=False
        for j in range(0,len(vector)-i-1):
            if(vector[j]>vector[j+1]):
                vector[j],vector[j+1]=vector[j+1],vector[j]
                bandera=True
        i+=1
    return vector


