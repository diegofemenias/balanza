import serial
import time

try:
    print("Intentando abrir el puerto...")
    arduino = serial.Serial('/dev/cu.usbserial-1140', 4800, timeout=1)
    print("Puerto abierto exitosamente.")
    time.sleep(2)
except Exception as e:
    print(f"Error al abrir el puerto: {e}")

def recibir():
    response = arduino.readline().decode().strip()
    print("Arduino says:", response)

while True:
    recibir()

arduino.close()