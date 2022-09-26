#!/usr/bin/python
#-*- coding: utf-8 -*-

from Usuario import Usuario

class UsuarioAdministracion(Usuario):
    def __init__(self):
        pass

    def AgregarLib(self, noml):
        print('Libro agregado')

    def ModificarInfLib(self, id, noml):
        print('Libro modificado')

    def EliminarLib(self, id, noml):
        print('Libro eliminado')
