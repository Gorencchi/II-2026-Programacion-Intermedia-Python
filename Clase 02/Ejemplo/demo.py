from Usuario import Usuario
from Cliente import Cliente
from administrador import administrador

cliente = Cliente(" juan123", "password123", "juan@example.com", "Calle Falsa 123", "Perez", 30, "Juan")
print(cliente)
admin = administrador("admin", "adminpass", "admin@example.com")
print(admin)

admin.agregar_usuario(cliente)

cliente.comprar("Laptop")