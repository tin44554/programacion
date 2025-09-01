from typing import Self
def __int__(self, nombre, raza):
    self.nombre = nombre 
    self.raza = raza 

def ladrar(self):
    return "¡Guau! ¡Guau!"
def datos_del_perro(self):
    
    return f"{self.nombre} es de raza {self.raza}"
mi_perro = Perro("Rex", "Pastor Alemán")
tu_perro = Perro("Luna", "Labrador")


print(mi_perro.nombre) 
print(tu_perro.ladrar()) 
print(mi_perro.datos_del_perro()) 
