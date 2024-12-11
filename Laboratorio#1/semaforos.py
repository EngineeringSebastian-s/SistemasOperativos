import threading
import time
import random

# Semáforo para controlar la capacidad del puente (3 vehículos)
bridge_capacity = threading.Semaphore(3)
# Semáforo para bloquear la entrada hasta que los 3 vehículos actuales hayan pasado
batch_semaphore = threading.Semaphore(0)

# Variable para contar los vehículos que han cruzado en el lote actual
vehicles_crossed = 0
vehicles_lock = threading.Lock()  # Controla el acceso a la variable vehicles_crossed

# Lista para almacenar mensajes de cada vehículo para mayor claridad
log = []

def log_message(message):
    """Agrega un mensaje al registro de eventos del puente."""
    log.append(message)
    print(message)

def vehicle_entry(vehicle_id):
    """Simula un vehículo intentando entrar al puente.
    
    Argumentos:
    vehicle_id (int): ID del vehículo que intenta cruzar.
    """
    global vehicles_crossed

    log_message(f"Vehículo {vehicle_id}: Llegando a la entrada del puente.")

    # Adquirir un lugar en el puente
    bridge_capacity.acquire()
    log_message(f"Vehículo {vehicle_id}: Pasando por el puente.")

    # Simular el tiempo que tarda en cruzar el puente
    time.sleep(random.uniform(1, 10))

    # Salida del puente
    log_message(f"Vehículo {vehicle_id}: Ha cruzado el puente.")

    with vehicles_lock:
        vehicles_crossed += 1
        # Cuando 3 vehículos han cruzado, permitir el siguiente lote
        if vehicles_crossed == 3:
            print("Ya han cruzado 3 vehículos, se revisa la integridad del puente.")
            time.sleep(random.uniform(1, 10))
            vehicles_crossed = 0  # Reinicia el conteo para el siguiente lote
            # Permitir que el siguiente lote de vehículos entre
            print("El puente está perfecto, se da acceso al siguiente lote")
            # Liberar el semáforo para los siguientes 3 vehículos
            for _ in range(3):
                batch_semaphore.release()

    # Libera el lugar en el puente para el siguiente vehículo
    bridge_capacity.release()

def vehicle_process(vehicle_id):
    """Gestiona el proceso completo de un vehículo.
    
    Argumentos:
    vehicle_id (int): ID del vehículo que intenta cruzar.
    """
    # Espera su turno si no es parte del primer grupo de 3 vehículos
    batch_semaphore.acquire()
    vehicle_entry(vehicle_id)

# Creación y ejecución de vehículos
def main():
    """Función principal para simular el paso de vehículos por el puente."""
    threads = []
    num_vehicles = 10  # Número total de vehículos que intentarán cruzar el puente

    # Inicialmente liberar permiso para los primeros 3 vehículos
    for _ in range(3):
        batch_semaphore.release()

    # Crear hilos para cada vehículo
    for i in range(num_vehicles):
        t = threading.Thread(target=vehicle_process, args=(i,))
        threads.append(t)
        t.start()
        time.sleep(random.uniform(1, 10))  # Pausa para simular el intervalo de llegada de vehículos

    # Esperar a que todos los vehículos terminen de cruzar
    for t in threads:
        t.join()

    log_message("Todos los vehículos han cruzado el puente.")

if _name_ == "_main_":
    main()
