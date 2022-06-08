from asyncio.windows_events import NULL
from io import open
import networkx as nx
import matplotlib.pyplot as plt

class Rescate:

    def __init__(self): 

        self.dragones=0
        self.nodos=0
        self.senderos=0
        self.posicionPrincesa=''
        self.posicionPrincipe=''
        self.posicionDragones=[]
        self.aristas = []
        self.Grafo=NULL
        self.out = open("rescate.out","w")

    def leerDatos(self,archivo):

        archivo = open(archivo,"r")
        frase = archivo.readlines()
        
        string = str.split(frase[0]) #Lectura datos del archivo y manejo de excepciones para efectuar el correcto manejo segun las 
        self.nodos=int(string[0])    #condiciones dadas por la consigna   

        if((self.nodos>=2 and self.nodos<=100000)==False):
            raise NameError("La cantidad de nodos debe ser 2 <= N <= 100000")
        self.senderos=int(string[1])

        if((self.senderos>=0 and self.senderos<=600000)==False):
            raise NameError("La cantidad de senderos debe ser 0 <= S <= 600000")
        self.dragones=int(string[2])

        if((self.dragones>=0 and self.dragones<=100)==False):
            raise NameError("La cantidad de dragones debe ser 0 <= D <= 100")
        string = str.split(frase[1])

        self.posicionPrincesa = string[0]
        self.posicionPrincipe = string[1]
        self.posicionDragones = str.split(frase[2])
        

        for x in range(3,len(frase)): #Obtengo las aristas
            dato = str.split(frase[x])
            if((1 <= int(dato[0]) <= self.nodos) == False 
            or (1 <= int(dato[1]) <= self.nodos) == False):
                raise NameError("Se debe respetar:\nEl nodo inicial ni (1 ≤ ni ≤ n)\nEl nodo final nf (1 ≤ nf ≤ n)")  
            dato[2] = int(dato[2])
            if((0<dato[2]<=1000)==False):
                raise NameError("El largo l del sendero debe ser (0 < l ≤ 1000)")
            self.aristas.append(dato)
        print("Aristas: ",self.aristas) 

    def creoGrafo(self):  #Se crea el grafo a partir de los datos obtenidos en el archivo
        
        vertices =[]
        self.Grafo = nx.Graph() 
        for i in range (1,(self.nodos+1)):
             vertices.append(str(i)) 
        self.Grafo.add_nodes_from(vertices) 
        self.Grafo.add_weighted_edges_from(self.aristas)
               
    def buscarCamino(self):

        try:   
            #Se busca camino con dijkstra dando como nodo inicial al principe y nodo final a la princesa
            grafico=nx.dijkstra_path(self.Grafo, self.posicionPrincipe, self.posicionPrincesa)
            nx.draw(self.Grafo, pos=nx.circular_layout(self.Grafo),node_size=650, node_color = '#ffff8f', edge_color='black', with_labels=True)   
            plt.show()
            cruzaDragon=False 
            camino=''
            for x in grafico:   #Se busca que el principe no se cruce con ningun dragón
                for i in self.posicionDragones:
                    if(x == i):
                        cruzaDragon=True
            if(cruzaDragon==False):
                self.out.write("Puntaje: 100\n")  #Se escribe el máximo puntaje 
                for x in grafico:
                    camino+=x+" "
                self.out.write(camino)    

        except nx.exception.NetworkXNoPath: 
            self.out.write("No hay camino")  #No se encontró camino al no conectar aristas desde el principe a la princesa
            
        try:
            if(cruzaDragon==True):

                #Verifico camino esquivando dragones
                for x in self.posicionDragones:
                    self.Grafo.remove_node(x)
                grafico=nx.dijkstra_path(self.Grafo, self.posicionPrincipe, self.posicionPrincesa)
                for x in grafico:
                    camino+=x+" " 
                self.out.write("Puntaje: 70\n") #El principe llegó, pero no siendo el camino minimo por evitar los dragones    
                self.out.write(camino)  

        except nx.exception.NetworkXNoPath: 
            self.out.write("Interceptado") #No hubo camino seguro, en todos fue interceptado por dragón

        self.out.close   

        print("Nodos: ",self.nodos)
        print("Senderos: ",self.senderos)
        print("Dragones: ",self.dragones)
        print("Posicion Princesa: ",self.posicionPrincesa)
        print("Posicion Principe: ",self.posicionPrincipe)
        print("Posicion Dragones: ",self.posicionDragones) 
        
obj = Rescate()
obj.leerDatos("rescate.in")
obj.creoGrafo()
obj.buscarCamino()
