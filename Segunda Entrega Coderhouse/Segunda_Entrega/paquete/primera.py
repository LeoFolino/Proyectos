import json

try:
    with open(r"C:\Users\Leito-PC\Documents\Trabajos en Python\Proyecto\registro_de_users.json", "r") as file:
        usuarios = json.load(file)
except FileNotFoundError:
    usuarios = {}

# función de registro de usuarios
def signin():
    user = input("Ingrese el nombre de usuario: ")
    password = input ("Ingrese su contraseña: ")
    usuarios[user] = password
    with open(r"C:\Users\Leito-PC\Documents\Trabajos en Python\Proyecto\registro_de_users.json", "w") as file:
        json.dump(usuarios, file)
    print("Usuario generado correctamente!")
    print("")

# función de login
def login():
    user = input("Ingrese su nombre de usuario: ")
    password = input ("Ingrese su contraseña: ")

    if user in usuarios and usuarios[user] == password:
        print("Bienvenido al sistema!")
        print("")
    else:
        print("Usuario o contraseña incorrecto.")
        print("")

# función de vista de usuarios
def vista_users():
    if usuarios == 0:
        print("No se encontraron registros")
    else:
        print("Usuarios registrados:")
        for user, password in usuarios.items():
            print(f"Usuario: {user}, Contraseña: {password}")
        print("")

# cuerpo del programa (MENÚ)
while True:
    print("Bienvenido al programa")
    print("")
    print("(1) Registrar usuario")
    print("(2) Iniciar sesión")
    print("(3) Vista de usuarios")
    print("(4) Salir")
    print("")
# ingresa opción
    numero = input("Seleccione una opción: ")

# respuestas del programa ante el número ingresado
    if numero == "1":
        signin()

    elif numero == "2":
        login()
    
    elif numero == "3":
        vista_users()
    
    elif numero == "4":
        break
    
    else:
     print("Ingrese un número válido")
     print("")