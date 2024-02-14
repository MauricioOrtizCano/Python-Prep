#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:
def es_primo(num):
    '''
    Determina si un numero es primo o no
    '''
    if (num == 0 or num == 1 or num == 4):
        return False
    
    for i in range(2,num):
        if(num % i == 0):
            return False
        
    return True




# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:
def devolviendo_primos (lista):
    '''
    Devuelve una lista con los numeros primos
    con respecto a otra
    '''

    copia = [x for x in lista if es_primo(x) == True]
    return copia



# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:
def repetido(lista):
    '''
    Determian cual es el numero que mas se 
    repite en una lista
    '''

    copia = []
    obj = {}

    for i in lista:
        if not (i in copia):
            copia.append(i)
            cantidad = lista.count(i)
            obj[i] = cantidad
        else:
            continue

    mayor_llave = ""
    mayor_valor = 0

    for llave, valor in list(obj.items()):
        if(mayor_llave == ""):
            mayor_llave = llave
            mayor_valor = valor
        else:
            if(mayor_valor < valor):
                mayor_llave = llave
                mayor_valor = valor
            else:
                continue

    return f'{mayor_llave} es el que más se repite con {mayor_valor} veces'




# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:
def conversion_temperatura (valor, me_origen, me_destino):
    if(me_origen == "°C"):
        if(me_destino == "°F"):
            to_far = (valor * 9/5) + 32
            return f'{to_far} °F'
        else:
            to_kel = (valor + 273.15)
            return f'{to_kel} °K'
    elif(me_origen == "°F"):
        if(me_destino == "°C"):
            to_ce = (valor - 32) * 5/9
            return f'{to_ce} °C'
        else:
            to_kelv = (valor - 32) * 5/9 + 273.15
            return f'{to_kelv} °K'
    else:
        if(me_destino == "°C"):
            to_cel = valor - 273.15
            return f'{to_cel} °C'
        else:
            to_fare = (valor - 273.15) * 9/5 + 32
            return f'{to_fare} °F'


# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:




# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:
def factorial(num):
    if(num < 0 or type(num) != int):
        return "Debe ser un numero entero positivo"
    
    if (num <= 1):
        return 1
    
    num = num * factorial(num-1)

    return num




