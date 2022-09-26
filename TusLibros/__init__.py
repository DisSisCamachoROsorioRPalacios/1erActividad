import Usuario
import Comic
import Libro
import Revista
import Producto
if __name__ == "__main__":
    
    usuario1 = Usuario.Usuario(1,"Monserrath","monsero10@gmail.com","1234")
    
    libro1= Libro.Libro("p1","Las batallas en el desierto",3536.3,"p1","jose emilio")
    libro2= Libro.Libro("p4","La batalla de Tenochtitlán",149.00,"p2","pedro s.")
    revista1=Revista.Revista("p2","National Geographic",450.99,"r1","Ciencia",111)
    comic1=Comic.Comic("p3","Fullmetal",50.20,"c2",53,"Alfred")
    
    #p= Producto.Producto()
    
    libros = []
    libros.append(libro1.__toString__())
    libros.append(revista1.__toString__())
    libros.append(comic1.__toString__())
    libros.append(libro2.__toString__())
    #print("LIBROS: ",libros)
    #print(usuario1.__toString__())
    #print(libro1.__toString__())
    #print(revista1.__toString__())
    #print(comic1.__toString__())
    
    print("====== T U S   L I B R O S=========")
    print("Bienvenid@ usuario: ", usuario1.getNombre())
    buscar=input("\nIngrese búsqueda: ")
    
    Producto.Producto.buscar(libros,buscar)
    