import collections


def simulate_round_robin(processes, quantum, context_switch_time):
    """
    Simula el algoritmo de planificación Round Robin.

    :param processes: Lista de diccionarios con los detalles de los procesos.
    :param quantum: Quantum de tiempo en milisegundos.
    :param context_switch_time: Tiempo necesario para el cambio de contexto en milisegundos.
    """
    clock = 0
    queue = collections.deque()
    completed_processes = []
    gantt_chart = []  # Lista para construir el diagrama de Gantt

    # Ordenar los procesos por tiempo de llegada
    processes.sort(key=lambda p: p['arrival_time'])
    next_process_index = 0

    while len(completed_processes) < len(processes):
        add_processes_to_queue(processes, queue, clock, next_process_index)

        # Mostrar la cola de procesos listos
        print_ready_queue(queue, clock)

        if queue:
            current_process = queue.popleft()
            clock = execute_process(current_process, queue, gantt_chart, clock, quantum, context_switch_time)
            if is_process_completed(current_process):
                completed_processes.append(current_process)
        else:
            # Avanzar el reloj al próximo arribo si no hay procesos listos
            clock = advance_to_next_arrival(processes, next_process_index, clock)

    calculate_metrics(completed_processes)
    display_gantt_chart(gantt_chart)

    return completed_processes


def add_processes_to_queue(processes, queue, clock, next_process_index):
    """Añade los procesos que han llegado a la cola."""
    while next_process_index < len(processes) and processes[next_process_index]['arrival_time'] <= clock:
        queue.append(processes[next_process_index])
        next_process_index += 1


def print_ready_queue(queue, clock):
    """Imprime los procesos listos en la cola."""
    ready_queue_ids = [p['id'] for p in queue]
    print(f"Clock {clock} ms: Ready queue: {ready_queue_ids}")


def execute_process(current_process, queue, gantt_chart, clock, quantum, context_switch_time):
    """Simula la ejecución de un proceso."""
    if 'start_time' not in current_process:
        current_process['start_time'] = clock

    execution_time = min(quantum, current_process['remaining_time'])
    gantt_chart.append((current_process['id'], clock, clock + execution_time))
    clock += execution_time
    current_process['remaining_time'] -= execution_time

    if current_process['remaining_time'] == 0:
        current_process['completion_time'] = clock
    else:
        handle_io_operations(current_process, clock)
        queue.append(current_process)

    return clock + context_switch_time


def handle_io_operations(process, clock):
    """Maneja las operaciones de entrada/salida de un proceso."""
    if process['io_times']:
        io_time = process['io_times'].pop(0)
        clock += io_time
        if process['cpu_after_io']:
            additional_cpu = process['cpu_after_io'].pop(0)
            process['remaining_time'] += additional_cpu


def is_process_completed(process):
    """Verifica si un proceso ha terminado su ejecución."""
    return process['remaining_time'] == 0


def advance_to_next_arrival(processes, next_process_index, clock):
    """Avanza el reloj al próximo arribo de procesos."""
    return processes[next_process_index]['arrival_time']


def calculate_metrics(processes):
    """Calcula métricas adicionales como turnaround time y waiting time."""
    for process in processes:
        process['turnaround_time'] = process['completion_time'] - process['arrival_time']
        process['waiting_time'] = process['turnaround_time'] - process['cpu_time']


def display_gantt_chart(gantt_chart):
    """Muestra el diagrama de Gantt."""
    print("\nGantt Chart:")
    for entry in gantt_chart:
        print(f"Process {entry[0]}: {entry[1]} ms -> {entry[2]} ms")


# Ejemplo de uso
if __name__ == "__main__":
    processes = [
        {
            'id': 0,
            'arrivalTime': 0,
            'cpuTime': 10,  # Suma de los tiempos de CPU antes y después de las operaciones de E/S
            'remainingTime': 10,  # Inicialmente igual al tiempo total de CPU
            'ioTimes': [2, 2],  # Tiempos de operaciones de E/S en orden
            'cpuAfterIO': [1, 2]  # Tiempos de CPU requeridos después de cada operación de E/S
        },
        {
            'id': 1,
            'arrivalTime': 80,
            'cpuTime': 12,
            'remainingTime': 12,
            'ioTimes': [2],  # Sólo tiene una operación de E/S
            'cpuAfterIO': [2]  # Tiempo de CPU después de esa E/S
        },
        {
            'id': 2,
            'arrivalTime': 200,
            'cpuTime': 5,
            'remainingTime': 5,
            'ioTimes': [],  # No tiene operaciones de E/S
            'cpuAfterIO': []  # No necesita tiempos de CPU adicionales
        }
    ]

    quantum = 4
    context_switch_time = 1

    result = simulate_round_robin(processes, quantum, context_switch_time)

    total_turnaround_time = 0
    total_waiting_time = 0
    print("\nProcess Execution Results:")
    for process in result:
        print(
            f"Process {process['id']}: Turnaround Time = {process['turnaround_time']} ms, Waiting Time = {process['waiting_time']} ms")
        total_turnaround_time += process['turnaround_time']
        total_waiting_time += process['waiting_time']

    print(f"\nAverage Turnaround Time: {total_turnaround_time / len(processes):.2f} ms")
    print(f"Average Waiting Time: {total_waiting_time / len(processes):.2f} ms")
