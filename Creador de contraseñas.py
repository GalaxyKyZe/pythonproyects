import time
import random

print("Este es un programa que genera contraseñas")
time.sleep(1.5)

contra1 = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" ## Caracteres a usar
contra2 = int(input("¿Con cuantas letras deseas que tenga tu contraseña?: "))
password = ""; ## Aquí irá la contraseña una vez termine de generarse

for i in range(contra2):
    password += random.choice(contra1)
print("Generando contraseña...")
time.sleep(3)
print("Tu contraseña es:", password)