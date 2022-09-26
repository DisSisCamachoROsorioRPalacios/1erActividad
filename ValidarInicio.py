#!/usr/bin/python
#-*- coding: utf-8 -*-

class ValidarInicio:
    def __init__(self):
        self.Permitido = None
        self.Negado = None

    def MensajePert(self, ):
        print('Inicio de secion correcto')

    def MensajeNega(self, ):
        print('Los datos ingresados no coinciden con ninguna cuenta.')

    def getPermitido(self, ):
        return self.Permitido

    def setPermitido(self, per):
        self.Permitido=per

    def getNegado(self, ):
        return self.Negado

    def setNegado(self, nper):
        self.Negado=nper
