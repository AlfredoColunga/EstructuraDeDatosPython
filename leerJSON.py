import json

with open('archivo_json_Ev3.json') as file:
    data = json.load(file)
for x in data:
    print(x)

#---Resultado
# userId
# id
# title
# completed