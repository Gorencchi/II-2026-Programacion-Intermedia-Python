import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'Clase 04\estudiantes.csv')
print(df)
#Borrar filas con valores vacios :pp
df = df.dropna()
#Valores erroneos
for i in df.index:
    if not df.loc[i, "Edad"].isnumeric():
        df = df.drop(i)
    elif int(df.loc[i, "Edad"]) < 0 and int(df.loc[i, "Edad"]) > 120:
        df.drop(i)
print(df)

#borrar datos duplicados
new_df = df
for i in df.index:
    for j in df.index:
        if i != j:
            if (df.loc[i, "Nombre"] == df.loc[j, "Nombre"]
                and df.loc[i, "Edad"] == df.loc[j, "Edad"]
                and df.loc[i, "Calificacion"] == df.loc[j, "Calificacion"]
                and df.loc[i, "Estatura"] == df.loc[j, "Estatura"]
                and df.loc[i, "Peso"] == df.loc[j, "Peso"]
                and df.loc[i, "HorasEstudio"] == df.loc[j, "HorasEstudio"]
                ):
                    new_df = new_df.drop(j)

#reemplazar valores vacios por la media de la columna :pp
df.fillna({col: df[col].mean() for col in df.columns if df[col].isnull().any()}, inplace=True)
print(df)
#promedios
print(new_df[["Calificacion", "Peso", "HorasEstudio"]].mean())
#correlaciones
print(new_df[["Calificacion", "Peso", "HorasEstudio"]].corr())

#grafico
new_df = new_df.sort_values(by="Estatura", ascending=False)
new_df.plot(
    kind="line",
    x="Estatura",
    y="Peso"
)
plt.show()