from crear_vector import crear_vector
v=crear_vector(10)
def insercion_sort(vector):
    for i in range(1,len(vector)+1):
        k=i-1
        while(k>0)and(vector[k]<vector[k-1]):
            vector[k],vector[k-1]=vector[k-1],vector[k]
            k-=1
    return vector
