#!/usr/bin/python
#-*- coding: utf-8 -*-

from Producto import Producto

class Revista(Producto):
   def __init__(self,idLibro,nombreLibro,precio,idRevista,categoria,numSerie):
        Producto.__init__(self,idLibro,nombreLibro,precio)
        self.idRevista=idRevista
        self.categoria= categoria
        self.numSerie=numSerie

   def setCategoria(self,categoria ):
        self.categoria= categoria

   def getCategoria(self):
        return self.categoria

   def setNumSerie(self,numSerie ):
        self.numSerie=numSerie

   def getNumSerie(self):
        return self.numSerie

   def suscribir(self, ):
        print("Puede suscribirse")
        
   def __toString__(self):
        return Producto.__toString__(self) + "Id revista: {} Categoria: {} nunero de serie: {}".format(self.idRevista,self.categoria,self.numSerie)

