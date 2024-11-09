from io_utils import handle_io_operations

def add_processes_to_queue(processes, queue, clock, next_index):
    while next_index < len(processes) and processes[next_index]['arrival_time'] <= clock:
        queue.append(processes[next_index])
        next_index += 1

def print_ready_queue(queue, clock):
    ready_queue_ids = [p['id'] for p in queue]
    print(f"Clock {clock} ms: Ready queue: {ready_queue_ids}")

def execute_process(current_process, queue, gantt_chart, clock, quantum, context_switch_time):
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

def is_process_completed(process):
    return process['remaining_time'] == 0

def advance_to_next_arrival(processes, next_index, clock):
    return processes[next_index]['arrival_time']
