


############### Ejercicio 26 ###############
def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma
    
    
#programa principal:
num=int(input("Numero a procesar: "))
while num!=0:
    print("Suma:",sumaDigitos(num))
    num=int(input("Numero a procesar: "))