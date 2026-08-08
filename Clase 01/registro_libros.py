from Entidades import Libro as lb

class Libro():
    def __init__(self, titulo, autor, anno_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anno_publicacion = anno_publicacion

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.anno_publicacion})"

class RegistroLibros:
    def __init__(self):
        self.libro= []
    def agregar_libro(self, libro):
        self.libro.append(libro)
    def mostrar_libros(self):
        for libro in self.libro:
            print(libro)
