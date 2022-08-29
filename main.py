from claseColaSecuencial import ColaSecuencial
from claseColaEncadenada import ColaEncadenada

def testColaSecuencial():
    objCola = ColaSecuencial()
    objCola.suprimir()
    x1 = 2
    x2 = 3
    objCola.insertar(x1)
    objCola.insertar(x2)
    print('Antes de suprimir: ')
    objCola.recorrer()
    objCola.suprimir()
    print('Despues de suprimir: ')
    objCola.recorrer()

def testColaEnlazada():
    objCola = ColaEncadenada()
    objCola.insertar(1)
    objCola.insertar(2)
    print('Antes de suprimir: ')
    objCola.recorrer()
    objCola.suprimir()
    print('Despues de suprimir: ')
    objCola.recorrer()
    

if __name__ == '__main__':
    print('Test cola secuencial')
    testColaSecuencial()
    print('Test cola encadenada')
    testColaEnlazada()

  
