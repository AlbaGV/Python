# Se dice una fruta y luego se pide un numero (desde 1), este numero corresponde a una letra de fruta escrita


fruta=raw_input("Dime una fruta: ")

num1=int(raw_input("Dime un numero:"))

num2=num1-1

long=len(fruta)

if num1>long:
    print "Lo siento, la fruta no tiene tantas letras"
elif num1<=long:

    print fruta[num2]