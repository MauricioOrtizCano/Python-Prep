class CalculadoraM08:
    def __init__(self, lista):
        self.lista = lista

    def es_primo(self, num):
        '''
        Determina si un numero es primo o no
        '''
        if (num == 0 or num == 1 or num == 4):
            return False
    
        for i in range(2,num):
            if(num % i == 0):
                return False
        
        return True
    
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
        else:
            if(me_destino == "°C"):
                to_cel = valor - 273.15
                return f'{to_cel} °C'
            else:
                to_fare = (valor - 273.15) * 9/5 + 32
                return f'{to_fare} °F'
            
    def factorial(self, num):
        if(num < 0 or type(num) != int):
            return "Debe ser un numero entero positivo"
    
        if (num <= 1):
            return 1
    
        num = num * self.factorial(num-1)

        return num