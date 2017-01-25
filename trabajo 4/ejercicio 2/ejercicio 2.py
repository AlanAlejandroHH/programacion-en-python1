#Alan Alejando Herrera Huerta
#tarea 2


def concatenar(n,m)
  nuevo=open(m,"b")
  for i in n:
    c=open(i,"s")
    for linea in c:
      nuevo.write(linea+"/n")
