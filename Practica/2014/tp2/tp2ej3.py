"""

3.- Modifique el ejercicio 11.- c) de la Práctica 1 para que se lean los alumnos y las notas de teclado,
informándolas hasta que se encuentre el número -1, y al finalizar deberá imprimir "Fin de la carga de notas".

11c) Dados el nombre de un alumno y su promedio, investigue cómo realizar la impresión de los datos en pantalla sin tener que 
convertir el valor numérico a string. Es decir, sin imprimirlo de la forma:
print (nombreAlumno   +   str (promedio ) ) ni print ( nombre Alumno , promedio )
"Name: %s, age: %d" % ('John', 35) 
'Name: John, age: 35' 


nombreAlumno=raw_input('ingrese el nombre del Alumno y presione enter')
promedio=input('ingrese el promedio del alumno')
print "%s, %f" % (nombreAlumno,promedio)

"""

promedio = float(input('ingrese el promedio del alumno'))

while promedio != -1:
    nombreAlumno = input('ingrese el nombre del Alumno y presione enter')
    print("%s, %f" % (nombreAlumno, promedio))
    promedio = float(input('ingrese el promedio del alumno'))
print('Fin de carga de notas')
