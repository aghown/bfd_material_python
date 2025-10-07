class Mamifero:
    def __init__(self, idade, habitat):
        self.idade = idade
        self.habitat = habitat
        self.prole = "gestação"
        self.alimentacao_infantil = "leite"

    def som(self):
        return "Nenhum som definido"

class Morcego(Mamifero):
    def som(self):
        return "Assobia"
    

class Gato(Mamifero):
    def som(self):
        return "Miauuuuu"
    #def __init__(self, locomocao="vôo"):
        #super().__init__(idade, habitat, som)
    #    self.locomocao = locomocao
        

zubat = Morcego(1,"laje")
gatinho = Gato(4,"sala")

print(gatinho.som())

print(zubat.idade)
print(zubat.habitat)
print(zubat.som())
#print(zubat.locomocao)
#print(zubat.prole)
#print(zubat.alimentacao_infantil)

#print(zubat.locomocao)