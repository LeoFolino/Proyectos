class Cliente:
    def __init__(self, nombre, apellido, edad, email, intereses):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email
        self.intereses = intereses

    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido}'
    
    def comprar(self, producto):
        return f"El cliente {self.nombre} {self.apellido} realizo la compra de {producto}"
    
    def ver_intereses(self):
        print(f'Intereses de {self.nombre} {self.apellido}: {", ".join(self.intereses)}')