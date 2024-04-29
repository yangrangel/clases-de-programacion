# Clase 5 python funciones.py

#def f(x: int):
 #   return x
# print(f("hola, fui enviado como argumento"))

#def f(x: int):
#     return x

#print(f(["hola","como","te llamas"]))

#def f(x: int):
 #    return x + 1

#print(f(5))

#def suma(a,b):
#   return a + b

#print(suma(5,4))

#def suma(a,b):
#    suma = a + len(b)
#    return suma

#print(suma(4,"hola"))
# 

#def suma (a, b, c):
#    suma = a + b
#    return suma
#print(suma(4,3,8))


#def suma (a, b, c):
#    suma = a + b
#    return suma
#print(suma(4,3,8))
#print(suma(8,3,5))
#print(suma(3,4,8))

# funciones con for

def suma(numeros):
    total = 0
    for n in numeros:
        total += n
        
    return print(f"la sumatoria total es: {total}, el valor de la ultima posicion es {n}")
    
suma([1,3,5,10])
    
    