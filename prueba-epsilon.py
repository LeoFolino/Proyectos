import pandas as pd
import re

# Leer el contenido del txt
with open(r'C:\Users\Leito-PC\Documents\Trabajos en Python\LABURO\Proyecto Epsilon V2\printer-de-modelo.txt', 'r', encoding='utf-8') as file:
    log_content = file.read()

# Crear un DataFrame a partir de OperacionesR3.csv
df_csv = pd.read_csv(r'C:\Users\Leito-PC\Documents\Trabajos en Python\LABURO\Proyecto Epsilon V2\OperacionesR3.csv', delimiter=';')

# Crear listas para almacenar la hora y el código de empresa del archivo printer.log
horas_log = []
empresas_log = []

# Dividir el archivo printer.log en operaciones
operaciones = log_content.split('Maquina:')      # Hay que modificarlo ----> ya que en el recuento final originalmente (No se añadio en printer-de-modelo.txt) muestra el cierre
                                                 # total de caja en el cual se repite "Maquina" y generaria una operacion mas que no corresponde . REVISAR LEO---

# Expresiones para extraer la hora y el código de empresa
hora_pattern = r'Hora: (\d+:\d+:\d+)'
empresa_pattern = r'mpresa: (\d+)'

# Extraer la hora y el código de empresa de cada operación
for operacion in operaciones:
    hora_match = re.search(hora_pattern, operacion)
    empresa_match = re.search(empresa_pattern, operacion)
    
    if hora_match and empresa_match:
        horas_log.append(hora_match.group(1))
        empresas_log.append(empresa_match.group(1))

# Comparar los datos del archivo CSV con los del archivo de texto
diferencias = []

for indice, fila in df_csv.iterrows():
    hora_csv = fila['Hora']
    empresa_csv = fila['Codigo_de_Empresa']

    if (hora_csv not in horas_log) or (str(empresa_csv) not in empresas_log):
        diferencias.append((hora_csv, str(empresa_csv)))

# Imprimir las diferencias
if diferencias:
    print("Operaciones faltantes o con diferencias:")
    for diferencia in diferencias:
        print(f'Hora: {diferencia[0]}, Código de Empresa: {diferencia[1]}')
else:
    print("No se encontraron diferencias entre los archivos.")



###     EL DEFECTO ES QUE VALIDA A PARTIR DEL .CSV LO QUE FALTA EN EL .TXT, Y NO EN AMBOS SENTIDOS // A FUTURO HAY QUE EXCLUIR EL CIERRE DEFINITIVO Y LOS CIERRES DE CAJA.
###     LO ESTA VALIDANDO POR HORARIO, LO QUE SIGNIFICA QUE SI METO MANO PARA MODIFICAR EN LA OPERACION DONDE EL HORARIO COINCIDE, EL CODIGO DE EMPRESA, VA A SEGUIR SIN DETECTAR DIFERENCIAS.
###     HAY QUE SEGUIR TRABAJANDO