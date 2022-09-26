#!/usr/bin/python
#-*- coding: utf-8 -*-

from Producto import Producto

class Libro(Producto):
    def __init__(self,idLibro,nombreLibro,precio,editorial,nombreAutor):
        Producto.__init__(self,idLibro,nombreLibro,precio)
        self.editorial=editorial
        self.nombreAutor= nombreAutor

    def setEditorial(self, editorial):
        self.editorial=editorial

    def getEditorial(self):
        return self.editorial

    def setNombreAutor(self,nombreAutor ):
        self.nombreAutor= nombreAutor

    def getNombreAutor(self):
        return self.nombreAutor

    def leer(self, ):
        print("El libro se puede leer")
        
    def __toString__(self):
        return Producto.__toString__(self)+"idLibro:{} Nombre autor: {} editorial:{}".format(self.idLibro,self.nombreAutor,self.editorial)

#libro1= Libro("jose emilio","$3536.3",12,9,8)
#print(Libro.__bases__)