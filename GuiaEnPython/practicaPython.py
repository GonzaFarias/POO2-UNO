#Ejercicio 1:

from asyncio.windows_events import NULL
from random import randint


print("----------------------------------------------------------------------------------------")  

def esPrimo(numero):
    if(numero == 0 or numero == 1 or numero == 4):
        return False
    for i in range(2, numero):
        if(numero % i == 0):
            return False
    return True

print("Ejercicio 1: ",esPrimo(15),"\n----------------------------------------------------------------------------------------")  

#Ejercicio 2:

def sumaMultiplos(numero):
    acum=0
    for x in range(0,numero):
        if(3*x<numero):
            acum+=3*x
        else:
            break    
        if(5*x<numero):
            acum+=5*x
    return acum

print("Ejercicio 2: ",sumaMultiplos(10),"\n----------------------------------------------------------------------------------------")          


#Ejercicio 3:

def estaOrdenado(arr):

    estaOrd = True
    cont=0
    for a in range(0,len(arr)):
        +cont
        if(len(arr)==(a+1)):
            break
        if(arr[a]<arr[a+1]):
            estaOrd=False
            break
    return estaOrd    

numeros = [9,8,5,2,1]
numeros2 = [1,4,2,9,1,2,6,8,9]
print("Ejercicio 3: ",estaOrdenado(numeros))
print("Ejercicio 3: ",estaOrdenado(numeros2),"\n----------------------------------------------------------------------------------------")


#Ejercicio 4:

def sumaPosicionesPares(arr):
    acum = arr[0]
    for x in range(2,len(arr)):
        if(x%2==0):
            acum+=arr[x]
    return acum

lista = [1, 2, 13 ,4, 8, 6]
print("Ejercicio 4: ",sumaPosicionesPares(lista),"\n----------------------------------------------------------------------------------------")


#Ejercicio 5:

def sumaMatrices(arr1,arr2):
    for x in range(0,len(arr1)):
        for j in range(0,len(arr1)):
            arr1[x][j]=arr1[x][j]+arr2[x][j]
    return arr1

matriz1 = [[1,2,3],[1,5,3],[5,2,3]]
matriz2 = [[1,2,3],[1,5,3],[15,2,3]]
print("Ejercicio 5: ",sumaMatrices(matriz1,matriz2),"\n----------------------------------------------------------------------------------------")

#Ejercicio 6:

def intercalarArrays(arr1,arr2):
    if(estaOrdenado(arr1)==False or estaOrdenado(arr2)==False):
        print("Mandame arrays ordenados")
        return NULL
    sumaArr=arr1+arr2
    for i in range(0,(len(sumaArr)-1)):      
         mayor = sumaArr[i]                                      
         pos = i                        
         for j in range(i+1,len(sumaArr)): 
              if (sumaArr[j] > mayor):        
                 mayor = sumaArr[j]           
                 pos = j
         if (pos != i):                                             
             aux = sumaArr[i]
             sumaArr[i] = sumaArr[pos]
             sumaArr[pos] = aux
    return sumaArr
                
arr1=[10,9,4,3,-5,-9]  
arr2=[15,8,7,5,4,2,1]  
           
print("Ejercicio 6: ",intercalarArrays(arr1,arr2),"\n----------------------------------------------------------------------------------------")

#Ejercicio 7:

def adivinar(opcion):
    numero = randint(0,1000)
    contador = 0
    flag = True
    while flag==True:
        contador+=1
        if(opcion==numero):
            flag = False
            return "Cantidad de intentos: ",contador
        elif(opcion=="*"):
            flag = False
            return numero    

print("Ejercicio 7: ",adivinar("*"),"\n----------------------------------------------------------------------------------------")

#Ejercicio 8:

def mediaMayorDiagonal(matriz):
    tamDiagonal = len(matriz)
    elementosFueraDiagonal=(tamDiagonal*tamDiagonal)-tamDiagonal
    acum=0
    diagonal=0
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz)):
            if(i!=j):
                acum+=matriz[i][j]
            else:
                diagonal+=matriz[i][j]
    media=acum/elementosFueraDiagonal
    if(media>(diagonal/tamDiagonal)):
        return True
    else: return False

matriz8a = [[1,2,4],[8,5,4],[4,9,2]]
matriz8b = [[12,4,4],[4,15,4],[4,4,12]]

print("Ejercicio 8: ",matriz8a,"Elementos fuera diagonal son superiores a ella: ",mediaMayorDiagonal(matriz8a))
print("Ejercicio 8: ",matriz8b,"Elementos fuera diagonal son superiores a ella: ",mediaMayorDiagonal(matriz8b),"\n----------------------------------------------------------------------------------------")
        
#Ejercicio 9:

#No entendi como hacerlo xd

#Ejercicio 10:

def consonantes(cadena):

    vocales="aeiou"

    for i in range(len(vocales)):
        cadena = cadena.replace(vocales[i],"")
    return cadena

print("Ejercicio 10: ",consonantes("Gonzalo Farias"),"\n----------------------------------------------------------------------------------------")

#Ejercicio 11:

def frecuencias(cadena):

    letras="abcdefghijklmnñopqrstuvwxyz"
    letrasM="ABCDEIOFGHIJKLMNÑOPQRSTUVWXYZ"
    aparicion=">\n"
    arrLetras=[]
    arrLetrasM=[]
    for x in letras:
        arrLetras.append(x)
    arrLetrasM=list(letrasM)

    #Hago vector  con contadores en 0:   
    arrContadores=arrLetras
    for x in range(0,len(arrContadores)):
        arrContadores[x]=0

    arrLetras=list(letras)
    
    #Cuento repeticion de letras en la cadena
    for i in cadena:
        for j in range(0,len(arrContadores)):
            if(arrLetras[j] is i or arrLetrasM[j] is i):
                arrContadores[j]+=1
    for x in range(0,len(arrContadores)):
        cont=str(arrContadores[x])
        aparicion+=""+arrLetras[x]+": "+cont+"\n" 
    return aparicion

print("Ejercicio 11:\n",frecuencias("Hola me llamo Gonzalo Farias"),"\n----------------------------------------------------------------------------------------")

#Ejercicio 12:

class Hotel:
    def __init__(self, cantidadHabitaciones):
         self.cantidadHabitaciones = cantidadHabitaciones
         self.habitacion=[]
         self.contador=0 

    def ocuparHabitacionCon(self,mayores,menores):
        self.contador+=1
        if((mayores+menores)>8):
            return "No se puede ocupar, el limite es de 8 personas por habitación"
        if(self.contador<=self.cantidadHabitaciones):
            self.habitacion.append(Habitacion(mayores,menores,True))
            mayores=str(mayores)
            menores=str(menores)
            return "Habitacion creada: "+mayores+" "+menores
        elif(self.contador>self.cantidadHabitaciones): 
            return "Ya no hay habitaciones disponibles"  

    def __str__(self):
        canth=str(self.cantidadHabitaciones)
        cadena = "Habitaciones: "+canth
        return cadena        

    def mostrarHabitaciones(self):
        lol=""
        for obj in self.habitacion:
                a = str(obj)
                lol+="["+a+"]"
        return lol        

    def totalPersonas(self):
        contador = 0
        for obj in self.habitacion:
            contador+=obj.personas
        return contador  

    def contarHabitacionesCon(self,mayores):
        contador = 0
        for obj in self.habitacion:
            if(mayores==obj.mayores):
                contador+=1
        return contador

    def arrayTamNueve_HabitacionesConIndicePersonas(self):
        array = []
        contador = 0
        for i in range(0,9):
            for habitacion in self.habitacion:
                if(habitacion.personas == i):
                    contador+=1      
            array.append(contador)
            contador = 0
        return array            

class Habitacion:
    def __init__(self,mayores,menores,ocupada):
        self.menores=menores
        self.mayores=mayores
        self.personas=self.menores+self.mayores
        self.ocupada=ocupada

    def __str__(self):
        mayor=str(self.mayores)
        menor=str(self.menores)
        ocu=str(self.ocupada)
        cadena = "Mayores: "+mayor+", Menores: "+menor+", Ocupada: "+ocu
        return cadena     

print("Ejercicio 12:\n")

hotel = Hotel(9)
hotel.ocuparHabitacionCon(4,3)
hotel.ocuparHabitacionCon(3,4)
hotel.ocuparHabitacionCon(1,3)
hotel.ocuparHabitacionCon(4,2)
hotel.ocuparHabitacionCon(8,0)
hotel.ocuparHabitacionCon(3,1)
hotel.ocuparHabitacionCon(5,2)
hotel.ocuparHabitacionCon(2,6)
hotel.ocuparHabitacionCon(4,2)

print("Hotel -",hotel)
print(hotel.ocuparHabitacionCon(2,2))
print(hotel.mostrarHabitaciones())
print("Habitaciones con mayores indicados: ",hotel.contarHabitacionesCon(4))
print("Total de personas ocupando las habitaciones: ",hotel.totalPersonas())
print(hotel.arrayTamNueve_HabitacionesConIndicePersonas())

