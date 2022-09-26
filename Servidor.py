#!/usr/bin/python
#-*- coding: utf-8 -*-
from ValidarInicio import ValidarInicio
from Usuario import Usuario
from UsuarioAdministracion import UsuarioAdministracion
from UsuarioNormal import UsuarioNormal
class Servidor:
    def __init__(self):
        pass

    def VerificarDatos(self, user, contra):
        usuario=Usuario()
        f = open("Users&pass.txt",'r')
        per=False
        nper=True
        for linea in f:
            g=linea
            u=g.split(',')
            if user==u[0]:
                if contra==u[1]:
                    per=True
                    usuario.setId(u[2])
                    usuario.setNombre(u[3])
                    usuario.setApellido(u[4])
                    break;
        f.close()
        print(per)
        if per:
            self.PermitirInicio(per,usuario)
        else:
            self.NegarInicio(nper)

    def PermitirInicio(self, per, user):
        val=ValidarInicio()
        val.setPermitido(per)
        val.MensajePert()

        if 'A' in user.getId():
            print('Tipo de usuario: Administrador')
            userad=UsuarioAdministracion()
            userad.AgregarLib('hola')
            userad.ModificarInfLib('123','hola')
            userad.EliminarLib('123','hola')
            userad.BuscarLib('hola')
            userad.AgregarLibCar('hola')
            print('Nombre: ',user.getNombre())
            print('Apellido: ',user.getApellido())

        if 'N' in user.getId():
            print('Tipo de usuario: Normal')
            usernor=UsuarioNormal()
            usernor.BuscarLib('hola')
            usernor.AgregarLibCar('hola')
            usernor.EliminarProdCar('hola')
            usernor.BuscarLibr('hola')
            usernor.AgregarLibrCar('hola')
            print('Nombre: ',user.getNombre())
            print('Apellido: ',user.getApellido())

    def NegarInicio(self, nper):
        val=ValidarInicio()
        val.setPermitido(nper)
        val.MensajeNega()
