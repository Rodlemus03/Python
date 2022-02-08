x=int(input("Ingresa un numero para buscar en la secuencia fibonacci "))

def fibonacci_recursivo(n):
    if(n==0 or n==1):
        return n
    else:
        return fibonacci_recursivo(n-1)+fibonacci_recursivo(n-2)
def fibonacci_iterativo(n):
    n0=0
    n1=1
    fib=0
    if(n==0 or n==1):
        fib=n
    else:
        i=2
        while(i<=n):
            fib=n0+n1
            n0=n1
            n1=fib
            i+=1
    return fib
print(fibonacci_iterativo(x))
print(fibonacci_recursivo(x))
        
