Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:24:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 

Alan Alejandro Herrera Huerta
#tarea 1 
print "ingresa un numero"
n = int(raw_input())
print "tu lista es: "
print range(1,n+1)
print "la suma de tu lista es: "
def sumas(n):
	suma=0
	for sumar in range(1,n+1):
		suma=suma+sumar
	return suma
print sumas(n)
