#!/usr/bin/python
#-*- coding: utf-8 -*-

from Producto import Producto

class Libro(Producto):
    def __init__(self,edit, num_p,desc,id,precio,nom):
        self.editorial = edit
        self.num_pag = num_p
        self.descripcion = desc
        Producto.__init__(self,id,precio,nom)

    def getEdit(self ):
        return self.editorial

    def getNum(self ):
        return self.num_pag

    def getDesc(self ):
        return self.descripcion

    def ordenar(self ):
        print("ordenando....")

