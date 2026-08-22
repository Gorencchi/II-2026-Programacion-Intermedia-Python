import pandas as pd
import matplotlib.pyplot as mt

df = pd.read_csv(r'Clase 04\estudiantes.csv')
print(df)
#Borrar filas con valores vacios :pp
df.fillna(0, inplace=True)

#valores erroneos, se corrige el formato de la columna de edad :pp
df.dropna(subset=["Edad"], inplace=True)

#Reemplazar valores erroneos de edad mayores a 100 por 100 y menores a 0 por 0 :pp
df.loc[df["Edad"] > 100, "Edad"] = 100
df.loc[df["Edad"] < 0, "Edad"] = 0
#correlaciones
df.corr()
print("Correlacion entre edad y calificacion:", df["Edad"].corr(df["Calificacion"]))
#promedios
x = df["Edad"].mean()
print("El promedio de edad es:", x)
y = df["Calificacion"].mean()
print("El promedio de calificacion es:", y)
u = df["Edad"].mean()
print("El promedio de edad es:", u)
