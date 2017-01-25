#Alan Alejandro Herrera Huerta
#trabajo 4

def leertxs(s,n)
    archivo=open(s"autos")
    for linea in range(1,(n+1)):
      lineas=archivo.readline()
      print lineas
