from paquete.clientes import Cliente

cliente1 = Cliente('Leonel', 'Folino', 25, 'rafaga@gmail.com', ['Astronomia', 'Cocina'])

print(cliente1.comprar('Telescopio'))
print(cliente1)
cliente1.ver_intereses()