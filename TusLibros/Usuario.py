#!/usr/bin/python
#-*- coding: utf-8 -*-

class Usuario():
    def __init__(self,idUsuario,nombre,correo,contrasenia):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.correo = correo
        self.contrasenia = contrasenia

    def buscarLibro(self, ):
        pass

    def setNombre(self,nombre):
        self.nombre= nombre
        

    def getNombre(self ):
        return self.nombre

    def setContrasenia(self,contrasenia):
        self.contrasenia=contrasenia

    def getContrasenia(self):
        return self.ontrasenia
    
    def __toString__(self):
        return "Id usuario: {} nombre: {} correo: {} contraseña:{}".format(self.idUsuario,self.nombre,self.correo,self.contrasenia)



#usuario1= Usuario(1,"Monserrath","monsero10@gmail.com","1234")
#print(usuario1.__toString__())