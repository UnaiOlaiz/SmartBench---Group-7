import time
import serial
import os

# Configuración del puerto UART
# '/dev/serial0' es el puerto por defecto en Raspberry Pi tras configurar raspi-config
ser = serial.Serial('/dev/serial0', 9600, timeout=1)

# Este es el "interruptor virtual". Si existe, las luces se apagan.
LOCK_FILE = "/tmp/leds_off_mode"

def listen():
    print("listening... (Di 'Hicell' para despertar)")
    
    while True:
        if ser.in_waiting > 0:
            # Leemos el byte que manda el sensor
            byte_data = ser.read()
            # Lo convertimos a número
            cmd_id = int.from_bytes(byte_data, byteorder='little')
            
            print(f"Comando recibido ID: {cmd_id}")

            # --- Lógica de Control ---

            # Comando 1: "Turn on the light" -> Borramos el bloqueo
            if cmd_id == 1:
                print("COMANDO: Encender luces (Volver a modo Clima)")
                if os.path.exists(LOCK_FILE):
                    os.remove(LOCK_FILE)

            # Comando 2: "Turn off the light" -> Creamos el bloqueo
            elif cmd_id == 2:
                print("COMANDO: Apagar luces")
                # Creamos el archivo vacío
                open(LOCK_FILE, "w").close()

            # Limpiamos el buffer para evitar lecturas falsas
            ser.reset_input_buffer()
            
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        print("Sensor de voz detenido.")
