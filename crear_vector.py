from random import randint
def crear_vector(longitud):
    v=[]*longitud
    for i in range(longitud):
        x=randint(1,100)
        v.append(x)
    return v
