# Se genera un error porque la variable "suma" no esta definida
try:
  print(suma)
except:
  print("Se ha ejecutado una excepción")

# Se genera un error a partir de un dato no valido
try:
  float("texto")
except NameError:
  print("La variable no esta definida")
except:
  print("Otro error ha ocurido")