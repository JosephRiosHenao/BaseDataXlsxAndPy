import pandas as pd

rutaDeLaBase = "Alquileres.xlsx"
hojaDeLaBase = "Data"

df = pd.read_excel(rutaDeLaBase, hojaDeLaBase)
df