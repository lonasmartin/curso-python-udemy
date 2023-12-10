#Como inicializar un diccionario
jugador = {}

#aqui agrego un jugador metiendo cada una de las popiedades por separad0
jugador['nombre'] = 'Martin'
jugador['puntaje'] = 0
print(jugador)

#aumento el puntaje a 100
jugador['puntaje'] = jugador['puntaje'] + 100
print(jugador)

#aumento otra vez
jugador['puntaje'] = jugador['puntaje'] + 100
print(jugador)

#ahora itero sobre la estructura  
# super interesante es que puede meter 2 variables en el for  
for llave, valor in jugador.items():
    print(llave)
    print(valor)

#funciona lo que hace es recorrer uno por uno primero nombre
# del campo y luego su valor
for llave in jugador.items():
    print(llave)

#si quiero acceder al elemento consola (que no existe)
print(jugador.get('consola', 'no existe valor'))

#si quiero acceder al elemento nombre
print(jugador.get('nombre', 'no existe valor'))

#si hago esto, piso todos los valores y los reemplazo por estos
jugador['nombre'] = 'Ines'
jugador['puntaje'] = 30
print(jugador)