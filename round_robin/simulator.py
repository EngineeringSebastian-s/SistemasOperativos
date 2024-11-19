import collections
from process_utils import (
    add_processes_to_queue, print_ready_queue, execute_process,
    is_process_completed, advance_to_next_arrival
)
from metrics import calculate_metrics, display_gantt_chart

def simulate_round_robin(processes, quantum, context_switch_time):
    """
    Simula el algoritmo de planificación Round Robin para un conjunto de procesos.

    Round Robin asigna un tiempo fijo (quantum) a cada proceso en la cola. Si el proceso
    no termina en ese tiempo, se reencola al final y se continúa con el siguiente.
    También se consideran cambios de contexto y operaciones de entrada/salida.

    Parámetros:
    - processes (list of dict): Lista de procesos. Cada proceso debe tener:
        - 'id': Identificador del proceso.
        - 'arrival_time': Tiempo en que el proceso llega al sistema.
        - 'cpu_time': Tiempo total de CPU necesario.
        - 'remaining_time': Tiempo restante de CPU al inicio (igual a cpu_time).
        - 'io_times': Lista de duraciones de E/S pendientes.
        - 'cpu_after_io': CPU adicional después de cada E/S.
    - quantum (int): Tiempo máximo (en ms) que puede usar un proceso antes de ser interrumpido.
    - context_switch_time (int): Tiempo (en ms) que tarda un cambio de contexto.

    Retorna:
    - completed_processes (list of dict): Lista de procesos con métricas agregadas:
        - 'completion_time', 'turnaround_time', 'waiting_time'

    Efectos:
    - Imprime el estado de la cola de listos en cada ciclo.
    - Muestra un diagrama de Gantt al final con los intervalos de ejecución.
    """

    clock = 0  # Reloj del sistema en ms
    queue = collections.deque()  # Cola de procesos listos
    completed_processes = []  # Procesos que ya terminaron
    gantt_chart = []  # Lista de tuplas (proceso_id, tiempo_inicio, tiempo_fin)

    # Ordenar los procesos por tiempo de llegada
    processes.sort(key=lambda p: p['arrival_time'])
    next_process_index = 0  # Índice del próximo proceso a agregar a la cola

    # Bucle principal de la simulación
    while len(completed_processes) < len(processes):
        # Agregar procesos que hayan llegado al tiempo actual
        add_processes_to_queue(processes, queue, clock, next_process_index)

        # Mostrar estado de la cola de listos
        print_ready_queue(queue, clock)

        if queue:
            # Ejecutar siguiente proceso de la cola
            current_process = queue.popleft()
            clock = execute_process(
                current_process, queue, gantt_chart, clock, quantum, context_switch_time
            )
            # Si el proceso terminó, agregar a la lista de completados
            if is_process_completed(current_process):
                completed_processes.append(current_process)
        else:
            # Si la cola está vacía, avanzar el reloj al próximo arribo
            clock = advance_to_next_arrival(processes, next_process_index, clock)

    # Calcular métricas de rendimiento y mostrar Gantt
    calculate_metrics(completed_processes)
    display_gantt_chart(gantt_chart)

    return completed_processes
