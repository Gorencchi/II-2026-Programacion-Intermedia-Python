import pandas as pd
import matplotlib.pyplot as mt

df = pd.read_csv(r'Clase 04\estudiantes.csv')
print(df)
#Borrar filas con valores vacios :pp
df.fillna(0, inplace=True)

#reemplazar valores vacios por la media de la columna :pp
df.fillna({col: df[col].mean() for col in df.columns if df[col].isnull().any()}, inplace=True)

#valores erroneos, se corrige el formato de la columna de edad :pp
df.dropna(subset=["Edad"], inplace=True)

#Reemplazar valores erroneos :pp

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
