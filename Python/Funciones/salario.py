# Ingresa 2 parametros, las horas trabajadas (mas de 40 son extraordinarias y se cuentan por 1.5 mas) , y el salario por hora

def computo(h,d):
    if h>40:
        extra=h-40
        total=extra*d*1.5 + 40*d
    elif h<40:
        total=h*d
    return total

h=int(raw_input("Dime cuantas horas: "))
d=int(raw_input("Dime cuanto cobras por hora: "))

print "Trabajas", h, "horas a", d, "euros, esto hace un total de", computo(h,d), "euros."