import csv

with open('ejemploLeer.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)