#!/usr/bin/python
#-*- coding: utf-8 -*-

class Usuario:
    def __init__(self,id,nom,ap,mail):
        self.id_usuario = id
        self.nombre = nom
        self.apellido = ap
        self.correo = mail

    def getNom(self):
        return self.nombre

    def getAp(self ):
        return self.apellido

    def getMail(self):
        return self.correo

    def getId(self ):
        return self.id_usuario

    def cerrarSesion(self ):
        exit()

