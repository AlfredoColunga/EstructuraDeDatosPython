import os
import pandas as pd
os.chdir(r"C:\Users\colun\Documents\Semestre 3")

# Crear archivo CSV
creacion = {0:[10.5],1:[20.5],2:[30.5]}
df = pd.DataFrame(creacion)
df.to_csv('resultado.csv',index=False, header=False, sep=';', decimal='.')

# Crear archivo Excel
from openpyxl import load_workbook
agrega = {0:['Pantalla'],1:['Samsung'],2:['G355']}
df2 = pd.DataFrame(agrega)
excel_dir = "pedidonuevo.xlsx"
writer = pd.ExcelWriter(excel_dir,engine='openpyxl') # pylint: disable=abstract-class-instantiated
df2.to_excel(writer,sheet_name='hoja2',header=False,index=False)
# EL archivo se crea hasta crear el .save
writer.save()
# EL archivo se cierra
writer.close()