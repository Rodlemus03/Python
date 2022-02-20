from crear_vector import crear_vector
v=crear_vector(10)
def seleccion_sort(vector):
    for i in range(0,len(vector)-1):
        minimo=i
        for j in range(i+1,len(vector)):
            if(vector[j]<vector[minimo]):
                minimo=j
        vector[i],vector[minimo]=vector[minimo],vector[i]
    return vector
