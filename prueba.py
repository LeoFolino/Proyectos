import re

# Leer el contenido del archivo 'printer.log'
with open(r'C:\Users\Leito-PC\Documents\Trabajos en Python\LABURO\Proyecto Epsilon V2\printer-de-modelo.txt', 'r') as file:
    log_content = file.read()

# Definir un patrón regex para extraer la hora y los números de empresa
pattern = r'Hora: (\d{2}:\d{2}:\d{2})[\s\S]*?mpresa: (\d+)'

# Encontrar todas las coincidencias en el contenido del archivo
matches = re.findall(pattern, log_content)

# Iterar a través de las coincidencias y mostrar la hora y el número de empresa
for match in matches:
    hora = match[0]
    numero_empresa = match[1]
    print(f'Hora: {hora}, Número de Empresa: {numero_empresa}')
