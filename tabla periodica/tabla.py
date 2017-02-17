#Alan Alejandro Herrera Huerta
#Tabla

import csv
tp=open('tablaperiodica.csv')
lns=csv.reader(tp,delimiter=';')
for line in lns:
    no_atom=line[0]
print no_atom
