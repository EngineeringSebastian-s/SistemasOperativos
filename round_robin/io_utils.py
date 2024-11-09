def handle_io_operations(process, clock):
    if process['io_times']:
        io_time = process['io_times'].pop(0)
        clock += io_time
        if process['cpu_after_io']:
            additional_cpu = process['cpu_after_io'].pop(0)
            process['remaining_time'] += additional_cpu
