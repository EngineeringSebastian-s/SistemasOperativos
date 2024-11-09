def calculate_metrics(processes):
    """
       Calcula métricas clave de rendimiento para cada proceso al finalizar la simulación.

       Las métricas calculadas son:
       - Turnaround Time (TAT): Tiempo total desde que el proceso llegó hasta que finalizó.
           Fórmula: completion_time - arrival_time
       - Waiting Time (WT): Tiempo total que el proceso pasó esperando en la cola de listos.
           Fórmula: turnaround_time - cpu_time

       Parámetros:
       - processes (list): Lista de diccionarios, cada uno representando un proceso con las claves:
           - 'arrival_time'
           - 'completion_time'
           - 'cpu_time'
           - Las nuevas claves añadidas son:
               - 'turnaround_time'
               - 'waiting_time'
       """
    for process in processes:
        process['turnaround_time'] = process['completion_time'] - process['arrival_time']
        process['waiting_time'] = process['turnaround_time'] - process['cpu_time']

def display_gantt_chart(gantt_chart):
    """
        Muestra el diagrama de Gantt en consola, indicando los intervalos de ejecución por proceso.

        Cada entrada del diagrama de Gantt representa una fracción de tiempo en la que un
        proceso estuvo en ejecución. Se muestran en el orden en que se ejecutaron.

        Parámetros:
        - gantt_chart (list): Lista de tuplas en formato (process_id, start_time, end_time),
          donde:
            - process_id: ID del proceso que se ejecutó
            - start_time: Tiempo en milisegundos en que inició la ejecución
            - end_time: Tiempo en milisegundos en que finalizó la ejecución
        """
    print("\nGantt Chart:")
    for entry in gantt_chart:
        print(f"Process {entry[0]}: {entry[1]} ms -> {entry[2]} ms")
