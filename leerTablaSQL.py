import sqlite3
import pandas as pd
import os

# Ruta en donde se encuentra la base de datos
os.chdir(r"C:\Users\colun\Documents\Semestre 3")

con = sqlite3.connect('(nombre del archivo db')

tabla = pd.read_sql("select * from (tabla)",con)
print(tabla)

print(tabla)
print(tabla['(Nombre del campo)'])