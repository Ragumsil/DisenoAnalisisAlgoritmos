#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 12:31:19 2022

@author: raulguzman
"""

class Vertice:
    
    """creamos nuestro método constructor en la que vamos a definir 
    todos los atributos de nuesta clase"""
    
    def __init__(self,i):
        
        """El primer atributo que va a tener nuestro nodo es un id o un 
        nombre con el fin de poder distinguirlo de otros nodos"""
        
        self.id = i
        
        """Otro atributo que tendrá nuestra clase, será una variable
        llamada visitado y lo vamos a inicializar en FALSE"""
        
        self.visitado = False
        self.padre = None
        
        """Por último, los nodos estarán conectados por una 
        arista a algún vecino y los asignaremos a una variable """
        
        self.vecinos = []
        
        
    def agregarVecinos(self, v):
            
        """ v es el id del vecino que vamos a agregar. Primero, vamos 
            a verificar que v no esté alamacenado ya en la lista de 
            vecinos"""
            
        if v not in self.vecinos:
            self.vecinos.append(v)
                
#Ahora, crearemos una segunda clase, la cuál definirá a todo el grafo

class grafo:
    
    def __init__(self, nodos=None):
        
        if nodos is None:
            nodos = {}
        
        """dentro del método constructor, vamos a crear un diccionario;
           de esta forma, podemos guardar nuestros nodos y poder 
           identificarlos"""
           
        self.nodos = {}
        
        """creamos otro métodod para guardar a cada nodo en el grafo"""
        
    def agregarNodo(self, n):
        
        """lo primero que haremos será revisar que no esté el nodo en
           nuestro diccionario. Si no está, agregaremos una llave dentro
           de nuestro diccionario y el valor almacenado será un objeto
           de tipo Nodo con ese identificador"""
        
        if n not in self.nodos:
            self.nodos[n] = Vertice(n)
        
        """ Tendremos un siguiente método para agregar aristas entre nodos;
           va recibir los dos nodos que van a ser conectados por una arista"""
           
    def agregarArista(self, a, b):
        """Primero revisamos si los dos nodos que nos pasan, ya se encuentran
        en nuestro diccionario"""
        
        if a in self.nodos and b in self.nodos:
            self.nodos[a].agregarVecinos(b)
            self.nodos[b].agregarVecinos(a)
            
            """De esta manera estamos creando la arista que va del nodo a al b
            y viceversa"""
            
            
            
    def iterativeDFS(self,  v):
    
        import collections
        
        arbol_DFS = grafo()
        stack = collections.deque()
        stack.append(("r",v))
 
        
        while len(stack)>0:
 
            # Pop a vertex from the stack
            (source, target) = stack.pop()
 
            if self.nodos[target].visitado == False:
                self.nodos[target].visitado = True
                arbol_DFS.agregarNodo(target)
                if (source != "r"):
                    arbol_DFS.agregarArista(source, target)
                for e in self.nodos[v].vecinos:
                    stack.append((target,e))
                    
        
                    
                    
        return arbol_DFS
                            

            
    
    def bfs(self, s):
        
        arbolBFS = grafo()
        arbolBFS.agregarNodo(s)
        
        if s in self.nodos:
            cola = [s]
            
            self.nodos[s].visitado = True
            self.nodos[s].nivel = 0
            
            while(len(cola) > 0):
                v = cola[0]
                cola = cola[1:]
                
                for e in self.nodos[v].vecinos:
                    if self.nodos[e].visitado == False:
                        cola.append(e)
                        self.nodos[e].visitado = True
                        self.nodos[e].nivel = self.nodos[v].nivel + 1
                        arbolBFS.agregarNodo(e)
                        arbolBFS.agregarArista(v, e)
      
        
        return arbolBFS
    
    
    
   
    def dfs(self,r):
        
        arbolDFS_r = grafo()
        return self.dfs_recursivo(arbolDFS_r, r)
    
    def dfs_recursivo(self, arbolDFS_r, r):
        
        
        
        if r in self.nodos:
            self.nodos[r].visitado = True
            
            for nodo in self.nodos[r].vecinos:
                if self.nodos[nodo].visitado == False:
                    self.nodos[nodo].visitado = True
                    self.nodos[nodo].padre = r
                    arbolDFS_r.agregarNodo(nodo)
                    arbolDFS_r.agregarArista(r,nodo)
                    self.dfs_recursivo(arbolDFS_r, nodo)
            
                    
        return arbolDFS_r
    
                      
        



#Modelos


def ErdosRenyi(nodos,aristas, directed = False):
    
    """En el modelo de Erdös y Rènyi, se trata de crear n vértices y elegir 
    uniformemente al azar m distintos pares de distintos vértices"""
    
    import random
    
    g = grafo()
    l = []
    for i in range(nodos):
        l.append(i)
    for vertice in l:
        g.agregarNodo(vertice)
    for m in range(aristas):
        n1 = random.randint(0,nodos)
        n2 = random.randint(0,nodos)
        g.agregarArista(n1, n2)
        
            

    
    return g     
   
        
def Gilbert(nodos,p, directed = False):

        """ 
        En el modelo de Gilbert, tenemos dos parámetros, n ( el número de nodos) 
        y p(una probabilidad). Consiste en crear n vértices y poner una arista 
        entre cada par independiente y uniformemente con probabilidad p."""

        import random

        g = grafo()
        l = []
        for i in range(nodos):
            l.append(i)

        for vertice in l:
            g.agregarNodo(vertice)

        for u in l:
            for v in l:
                if random.random() <= p:
                    g.agregarArista(u, v)

        for v in g.nodos:
            print(v, g.nodos[v].vecinos)
        
        return g
                
    
    
    
def Malla(m,n, directed = False):
    g = grafo()
    for v in range(m * n):
        g.agregarNodo(v)
    index = 0
    for i in range(m):
        for j in range(n):
            if i != (m - 1):
                g.agregarArista(index, (index + n))
            if j != (n - 1):
                    g.agregarArista(index, (index + 1))
            index = index + 1
    
    return g



def GeograficoSimple(n,r, directed = False):
    
    """Colocar n nodos en un rectángulo unitario con coordenadas uniformes 
    (o normales) y colocar una arista entre cada par que queda en distancia 
    r o menor"""
    
    import random
    import numpy as np
    
    g = grafo()
    coordenadas = []
    
    for v in range(n):
        g.agregarNodo(v)
        
    for i in g.nodos:
        for j in g.nodos:
            coordenadas.append([random.random(),random.random()])
            distancia = np.sqrt(coordenadas[j][0]**2 + coordenadas[j][1]**2)
            
            if distancia <= r:
                g.agregarArista(i, j)

    return g           


            
def BarabasiAlbert(n,d, directed = False):
    
    """ Consiste en colocar "n" vértices uno por uno, asignando a cada uno 
    "d" aristas a vértices distintos de tal manera que la probabilidad 
    de que el vértice nuevo se conecte a un vértice existente "v" es 
    proporcional a la cantidad de aristas que "v" tiene actualmente
    -los primeros "d" vértices se conecta todos a todos. """
    
    import random
    g = grafo()
    
    #Primero crearemos un número de nodos igual a las aristas incluidas
    # para poder comenzar a organizarlos
    
    for v in range(d):
        g.agregarNodo(v)
    #Y comenzamos a generar las conexiones
    for i in range(d):
        for j in range(d):
            if len(g.nodos[i].vecinos) < d and len(g.nodos[j].vecinos) < d:
                g.agregarArista(i, j)
                
    #Una vez que tenemos las primeras conexiones, comenzamos a agregar aristas
    # en los demás
    
    for v in range(d,n):
        g.agregarNodo(v)
        for j in range(v):
            #Las siguientes conexiones estarán sujetas al grado de cada nodo
            
            p = 1 - (len(g.nodos[j].vecinos) / len(g.nodos))
            if len(g.nodos[i].vecinos) < d and len(g.nodos[j].vecinos) < d and p >= random.random():
                g.agregarArista(i, j)
    

                
    return g
    
        
        
def dorogovtsev_mendes(n, directed=False):

    import random
    # Validación para el parámetro
    if n < 3:
        raise ValueError("n parameter must to be >= 3 ")

    g = grafo()

    # Create 3 vertex and 3 edges to form triangle
    for v in range(3):
        g.agregarNodo(v)
    for i in range(3):
        j = i + 1 if i < 2 else 0
        g.agregarArista(i, j)
        
    for i in range(3, n):
        g.agregarNodo(i)
        # Select random edge of the graph
        id_edge = random.randint(0, len(g.nodos) - 1)
        edge_selected = g.nodos[id_edge]
        (source, target) = id_edge, edge_selected
        # Create edges between new vertice and origin and source of edge selected 
        g.agregarArista(i, source)
        g.agregarArista(i, target)
        g.agregarArista(source,target)
        
        

    return g