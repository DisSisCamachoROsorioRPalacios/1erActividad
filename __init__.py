from Usuario import Usuario
from Comic import Comic
from Libro import Libro
from Carrito import Carrito

u=Usuario(0,"ali","camacho","a@a.com")
l1=Libro("minotauro",890,"lorem",0,5.98,"rueda del tiempo")
l2=Libro("minotauro",600,"lorem",1,6.70,"el mundo bajo el agua")
l3=Libro("minotauro",312,"lorem",2,3.30,"tiempo")
c1=Comic(100,"one piece","lorem",0,1.25,"el paraiso")
c2=Comic(100,"one piece","lorem",1,1.25,"nuevo mundo")
carro = []

print("bienvenido usuario")
print("estos son nuestros libros")
print("1.",l1.getNombre(), " precio:",l1.getPrecio()," Num. Paginas:",l1.getNum())
print("2.",l2.getNombre(), " precio:",l2.getPrecio()," Num. Paginas:",l2.getNum())
print("3.",l3.getNombre(), " precio:",l3.getPrecio()," Num. Paginas:",l3.getNum())
print("si le interesa alguno ingrese su numero de lo contrario un 0")
e=int(input())
if(e==1):
    print("cuantas cantidades")
    c=int(input())
    carro.append(l1.agregarcarrito(c))
elif(e==2):
    print("cuantas cantidades")
    c=int(input())
    carro.append(l2.agregarcarrito(c))
elif(e==3):
    print("cuantas cantidades")
    c=int(input())
    carro.append(l3.agregarcarrito(c))

print("estos son nuestros comics")
print("1.",c1.getNombre()," precio:",c1.getPrecio(), " serie:",c1.getNomS())
print("2.",c2.getNombre()," precio:",c2.getPrecio(), " serie:",c2.getNomS())
print("si le interesa alguno ingrese su numero de lo contrario un 0")
e=int(input())
if(e==1):
    print("cuantas cantidades")
    c=int(input())
    carro.append(c1.agregarcarrito(c))
elif(e==2):
    print("cuantas cantidades")
    c=int(input())
    carro.append(c2.agregarcarrito(c))
print("desea ver el carrito 1, 0 para salir")
e=int(input())
if(e==0):
    u.cerrarSesion
elif(e==1):
    for a in carro:
        print(a.mostrar())
        a.pagar()

