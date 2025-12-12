import psutil
import time
import os

def monitor_processes():
    """Lists basic info for all running processes."""
    # Clear console for a cleaner output (optional)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print(f"{'PID':<10} {'Name':<25} {'CPU %':<10} {'Memory %':<10}")
    print("-" * 55)

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Obtener valores en forma directa; cpu_percent(None) usa el último muestreo
            cpu = proc.cpu_percent(interval=None)
            mem = proc.memory_percent()
            pid = proc.pid
            name = proc.name() or ''
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

        # Normalizar None a 0.0 antes de formatear
        if cpu is None:
            cpu = 0.0
        if mem is None:
            mem = 0.0

        print(f"{pid:<10} {name:<25} {cpu:<10.2f} {mem:<10.2f}")

if __name__ == "__main__":
    # Warm-up: inicializa las lecturas de cpu_percent para que la siguiente medición sea válida
    for p in psutil.process_iter():
        try:
            p.cpu_percent(None)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    try:
        while True:
            monitor_processes()
            time.sleep(10)  # actualizar cada 10 segundos
    except KeyboardInterrupt:
        print("\nProcess monitoring stopped.")