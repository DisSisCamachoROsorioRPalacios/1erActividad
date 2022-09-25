#!/usr/bin/python
#-*- coding: utf-8 -*-

class Carrito:
    def __init__(self,id,id_pro,cant,precio):
        self.id_carrito = id
        self.id_prod = id_pro
        self.cantidad = cant
        self.total = cant*precio

    def mostrar(self ):
        print("id: ",self.id_prod," \ncantidad: " ,self.cantidad," \ntotal:", self.total)

    def actualizar(self ):
        print("que decea actualizar 1-id_prod, 2-cantidad")
        a=input()
        if(a==1):
            print("ingrese el nuevo id")
            self.id_prod=input()
        elif(a==2):
            print("nueva cantidad")
            self.cantidad=input()

    def pagar(self ):
        print("Pagar....")

    def cancelar(self ):
        exit()

