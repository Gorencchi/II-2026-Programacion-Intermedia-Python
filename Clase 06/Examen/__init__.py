import pandas as pd
import matplotlib.pyplot as mt

class Pelicula:
    def __init__(self, titulo, genero, duracion, presupuesto, calificacion):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        self.presupuesto = presupuesto
        self.calificacion = calificacion

    def mostrar_datos(self):
        print(f"\n\tTítulo: {self.titulo}")
        print(f"\n\tGénero: {self.genero}")
        print(f"\n\tDuración: {self.duracion} minutos")
        print(f"\n\tPresupuesto: ${self.presupuesto}")
        print(f"\n\tCalificación: {self.calificacion}/10")

peliculas = [
    Pelicula("My Bloody Valentine", "Ciencia ficción/Slasher", 148, 16000, 9),
    Pelicula("El resplandor", "Terror", 130, 18000, 9),
    Pelicula("Paprika", "Animacion", 169, 100000, 8.6),
    Pelicula("Lalaland", "Terror(Mia y Sebastian tenian que haber quedado juntos)", 136, 63000000, 8.7),
    Pelicula("Pulp Fiction", "Crimen", 154, 8000000, 8.9),
    Pelicula("Dracula", "Terror", 120, 50000, 10)
]
print("\n\tInformacion de peliculas")
print("\n\t----------------------")
for pelicula in peliculas:
    pelicula.mostrar_datos()

datos = []
for pelicula in peliculas:
    datos.append(pelicula.__dict__)
df = pd.DataFrame(datos)
print("\n\t-----------------------------------")
print("\n\tInformacion de peliculas en DataFrame")
print("\n\t-----------------------------------")
print(df)
print("\n\t-----------------------------------")
print("\n\tPelicula con mayor duracion")
print("\n\t-----------------------------------")
pelicula_mayor_duracion = df.loc[df['duracion'].idxmax()]
print(pelicula_mayor_duracion)
print("\n\t-----------------------------------")
print("\n\tPelicula con menor duracion")
print("\n\t-----------------------------------")
pelicula_menor_duracion = df.loc[df['duracion'].idxmin()]
print(pelicula_menor_duracion)

print("\n\t-----------------------------------")
print("\n\tCorrelacion entre presupuesto y calificacion")
print("\n\t-----------------------------------")
cor = df['presupuesto'].corr(df['calificacion'])
print(f"\n\tCorrelacion: {cor}")

print("\n\t-----------------------------------")
print("\n\tCorrelacion entre duracion y calificacion")
print("\n\t-----------------------------------")
dyc = df['duracion'].corr(df['calificacion'])
print(f"\n\tCorrelacion: {dyc}")

mt.scatter(df['presupuesto'], df['calificacion'])
mt.xlabel("Presupuesto")
mt.ylabel("Calificación")
mt.show()