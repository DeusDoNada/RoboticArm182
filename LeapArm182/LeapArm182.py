import leap
import serial
import time


# Posições de calibração dos servos
GARRA_ABERTA = 65
GARRA_FECHADA = 110
ROT_ESQ = 180
ROT_DIR = 0
ATAQUE_AVANCO = 140
ATAQUE_RECUO = 60
ALTURA_CIMA = 140
ALTURA_BAIXO = 80

# Configura o serial do Arduino
arduino = serial.Serial("COM4", 9600)
time.sleep(2)  # Espera o Arduino resetar


# Limita extensão dos movimentos
def clamp(value, min_val=0.0, max_val=1.0):
    return max(min_val, min(max_val, value))


class MyListener(leap.Listener):
    def on_connection_event(self, event):
        print("Leap Motion Controller connectado!")

    def on_device_event(self, event):
        try:
            with event.device.open():
                info = event.device.get_info()
        except leap.LeapCannotOpenDeviceError:
            info = event.device.get_info()

        print(f"Dispositivo encontrado: {info.serial}")

    def on_tracking_event(self, event):
        if len(event.hands):
            hand = event.hands[0]  # Primeira mão da lista (esquerda ou direita)

            palma_da_mao = clamp(hand.grab_strength)  # 0=aberta, 1=fechado
            garra = int(GARRA_ABERTA + palma_da_mao * (GARRA_FECHADA - GARRA_ABERTA))

            x_norm = clamp((hand.palm.position.x + 250.0) / 500.0)  # -250 a 250
            rotacao = int(ROT_ESQ - x_norm * (ROT_ESQ - ROT_DIR))
            
            z_norm = 1.0 - clamp((hand.palm.position.z + 120.0) / 240.0)  # -120 a 120
            ataque = int(ATAQUE_RECUO + z_norm * (ATAQUE_AVANCO - ATAQUE_RECUO))
            
            y_norm = clamp((hand.palm.position.y - 150.0) / 200.0)  # 150 a 350
            altura = int(ALTURA_BAIXO + y_norm * (ALTURA_CIMA - ALTURA_BAIXO))
            
            # Imprime os valores normalizados
            print(
                f"Rotação: {x_norm:.3f} | Ataque: {z_norm:.3f} | Altura: {y_norm:.3f} | Palma: {palma_da_mao:.3f})"
            )
            
            pacote = bytes([garra, rotacao, ataque, altura])
            arduino.write(bytes(pacote))

        else:
            # Nenhuma mão posicionada, coloca no centro do movimento em todos os eixos
            # pacote = bytes([
            #     int(GARRA_ABERTA + (GARRA_FECHADA - GARRA_ABERTA) / 2),
            #     int(ROT_DIR + (ROT_ESQ - ROT_DIR) / 2),
            #     int(ATAQUE_RECUO + (ATAQUE_AVANCO - ATAQUE_RECUO) / 2),
            #     int(ALTURA_BAIXO + (ALTURA_CIMA - ALTURA_BAIXO) / 2)
            # ])
            pacote = bytes([
                int(90),
                int(90),
                int(90),
                int(90)
            ])
            arduino.write(bytes(pacote))


def main():
    my_listener = MyListener()

    connection = leap.Connection()
    connection.add_listener(my_listener)

    running = True

    with connection.open():
        connection.set_tracking_mode(leap.TrackingMode.Desktop)
        while running:
            time.sleep(1)

    arduino.close()


if __name__ == "__main__":
    main()

