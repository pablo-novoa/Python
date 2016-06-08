from alumnos import *

lista = alumnosLista

print "\n\n"
print "==========================="
print "Listado de alumnos"
print "===========================\n"

for i in xrange(0,len(lista)):
	print "Alumno #" + str(i+1) + ": " + str( lista[i]['nombre'] ) + ", " + str( lista[i]['edad'] )

print "\n==========================="
print "\n\n"
