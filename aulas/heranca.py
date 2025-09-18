class Pessoa:
    def __init__(self, nome:str, data_nascimento:str, cpf:int):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __str__(self):
        return f"nome = {self.nome}, data de nascimento = {self.data_nascimento}, cpf = {self.cpf}"
    
    def andar(self, passos):
        return f"{self.nome} deu {passos} passos"
    

class JogadorBasquete(Pessoa):
    def __init__(self, nome, data_nascimento, cpf, time, camisa):
       super().__init__(nome, data_nascimento, cpf)
       self.time = time
       self.camisa = camisa 

    def __str__(self):
        return f"{super().__str__()},time = {self.time}, camisa = {self.camisa}"
    
    def arremeco_bola(self) -> str:
        return f"o jogador {self.nome} arremecou a bola"
    
jogador10 = JogadorBasquete("Jason X", "24/05/1998", 89897456, "Lakers", 10)

print(jogador10)
print(jogador10.andar(10))
print(jogador10.arremeco_bola())