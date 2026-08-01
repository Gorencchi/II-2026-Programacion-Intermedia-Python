from Usuario import Usuario

class Cliente(Usuario):
    def comprar(self, producto):
        print(f"{self.username} ha comprado {producto}.")
        
        