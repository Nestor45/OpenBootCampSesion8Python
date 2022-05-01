archivo = open('archivo.txt','a')
archivo.write("escribiendo una vez\n")

archivo = open('archivo.txt','r+')
archivo.write("escribiendo dos veces\n")

datos = archivo.readlines()
archivo.seek(0)
print(archivo.read())
archivo.close()

