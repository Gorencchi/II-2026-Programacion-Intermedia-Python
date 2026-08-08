import pandas as pd

a = [1,7,2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0])

b = [1,7,2]
myvar2 = pd.Series(b, index = ["x", "y", "z"])
print(myvar2)
print(myvar2["y"])

data = {
    "calorias": [420, 380, 390],
    "duracion": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["dia1", "dia2", "dia3"])
print(df)
print(df.loc["dia1"])

df2= pd.read_json(r'Clase 03/olaaa.json')
print(df2)


