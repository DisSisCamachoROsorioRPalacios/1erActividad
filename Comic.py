#!/usr/bin/python
#-*- coding: utf-8 -*-

from Producto import Producto

class Comic(Producto):
    def __init__(self,n_tomo,nom_ser,desc,id,precio,nom):
        self.num_tomo = n_tomo
        self.nombre_serie = nom_ser
        self.descripcion = desc
        Producto.__init__(self,id,precio,nom)
    def getNumT(self):
        return self.num_tomo

    def getNomS(self ):
        return self.nombre_serie

    def getDesc(self ):
        return self.descripcion

    def ordenar(self ):
        print("ordenando....")

