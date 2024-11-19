from io_utils import handle_io_operations

def add_processes_to_queue(processes, queue, clock, next_index):
    """
    Añade a la cola de listos los procesos que han llegado al sistema
    hasta el tiempo actual del reloj.

    Parámetros:
    - processes (list): Lista de procesos ordenados por tiempo de llegada.
    - queue (deque): Cola de procesos listos para ejecutarse.
    - clock (int): Tiempo actual del reloj del sistema (en ms).
    - next_index (int): Índice del siguiente proceso por evaluar en la lista.

    Nota:
    - Esta función modifica la cola pero no retorna el nuevo índice actualizado.
      El control del índice debe manejarse externamente si se desea seguimiento.
    """
    while next_index < len(processes) and processes[next_index]['arrival_time'] <= clock:
        queue.append(processes[next_index])
        next_index += 1


def print_ready_queue(queue, clock):
    """
    Imprime el estado actual de la cola de procesos listos.

    Parámetros:
    - queue (deque): Cola de procesos listos.
    - clock (int): Tiempo actual del reloj del sistema.
    """
    ready_queue_ids = [p['id'] for p in queue]
    print(f"Clock {clock} ms: Ready queue: {ready_queue_ids}")


def execute_process(current_process, queue, gantt_chart, clock, quantum, context_switch_time):
    """
    Ejecuta un proceso durante un intervalo limitado por el quantum o el tiempo restante.

    - Si el proceso termina su ejecución, se marca su tiempo de finalización.
    - Si el proceso requiere más tiempo, se simulan sus operaciones de E/S y se reencola.
    - Se actualiza el diagrama de Gantt con el intervalo de ejecución.

    Parámetros:
    - current_process (dict): Proceso que está siendo ejecutado.
    - queue (deque): Cola de procesos listos (el proceso puede volver a esta cola).
    - gantt_chart (list): Lista de tuplas para construir el diagrama de Gantt.
    - clock (int): Tiempo actual del sistema (antes de ejecutar el proceso).
    - quantum (int): Tiempo máximo que puede ejecutarse el proceso en una ronda.
    - context_switch_time (int): Tiempo extra después de ejecutar el proceso (por cambio de contexto).

    Retorna:
    - (int): Nuevo valor del reloj después de ejecutar el proceso y aplicar el cambio de contexto.
    """
    if 'start_time' not in current_process:
        current_process['start_time'] = clock  # Marcar la primera vez que se ejecuta

    execution_time = min(quantum, current_process['remaining_time'])

    # Registrar ejecución en el diagrama de Gantt
    gantt_chart.append((current_process['id'], clock, clock + execution_time))

    # Avanzar el reloj y reducir el tiempo restante
    clock += execution_time
    current_process['remaining_time'] -= execution_time

    if current_process['remaining_time'] == 0:
        # Proceso terminado
        current_process['completion_time'] = clock
    else:
        # Simular operación de E/S (si existe) y volver a encolar
        handle_io_operations(current_process, clock)
        queue.append(current_process)

    return clock + context_switch_time  # Se incluye el costo del cambio de contexto


def is_process_completed(process):
    """
    Verifica si el proceso ha finalizado toda su ejecución de CPU.

    Parámetro:
    - process (dict): Proceso a evaluar.

    Retorna:
    - (bool): True si no queda CPU por ejecutar, False en caso contrario.
    """
    return process['remaining_time'] == 0


def advance_to_next_arrival(processes, next_index, clock):
    """
    Avanza el reloj al tiempo de llegada del siguiente proceso si no hay procesos listos.

    Parámetros:
    - processes (list): Lista ordenada de procesos.
    - next_index (int): Índice del siguiente proceso por llegar.
    - clock (int): Tiempo actual del sistema.

    Retorna:
    - (int): Nuevo valor del reloj avanzado al próximo arribo.
    """
    return processes[next_index]['arrival_time']
