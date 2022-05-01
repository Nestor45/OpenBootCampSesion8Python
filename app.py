import pickle

class Vehiculo:
    color = ''
    marca = ''
    llantas = 4
    def __init__(self, color, marca, llantas):
        self.color = color
        self.marca = marca
        self.llantas = llantas
    
    def getColor(self):
        return self.color

v1 = Vehiculo("rojo",'bmw',4)
# f = open('datos.bin','wb')
# pickle.dump(v1, f)
f = open('datos.bin','rb')
coche = pickle.load(f)
f.close()
print("color:",coche.getColor(),"\nllantas: ",coche.llantas)