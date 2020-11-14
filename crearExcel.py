import os
import pandas as pa
import numpy as np
from openpyxl import load_workbook
os.chdir(r"C:\Users\colun\Documents\Semestre 3")
path = "pedidonuevonp.xlsx"
writer = pa.ExcelWriter(path,engine='openpyxl') # pylint: disable=abstract-class-instantiated
x3 = np.random.randn(100,2)
df3 = pa.DataFrame(x3)
x4 = np.random.randn(200,2)
df4 = pa.DataFrame(x4)
df3.to_excel(writer,sheet_name='x3')
df4.to_excel(writer,sheet_name='x4')
writer.save()
writer.close()