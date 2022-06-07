#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 14:49:00 2022

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
        
        """Creamos un nuevo atributo dentro del constructor, el cual es la distancia
        inicializada en el infinito"""
        
        self.distancia = float("inf")
        
        
    def agregarVecinos(self, v, p):
            
        """ v es el id del vecino que vamos a agregar. Primero, vamos 
            a verificar que v no esté alamacenado ya en la lista de 
            vecinos"""
            
        if v not in self.vecinos:
            self.vecinos.append([v, p])
                
#Ahora, crearemos una segunda clase, la cuál definirá a todo el grafo

class grafo:
    
    def __init__(self, nodos=None, attr = {}):
        
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
           
    def agregarArista(self, a, b, p):
        """Primero revisamos si los dos nodos que nos pasan, ya se encuentran
        en nuestro diccionario; ahora también recibe un tercer valor, el peso de la arista"""
        
        if a in self.nodos and b in self.nodos:
            self.nodos[a].agregarVecinos(b, p)
            self.nodos[b].agregarVecinos(a, p)
            
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
                    
        from graphviz import Graph
        dot = Graph()
        
        for v in arbol_DFS.nodos:
            dot.node(str(v),str(v))
            for j in arbol_DFS.nodos[v].vecinos:
                dot.edge(str(v),str(j))
        dot.render("/Volumes/Seagate/Maestria/CIC/Diseno_algoritmos/Grafos/Proyecto2/ErdosRenyi/iterativeDFSErdosRenyi500.gv",view=True)
                    
        #for v in arbol_DFS.nodos:
         #       print(v, arbol_DFS.nodos[v].vecinos)
                    
                    
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
    

    
    def camino_calculado_dijkstra(self, a, b):
        
        camino = []
        actual = b
        
        while actual != None:
            camino.insert(0,actual)
            actual = self.nodos[actual].padre
            
        return [camino,self.nodos[b].distancia]
       
    
    def minimo(self,lista):
        
        if len(lista) > 0:
            m = self.nodos[lista[0]].distancia
            v = lista[0]
            for elemento in lista:
                if m > self.nodos[elemento].distancia:
                    m = self.nodos[elemento].distancia
                    v = elemento
                    
            return v
    
    
    def dijkstra(self, a):
        
        """Recibe un nodo a, donde inciaremos nuestro recorrido, de tal manera que
        se calcule el árbol de caminos más cortos"""

        g = grafo()
        g.agregarNodo(a)
        
        if a in self.nodos:
            self.nodos[a].distancia = 0
            actual = a
            noVisitados = []

            for nodo in self.nodos:
                if nodo != a:
                    self.nodos[nodo].distancia = float("inf")
                self.nodos[nodo].padre = None
                noVisitados.append(nodo)

            while len(noVisitados) > 0:
                for vecino in self.nodos[actual].vecinos:
                    if self.nodos[vecino[0]].visitado == False:
                        if self.nodos[actual].distancia + vecino[1] < self.nodos[vecino[0]].distancia:
                            self.nodos[vecino[0]].distancia = self.nodos[actual].distancia + vecino[1]
                            self.nodos[vecino[0]].padre = actual
                            g.agregarNodo(vecino[0])
                            g.agregarArista(actual, vecino[0], self.nodos[actual].distancia + vecino[1] )
                            
                self.nodos[actual].visitado = True
                noVisitados.remove(actual)
                
                actual = self.minimo(noVisitados)
          
        else:
                
            return False
        
        from graphviz import Graph
        dot = Graph()
        
        for v in g.nodos:
            dot.node(str(v),str(v))
            for j in g.nodos[v].vecinos:
                dot.edge(str(v),str(j[0]))
        dot.render("/Volumes/Seagate/Maestria/CIC/Diseno_algoritmos/Grafos/Proyecto3/Dijkstra/dijkstra500.gv",view=True)
        
        return g
    
    
    
    
    def find(self, parent, i):
        
        if parent[i] == i:
            return i
        return self.fins(parent,parent[i])
    
    def clone(self):
        g = grafo(nodos=self.nodos.copy(),
        edges=self.edges.copy())
        return g
    
    
    def KrustalD(self):
    
        import numpy as np
    
        ArbolEM = grafo()
    
        parent = []
        rank =[]
    
        for v in self.nodos:
            parent.append(v)
            rank.append(0)
        
        #Ordenamos las aristas por sus pesos
        enlaces=[]
        for v in self.nodos:
            for j in self.nodos[v].vecinos:
                enlaces.append([(v,j[0]), j[1]])
            
        q = np.sort(enlaces, axis=0)
    
        #insertamos las aristas en el arbol de expasión evitando ciclos
    
        for e in q:
            (u,v) = q[0]
            v1 = self.find(parent,u)
            v2 = self.find(parent, v)
        
            if v1 != v2:
                ArbolEM.agregarNodo(u)
                ArbolEM.agregarNodo(v)
                ArbolEM.agregarArista(u,v, e[1])
            
                if rank[v1] < rank[v2]:
                    parent[v2] = v2
                    rank[v1] += 1
                
                else:
                    parent[v2] = v1
                    rank[v1] += 1
                
        return ArbolEM
    
    
    def KrustalI(self):
    
        import numpy as np
    
        g = self.clone()
        #Ordenamos las aristas por sus pesos
        enlaces=[]
        for v in self.nodos:
            for j in self.nodos[v].vecinos:
                enlaces.append([(v,j[0]), j[1]])
            
        q = np.sort(enlaces, axis=0)[::-1]
        for e in q:
            # remove e  
            g.edges.pop(e[0])
            # clear weight
            for k in self.vertices:
                g.nodos[k].visitado == False 
            # valid if there is connected graph 
            if len(g.nodos) != len(g.bfs(0).nodos):
                g.agregarArista(e[1])
                
        return g
    
    
   
    
    
    def Prim(self):
        
        
        import sys
        
        g = grafo()
        distance = [sys.maxsize] * len(self.nodos)
        parent = [None] * len(self.nodos)
        set = [False] * len(self.nodos)

        distance[0] = 0
        parent[0] = -1

        for i in self.vertices:
            # Search vertex with minimum distance
            min_index = 0
            min = sys.maxsize
            for v in self.nodos:
                if distance[v] < min and set[v] is False:
                    min = distance[v]
                    min_index = v
            u = min_index

            # Add u vertex in set to not use it in other iteration 
            set[u] = True
            g.agregarNodo(u)

            # Iterate all adjacent vertices of u vertex and update distance 
            for v in self.nodos[i].vecinos:
                if set[v] is False and distance[v] > \
                        self.nodos[v[0]].distancia:
                    distance[v] = self.nodos[i].distancia + v[1]
                    parent[v] = u

        for i in self.nodos:
            if i == 0:
                continue
            if parent[i] is not None:
                g.agregarArista(parent[i], i, self.nodos[i].distancia)

        return g
        
    

