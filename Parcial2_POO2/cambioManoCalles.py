from asyncio.windows_events import NULL
from io import open
import networkx as nx

class CambioDeMano:

    def __init__(self): #Se inicia el objeto del ejercicio dado, con sus correspondientes atributos.

        self.esquinas=0
        self.callesCambiar=[]
        self.pesoMinimo=0
        self.inicioColectivo=''
        self.ubicacionEscuela=''
        self.aristas = []
        self.Grafo=NULL
        self.out = open("casosPrueba/cambio3.out","w")
        self.caminoMinimo=[]

    def leerDatos(self,archivo):
        archivo = open(archivo,"r")
        frase = archivo.readlines()
        string = str.split(frase[0]) #Lectura datos del archivo y manejo de excepciones para efectuar el correcto manejo segun las 
        self.esquinas=int(string[0]) #condiciones dadas por la consigna .

        if((self.esquinas>=1 and self.esquinas<=80000)==False):
            raise NameError("La cantidad de esquinas debe ser 1 <= N <= 100000")
        self.inicioColectivo=string[1]
        self.ubicacionEscuela=string[2]
        string = str.split(frase[1])

        for x in range(2,len(frase)): #Obtengo las aristas
            dato = str.split(frase[x])
            dato[2] = int(dato[2])
            if((0<dato[2]<=50)==False):
                raise NameError("El largo l de la calle debe ser (0 < l ≤ 50)")
            self.aristas.append(dato)
        print("Calles: ",self.aristas) 

    def creoGrafo(self):  #Se crea el grafo a partir de los datos obtenidos en el archivo
        self.Grafo = nx.Graph() 
        self.Grafo.add_weighted_edges_from(self.aristas)

    def cambiarManos(self):
        try: #Se busca camino con dijkstra dando como nodo inicial al bondi y nodo final a la escuela
            self.caminoMinimo=nx.dijkstra_path(self.Grafo, self.inicioColectivo, self.ubicacionEscuela)
            self.pesoMinimo=nx.dijkstra_path_length(self.Grafo, self.inicioColectivo, self.ubicacionEscuela)
        except nx.exception.NetworkXNoPath: 
            self.out.write("No hay camino")  #No se encontró camino al no conectar aristas desde el bondi a la escuela

        #- Almacenamos la cantidad de elementos del recorrido de dijkstra en la variable contador
        #.inicializamos una variable numeroCalle en 1 para tener una referencia sobre las aristas
        # que estamos iterando para buscar coincidencia con las obtenidas en el recorrido dijkstra
        #- Para cambiar la mano de las calles vamos a comparar el recorrido de las calles obtenidos
        # al realizar dijkstra con el recorrido de las calles del grafo pero invertidas,
        # simulando así el cambio de mano, si coinciden, se agrega el número de la calle
        # a un array que almacena las calles que se deben cambiar de mano
            
        contador = len(self.caminoMinimo)
        numeroCalle=1
        for i in self.aristas:
            recorridoEsquinasCalle = [i[1],i[0]]
            for j in range(1,contador):
                recorridoEsquinasDijkstra = [self.caminoMinimo[j-1],self.caminoMinimo[j]]
                if recorridoEsquinasDijkstra == recorridoEsquinasCalle:
                    self.callesCambiar.append(numeroCalle)
            numeroCalle+=1

    def escribirArchivo(self): #Se realiza la escritura del archivo, implementando validaciones para escribir diferente
        texto=""               #dependiendo del caso
        if(self.pesoMinimo!=0):
            self.out.write(str(self.pesoMinimo)+"\n")
        for x in self.callesCambiar:
            texto+=str(x)+" "
        if(self.callesCambiar==[]):
            self.out.write("No hubo que alterar el sentido de las calles")    
        self.out.write(texto)

obj = CambioDeMano()
obj.leerDatos("casosPrueba/cambio3.in")
obj.creoGrafo() 
obj.cambiarManos()
obj.escribirArchivo()