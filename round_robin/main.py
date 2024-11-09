from simulator import simulate_round_robin

# Punto de entrada principal del programa
if __name__ == "__main__":
    # 🔧 PRUEBA 1: Definición de procesos para simular
    # Cada proceso contiene:
    # - id: Identificador único
    # - arrival_time: Tiempo en que el proceso llega al sistema (en ms)
    # - cpu_time: Tiempo total que requiere de CPU (incluyendo después de I/O)
    # - remaining_time: Tiempo restante de CPU (se actualiza en tiempo de ejecución)
    # - io_times: Lista de duraciones de operaciones de E/S (se ejecutan en orden)
    # - cpu_after_io: Tiempos adicionales de CPU requeridos después de cada E/S

    processes = [
        {
            'id': 0,
            'arrival_time': 0,
            'cpu_time': 10,
            'remaining_time': 10,
            'io_times': [2, 2],
            'cpu_after_io': [1, 2]
        },
        {
            'id': 1,
            'arrival_time': 80,
            'cpu_time': 12,
            'remaining_time': 12,
            'io_times': [2],
            'cpu_after_io': [2]
        },
        {
            'id': 2,
            'arrival_time': 200,
            'cpu_time': 5,
            'remaining_time': 5,
            'io_times': [],
            'cpu_after_io': []
        }
    ]

    # ⏱ Configuración de la simulación
    quantum = 4                # Tiempo máximo que un proceso puede ejecutar antes de ser interrumpido
    context_switch_time = 1   # Tiempo de cambio de contexto entre procesos

    # ▶️ Ejecución de la simulación Round Robin
    result = simulate_round_robin(processes, quantum, context_switch_time)

    # 📊 Cálculo de métricas globales
    total_turnaround_time = sum(p['turnaround_time'] for p in result)
    total_waiting_time = sum(p['waiting_time'] for p in result)

    # 📋 Resultados individuales por proceso
    print("\nProcess Execution Results:")
    for process in result:
        print(f"Process {process['id']}: Turnaround Time = {process['turnaround_time']} ms, Waiting Time = {process['waiting_time']} ms")

    # 📈 Promedios de las métricas
    print(f"\nAverage Turnaround Time: {total_turnaround_time / len(processes):.2f} ms")
    print(f"Average Waiting Time: {total_waiting_time / len(processes):.2f} ms")
