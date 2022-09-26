#!/usr/bin/python
#-*- coding: utf-8 -*-

class Login:
    def __init__(self):
        self.nomuser = None
        self.contras = None

    def ObtenerUsuario(self):
        usuario = input("Por favor ingrese su usuario: ")
        self.setUsuario(usuario)

    def ObtenerContra(self):
        contra = input("Por favor ingrese su contraseña: ")
        self.setContra(contra)

    def getUsuario(self, ):
        return self.nomuser

    def setUsuario(self, nomu):
        self.nomuser=nomu

    def getContra(self, ):
        return self.contras

    def setContra(self, contra):
        self.contras=contra
