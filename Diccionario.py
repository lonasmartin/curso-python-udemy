#Un diccionario es parecido a los SDT en genexus
cancion = {
    'artista' :'metalica',
    'cancion': 'Enter sandman',
    'lanzamiento' : 1992,
    'likes': 3000
}

print(cancion)

#si  quiero acceder a un elemento
print(cancion['cancion'])

print(f'estoy escuchando {cancion["artista"]}')

#agregar nuevos valores
cancion['playlist'] = 'Heavy metal'
print(cancion)

#Eliminar uno de los elementos
del cancion['lanzamiento']
print(cancion)


