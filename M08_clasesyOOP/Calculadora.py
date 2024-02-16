class CalculadoraM08:
    def __init__(self, lista):
        if (type(lista) != list):
            self.lista = []
            raise ValueError('Debe ser pasado como parametro una lista')
        else:
            self.lista = lista
        

    def es_primo(self):
        '''
        Determina si un numero es primo o no
        '''
        def demostrar(numero):
            if (numero == 0 or numero == 1 or numero == 4):
                return False
        
            for i in range(2,numero):
                if(numero % i == 0):
                    return False
            
            return True
        
        primos = []

        for i in self.lista:
            primos.append(demostrar(i))

        return primos


    
    def repetido(self):
        '''
        Determian cual es el numero que mas se 
        repite en una lista
        '''

        copia = []
        obj = {}

        for i in self.lista:
            if not (i in copia):
                copia.append(i)
                cantidad = self.lista.count(i)
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

        return mayor_llave, mayor_valor
    
    def conversion_temperatura (self, valor, me_origen, me_destino):
        
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
        elif(me_origen == "°K"):
            if(me_destino == "°C"):
                to_cel = valor - 273.15
                return f'{to_cel} °C'
            else:
                to_fare = (valor - 273.15) * 9/5 + 32
                return f'{to_fare} °F'
        else:
            raise ValueError("Las medidas de origen o de destino deben ser °C, °K, °F")

            
    def factorial(self, num):
        if(num < 0 or type(num) != int):
            return "Debe ser un numero entero positivo"
    
        if (num <= 1):
            return 1
    
        num = num * self.factorial(num-1)

        return num
    



imprimir = CalculadoraM08([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

print(imprimir.es_primo())