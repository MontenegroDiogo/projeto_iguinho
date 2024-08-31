class Caneta:
    def __init__(self, cor, ponta, carga, tampa):
        self.cor = cor
        self.ponta = ponta
        self.carga = carga
        self.tampa = tampa
        
    def tampar(self):
        if self.tampa == "não" and self.carga > 0:
            print("A caneta esta rabiscando")
        elif self.tampa == "sim":
            print("A caneta esta tampada, não pode rabiscar")
        else:
            print("Esta sem carga")
    
    def mostrar_info(self):
        print(f'Informações, a caneta é {self.cor}, de ponta {self.ponta}, esta com a carga {self.carga}')

minha_caneta = Caneta("azul", '0.5', 80, 'sim')
minha_caneta.tampar()
minha_caneta.mostrar_info()


