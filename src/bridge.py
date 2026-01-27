import serial

def listen_to_arduino(port='/dev/ttyACM0', baud=9600):
    """Simple bridge to capture signal from Arduino."""
    try:
        with serial.Serial(port, baud, timeout=1) as ser:
            print(f"Connected to {port}. Waiting for data...")
            while True:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    print(f"Signal Received: {line}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    listen_to_arduino()