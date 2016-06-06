# fibonacci.py
def fib(i):  # Definicion de la funcion
    a = 0
    b = 1
    c = 0
    while c < i:
        print c,  # Mostramos el resultado por pantalla
        a = b
        b = c
        c = a + b


fib(100)  # Llamamos a la funcion con el Fibonacci hasta 100