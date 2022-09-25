#!/usr/bin/python
#-*- coding: utf-8 -*-

from Carrito import Carrito

class Producto:
    def __init__(self,id,precio,nom):
        self.id_prod = id
        self.precio = precio
        self.nombre = nom

    def getId(self ):
        return self.id_prod

    def getPrecio(self):
        return self.precio

    def getNombre(self ):
        return self.nombre

    def agregarcarrito(self,cant ):
        return Carrito(1,self.id_prod,cant,self.precio)
