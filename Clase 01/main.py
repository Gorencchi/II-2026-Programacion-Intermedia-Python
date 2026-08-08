from Entidades.libro import Libro

class registro_libros():
    libro1= Libro("Rayuela", "Julio Cortazar",1963)
    libro2= Libro("La Metamorfosis", "Franz Kafka", 1915)
    libro3= Libro("Bestiario", "Julio Cortazar", 1951)
    libro4= Libro("Final del juego", "Julio Cortazar", 1956)
    catalogo = [libro1, libro2, libro3, libro4]
    print  ("\tCatalogo de Libros")
    for libro in catalogo:
           libro.mostrar_libro()