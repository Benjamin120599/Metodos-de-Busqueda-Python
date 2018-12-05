'''
Created on 29/11/2018

@author: Benja
'''
from random import random
from pip._vendor.distlib.compat import raw_input

class hash_table:
    
    def __init__(self):
        self.table = [None] * 127
    
    # Hash function
    def Hash_func(self, value):
        key = 0
        for i in range(0,len(value)):
            key += ord(value[i])
        return key % 127

    def Insert(self, value):
        hash = self.Hash_func(value)
        if self.table[hash] is None:
            self.table[hash] = value
   
    def Search(self,value):
        hash = self.Hash_func(value);
        if self.table[hash] is None:
            return None
        else:
            print("Se encontro el elemento en")
            return hex(id(self.table[hash]))
  
    def Remove(self,value):
        hash = self.Hash_func(value);
        if self.table[hash] is None:
            print("No se encontro el elemento", value)
        else:
            print("Element with value", value, "deleted")
            self.table[hash] is None
            
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

    def busquedaBinaria(self, unaLista, elemento):
        
        primero = 0
        ultimo = len(unaLista) - 1
        
        while(primero <= ultimo):
            centro = int((primero + ultimo) / 2)
            valorCentro = unaLista[centro]
            print("Comparando "+str(elemento)+" con "+str(unaLista[centro]))
            
            if(elemento == valorCentro):
                return centro
            elif(elemento < valorCentro):
                ultimo = centro - 1
            else:
                primero = centro + 1
        
        return - 1
        
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
unaLista = [1, 2, 35, 76, 80, 110, 123, 340, 341, 500]

while(opcion != 10):
    
    
    print("\n                          M E N U")
    print()
    print("1) Busqueda Secuencial.")
    print("2) Busqueda Binaria. ")
    print("3) Busqueda por Funciones Hash.")
    print("10) Salir.")
    print()
    opcion = int(raw_input("Elija una opcion: "))
    
    if(opcion == 1):
        
        print()
        print("=========== BUSQUEDA SECUENCIAL ===========")
        print
        datoBuscar = int(raw_input("Ingrese el dato a buscar: "))
        if(mb.busquedaSecuencial(None, arreglo1.copy(), datoBuscar) == True):
            print("EL dato si esta")
        else:
            print("El dato no esta")
    elif(opcion == 2):
        
        print()
        print("=========== BUSQUEDA BINARIA ===========")
        print
        datoBuscar = int(raw_input("Ingrese el dato a buscar: "))
        
        print("El dato se encontro en la posicion: "+str(mb.busquedaBinaria(None, unaLista, datoBuscar)+1))
    
    elif(opcion == 3):
        
        print()
        print("=========== BUSQUEDA POR FUNCIONES HASH ===========")
        print()
        
        H = hash_table()
        H.Insert("Alo")
        H.Insert("Bou")
        H.Insert("Col")

        print(H.Search("Bou"))
        
    elif(opcion == 10):
        print("Saliendo...")
        