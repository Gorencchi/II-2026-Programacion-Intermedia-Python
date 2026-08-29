import os
import pandas as pd
import matplotlib as mt

class Estudiante:
    def __init__(self, nombre, edad, estatura, horas_estudio, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.horas_estudio = horas_estudio
        self.calificacion = calificacion
        
    def mostrar_datos(self.):
        print(f"\n\tNombre: {self.nombre}\n\tEdad: {self.edad}\n\tEstatura: {self.estatura}\n\tHoras de estudio: {self.horas_estudio}\n\tCalificacion: {self.calificacion}")
        
        
    