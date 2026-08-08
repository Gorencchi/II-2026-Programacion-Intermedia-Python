class Libro():
    def __init__(self, titulo, autor, anno_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anno_publicacion = anno_publicacion
        
    def mostrar_libro(self):
        print(f"Titulo:{self.titulo}, Autor: {self.autor}, Año de publicación: {self.anno_publicacion}")