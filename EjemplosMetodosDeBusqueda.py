'''
Created on 29/11/2018

@author: Benja
'''
from random import random
from pip._vendor.distlib.compat import raw_input

class MetodosDeBusqueda:
    
    def busquedaSecuencial(self, vector, datoBuscar):
        pos = 0
        encontrado = False
        
        while pos < len(vector) and not encontrado:
            if(vector[pos] == datoBuscar):
                encontrado = True
            else:
                pos = pos+1
        
        return encontrado
    
    def vector100(self):
        vector = []
        numeroAleatorio = 0
        for i in range(0, 100):
            numeroAleatorio =  (int)(random() * 1000) + 1
            vector.insert(i, numeroAleatorio)
        
        return vector;
    
    def mostrarVector(self, vector):
        
        contador = 0
        
        for i in range(0, len(vector)):
            if(contador == 15):
                print("["+str(vector[i])+"] -- ")
                contador=0
            else:
                print("["+str(vector[i])+"] -- ", end=' ')
            
            contador = contador + 1
        
        print("\n")



mb = MetodosDeBusqueda

arreglo1 = mb.vector100(None)
mb.mostrarVector(None, arreglo1)

opcion = 0

while(opcion != 10):
    
    print("\n                          M E N U")
    print()
    print("1) Busqueda Secuencial.")
    print("10) Salir.")
    print()
    opcion = int(raw_input("Elija una opcion: "))
    
    if(opcion == 1):
        
        print()
        print("=========== BUSQUEDA SECUENCIAL ===========")
        print
        datoBuscar = int(raw_input("Ingrese el dato a buscar"))
        if(mb.busquedaSecuencial(None, arreglo1.copy(), datoBuscar) == True):
            print("EL dato si esta")
        else:
            print("El dato no esta")
        