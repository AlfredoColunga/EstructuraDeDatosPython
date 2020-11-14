import csv

with open('ejemploEscribir.csv', 'w', newline='') as File:
    writer = csv.writer(File)
    writer.writerow(["Numero", "Apellido", "Nombre"])
    writer.writerow([2, "Colunga", "Alfredo"])