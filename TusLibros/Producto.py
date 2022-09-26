#!/usr/bin/python
#-*- coding: utf-8 -*-

#import Comic
#import Revista
#import Libro

class Producto(object):
    def __init__(self,idLibro,nombreLibro,precio):
        self.idLibro = idLibro
        self.nombreLibro = nombreLibro
        self.precio = precio
    

    @classmethod
    def buscar(self,libros,busca ):
        
        str_libro = [s for s in libros if busca in s]
        print("Mejor coincidencia \n",str_libro)
        
        
        

    def setNombreLibro(self,nombreLibro):
        self.nombreLibro= nombreLibro

    def getNombreLibro(self,):
        self.nombreLibro

    def setPrecio(self,precio ):
        self.precio=precio

    def getPrecio(self,):
        self.precio

    def __toString__(self):
        return "idLibro:{} Nombre libro: {} precio:{}".format(self.idLibro,self.nombreLibro,self.precio)

    def pedirDatos(self,idLibro,nombreLibro,precio ):
        pass

