import pandas as pd
import re

# Leer el contenido del txt
with open('printer-de-modelo.txt', 'r', encoding='utf-8') as file: 
    log_content = file.read()                                     

# Crear un DataFrame a partir de OperacionesR3.csv
df_csv = pd.read_csv('OperacionesR3.csv', delimiter=';')          

# Crear listas para almacenar la hora y el código de empresa del archivo printer.log
horas_log = []                                                   
empresas_log = []                                               

# Dividir el archivo printer.log en operaciones
operaciones = log_content.split('Maquina:')                        
                                                                   
# Expresiones para extraer la hora y el código de empresa                  /// HAY QUE SACAR EL CIERRE DEFINITIVO 
hora_patron = r'Hora: (\d+:\d+:\d+)'                               
empresa_patron = r'mpresa: (\d+)'                                

# Extraer la hora y el código de empresa de cada operación
for operacion in operaciones:                                      
    hora_match = re.search(hora_patron, operacion)                 
    empresa_match = re.search(empresa_patron, operacion)         

    if hora_match and empresa_match:                              
        horas_log.append(hora_match.group(1))                       
        empresas_log.append(empresa_match.group(1))

# Comparar los datos del archivo csv contra el txt
diferencias_csv_a_txt = []                                     
diferencias_txt_a_csv = []

for indice, fila in df_csv.iterrows():                            
    hora_csv = fila['Hora']                                   
    empresa_csv = str(fila['Codigo_de_Empresa'])
                                                                            
    if (hora_csv not in horas_log) or (empresa_csv not in empresas_log):   
        diferencias_csv_a_txt.append((hora_csv, empresa_csv))             

# Comparar los datos del txt contra el csv                                                                          
for hora_log, empresa_log in zip(horas_log, empresas_log):
    if (hora_log not in df_csv['Hora'].values) or (empresa_log not in df_csv['Codigo_de_Empresa'].astype(str).values):    
        diferencias_txt_a_csv.append((hora_log, empresa_log))   

# Imprimir las diferencias
if diferencias_csv_a_txt:
    print("Operaciones faltantes en el archivo de texto (CSV a TXT):")
    for diferencia in diferencias_csv_a_txt:
        print(f'Hora: {diferencia[0]}, Código de Empresa: {diferencia[1]}')

if diferencias_txt_a_csv:
    print("Operaciones faltantes en el archivo CSV (TXT a CSV):")
    for diferencia in diferencias_txt_a_csv:
        print(f'Hora: {diferencia[0]}, Código de Empresa: {diferencia[1]}')

if not diferencias_csv_a_txt and not diferencias_txt_a_csv:
    print("No se encontraron diferencias entre los archivos.")

#   --------AÑADIR QUE VALIDE SECUENCIAS DUPLICADAS POR NUMERO DE OPERACION EN UNA BASE DE DATOS UNIFICADA CON LOS REPORTES DE SECUENCIAS DUPLICADAS------