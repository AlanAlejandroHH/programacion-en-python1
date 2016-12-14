Alan Alejandro Herrera Huerta
#tarea 6

print "ingresa numero de años humanos"
A = float(raw_input())
def convierte(A):
	if 0 <= A <= 2:
		A = A*10.5
		return A
	if A > 2:
		x = (A-2)*4+2*10.5
		return A
A = convierte(A)
if A >= 0:
	print "el numero de años perro equivalente es: ",A,"años perro"
elif A < 0:
	print "ERROR!: no se admiten años negativos"
