import sys
import serial
import time

# Configura o serial do Arduino
arduino = serial.Serial("COM4", 9600)
time.sleep(2)  # Espera o Arduino resetar

while True:
    # Lê as posições desejadas
    print("Digite os ângulos (0-180) ou S para sair")
    try:
        garra = int(input("Garra: "))
        rot = int(input("Rotação: "))
        ataque = int(input("Ataque: "))
        altura = int(input("Altura: "))
    except:
        arduino.close()
        sys.exit(0)

    pacote = bytes([garra, rot, ataque, altura])
    arduino.write(bytes(pacote))
