import sys
import unittest

sys.path.append(r'c:\Users\USER\Documents\Todos Mis documentos\Curso python\Python Henry\Python-Prep\M08_clasesyOOP')
#print(sys.path)

from Calculadora import CalculadoraM08

convertir = CalculadoraM08([1])

#print(convertir.conversion_temperatura(38, "°Celcius", "°F"))



class PruebaPrimosTest(unittest.TestCase):
    def test_de_primos(self):
        imprimir = CalculadoraM08([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
        resultado = imprimir.es_primo()

        self.assertEqual(resultado, [False, True, True, False, True, False, True, False, False, False, True, False, True, False, False])




unittest.main(argv=[''], verbosity=2, exit=False)





