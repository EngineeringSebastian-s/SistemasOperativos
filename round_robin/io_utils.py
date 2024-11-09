def handle_io_operations(process, clock):
    """
    Simula las operaciones de entrada/salida (I/O) de un proceso en ejecución.

    Este método se llama cuando un proceso no ha finalizado su ejecución completa
    y puede requerir una operación de E/S. La función actualiza el reloj del sistema
    y ajusta el tiempo de CPU restante según la CPU que debe ejecutarse luego de la E/S.

    Parámetros:
    - process (dict): Diccionario que representa el proceso en ejecución. Contiene:
        - 'io_times': Lista de duraciones de operaciones de E/S pendientes.
        - 'cpu_after_io': Lista de tiempos de CPU que se deben ejecutar después de cada E/S.
        - 'remaining_time': Tiempo restante de CPU del proceso (se incrementa si hay más CPU después de E/S).
    - clock (int): Tiempo actual del reloj del sistema en milisegundos.

    Efectos:
    - Modifica el proceso, retirando su próxima operación de E/S y, si corresponde,
      agregando el tiempo de CPU adicional a 'remaining_time'.
    - Actualiza el reloj localmente (pero el cambio **no se refleja fuera de esta función**).

    Nota:
    - Esta función no retorna el nuevo clock, ya que el cambio es interno.
      Si necesitas usar el clock actualizado, deberías devolverlo.
    """
    if process['io_times']:
        io_time = process['io_times'].pop(0)
        clock += io_time
        if process['cpu_after_io']:
            additional_cpu = process['cpu_after_io'].pop(0)
            process['remaining_time'] += additional_cpu
