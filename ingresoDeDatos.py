# puedo formatear un saldo de linea con ej ual es tu nombre: \r\n
nombre = input('cual es tu nombre:')
print(f'Hola {nombre}')

edad = input('cual es tu edad:')
#el input es string asi que convierto
edad = int(edad)

if edad >= 17:
    print('puedes votar')
else:
    print('aun no puedes votar')

#un nuevo operador, el modulo que me da el resto de la division
if edad % 2 == 0:
    print('la edad es par')
else:
    print('La edad es impar')