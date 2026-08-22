import pandas as pd 
import matplotlib as mt
class DataFrame:
    def __init__(self, nombre, edad, estatura, peso, HorasEstudio, Calificacion):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.peso = peso
        self.HorasEstudio = HorasEstudio
        self.Calificacion = Calificacion
personas = [
    DataFrame("Juan", 20, 1.75, 70, 5, 85),
    DataFrame("Maria", 22, 1.65, 60, 8, 90),
    DataFrame("Pedro", 19, 1.80, 75, 3, 70),                            
    DataFrame("Ana", 21, 1.70, 65, 6, 95),
    DataFrame("Luis", 23, 1.85, 80, 4, 80),
    DataFrame("Sofia", 20, 1.60, 55, 7, 88)
]
datos = []
for persona in personas:
    datos.append(persona.__dict__)
df = pd.DataFrame(datos)

df = pd.read_csv("datos.csv")
df.plot(kind='scatter', x='HorasEstudio', y='Calificacion', color='blue')
mt.show()
    

