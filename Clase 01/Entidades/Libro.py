class Libro():
    def __init__(self, titulo, autor, anno_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anno_publicacion = anno_publicacion
        
    
    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.anno_publicacion})"