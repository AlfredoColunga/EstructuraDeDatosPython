import os
# Funcion para obtener directorio actual
cwd = os.getcwd()
print (cwd)
# FUncion para hacer cambio de directorio
os.chdir("(Ingresar ruta del archivo con que le se va a trabajar)")

import pandas as pd
# Leer archivos csv
df = pd.read_csv('(nombre del archivo)')
print (df)

# Leer archivos excel
import pandas as pd
xls = pd.read_excel("(nombre de archivo excel)", sheet_name= "(nombre de hoja)")
# Si no se aclara el nombre de la hoja a imprimir, imprime la primera atomaticamente
print(xls)

#Leer archivos CSV y modificarlos
import pandas as pd
df = pd.read_csv('(nombre del archivo)')
# Agregar datos
agrega = {0:['Pantalla'],1:['Samsung'],2:['G530']}
df.to_csv(open('(nombre del archivo)',mode='a'),index=False,header=False,sep=',')

# Agregar hoja
import pandas as pd
import openpyxl
agrega1 = {0:['Pantalla'],1:['Samsung'],2:['G530']}
df5 = pd.DataFrame(agrega1)
excel_dir = "(nombre de archivo)"
writer = pd.ExcelWriter(excel_dir,engine='openpyxl') # pylint: disable=abstract-class-instantiated
book = openpyxl.load_workbook(excel_dir)
writer.book = book
df5.to__excel(writer,sheet_name='Hoja N')
writer.save()
writer.close()