class Carro:
    def __init__(self, dominio, marca):
        self.dominio = dominio
        self.marca = marca

carro1 = Carro("AA100", "volkswagen")
carro2 = Carro("AA200", "toyota")
carro3 = Carro("AA300", "Fiat")

lista_carros = [carro1, carro2]

'''
if "AA100" in lista_carros[0].dominio:
    print("Sirve")
else:
    print("no sirve putoooo")
'''

for i in lista_carros:
    if i.dominio == "AA200":
        print("Oh yeah")
        break
    