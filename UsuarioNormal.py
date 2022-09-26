#!/usr/bin/python
#-*- coding: utf-8 -*-

from Usuario import Usuario

class UsuarioNormal(Usuario):
    def __init__(self):
        pass

    def BuscarLibr(self, noml):
        print('Libro buscado')

    def AgregarLibrCar(self, noml):
        print('Libro agregado')

    def EliminarProdCar(self, noml):
        print('Libro eliminado')
