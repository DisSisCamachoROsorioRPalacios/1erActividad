#!/usr/bin/python
#-*- coding: utf-8 -*-

class Usuario:
    def __init__(self):
        self.nombre = None
        self.apellidoPat = None
        self.Id = None

    def BuscarLib(self, noml):
        print('Libro buscado')

    def AgregarLibCar(self, noml):
        print('Libro agregado')

    def getNombre(self, ):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre=nombre

    def getApellido(self, ):
        return self.apellidoPat

    def setApellido(self, apPat):
        self.apellidoPat=apPat

    def setId(self, id):
        self.ID=id

    def getId(self):
        return self.ID
