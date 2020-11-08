def sumaTodos(limitTo):
    resultado = 0
    for i in range (0, limitTo+1):
        resultado += i
    
    return resultado

'''int(Numero) = input("Dame un número para contar: ")
numero = int(strNumero)'''

print (sumaTodos(100))