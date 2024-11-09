import collections
from process_utils import (
    add_processes_to_queue, print_ready_queue, execute_process,
    is_process_completed, advance_to_next_arrival
)
from metrics import calculate_metrics, display_gantt_chart

def simulate_round_robin(processes, quantum, context_switch_time):
    clock = 0
    queue = collections.deque()
    completed_processes = []
    gantt_chart = []

    processes.sort(key=lambda p: p['arrival_time'])
    next_process_index = 0

    while len(completed_processes) < len(processes):
        add_processes_to_queue(processes, queue, clock, next_process_index)

        print_ready_queue(queue, clock)

        if queue:
            current_process = queue.popleft()
            clock = execute_process(current_process, queue, gantt_chart, clock, quantum, context_switch_time)
            if is_process_completed(current_process):
                completed_processes.append(current_process)
        else:
            clock = advance_to_next_arrival(processes, next_process_index, clock)

    calculate_metrics(completed_processes)
    display_gantt_chart(gantt_chart)

    return completed_processes
