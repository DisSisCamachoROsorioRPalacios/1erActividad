#!/usr/bin/python
#-*- coding: utf-8 -*-

from Producto import Producto

class Comic(Producto):
    def __init__(self,idLibro,nombreLibro,precio,idComic,numeroComic,nombreAutor):
        
        Producto.__init__(self,idLibro,nombreLibro,precio)
        self.idComic = idComic
        self.numeroComic = numeroComic
        self.nombreAutor = nombreAutor
        

    def setNumComic(self, numeroComic):
        self.numeroComic=numeroComic

    def getNumComic(self):
        self.numeroComic

    def setNomAutor(self,nombreAutor ):
        self.nombreAutor=nombreAutor

    def getNomAutor(self):
        self.nombreAutor
    
    def coleccionar(self, ):
        print("El libro lo puede coleccionar")

    def __toString__(self):
        return Producto.__toString__(self) + "Id comic: {} Numero comic: {} nombre autor: {}".format(self.idComic,self.numeroComic,self.nombreAutor,)