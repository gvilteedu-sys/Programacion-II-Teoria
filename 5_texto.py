palabra="Mandarina"
print(len(palabra))

print(palabra.upper())
print(palabra.lower())
print(palabra.capitalize())
print(palabra.title())
print(palabra.replace("a","o"))
print(palabra.split("a"))
print(palabra[0])
print(palabra[1])

print(palabra[0:5]) #Manda
print(palabra[5:]) #inarina
print(palabra[:5]) #Mandarina
print(palabra[-1]) #a

Texto="Esta materia es Programacion II del instituto Tecnologico Mercantil"
Texto.lower()
estaInclida= "programacion" in Texto.lower()
print(estaInclida)


print(Texto.upper().replace("PROGRAMACION","Python"))

frase="                      ESTO TAMBIEN ES UN TEXTO                              "
print(frase)
print(frase.strip())
