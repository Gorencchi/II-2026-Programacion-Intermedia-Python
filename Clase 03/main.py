import pandas as pd

df = pd.read_csv(r'Clase 03\estudiantes.csv')
print(df.head(10))
#maximo
print("Edad maxima: ", df['edad'].max())
#minimo
print("Edad minima: ", df['edad'].min())
#estatura max
print("Estatura maxima: ", df['estatura'].max())
#estatura min
print("Estatura minima: ", df['estatura'].min())


    