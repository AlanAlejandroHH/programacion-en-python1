Alan Alejandro Herrera Huerta
#tarea 1

import math
print "latitud 1 en grados:"
A1 = float(raw_input())
print "longitud 1 en grados"
A2 = float(raw_input())
print "latitud 2 en grados"
P1 = float(raw_input())
print "longitud 2 en grados"
P2 = float(raw_input())
#conversiones
a = (A1*math.pi)/180
b = (A2*math.pi)/180
c = (P1*math.pi)/180
d = (P2*math.pi)/180

distancia = 6371.01*math.acos(math.sin(a)*math.sin(c)
	    +math.cos(a)*math.cos(c)*math.cos(b-d))
print "la distancia en km es: ", distancia
