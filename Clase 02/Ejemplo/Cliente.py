from Usuario import Usuario

class cliente(Usuario):
    def comprar(self, producto):
        print(f"{self.username} ha comprado {producto}.")
        