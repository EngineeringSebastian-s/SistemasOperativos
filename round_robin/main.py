from simulator import simulate_round_robin

if __name__ == "__main__":
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

    quantum = 4
    context_switch_time = 1

    result = simulate_round_robin(processes, quantum, context_switch_time)

    total_turnaround_time = sum(p['turnaround_time'] for p in result)
    total_waiting_time = sum(p['waiting_time'] for p in result)

    print("\nProcess Execution Results:")
    for process in result:
        print(f"Process {process['id']}: Turnaround Time = {process['turnaround_time']} ms, Waiting Time = {process['waiting_time']} ms")

    print(f"\nAverage Turnaround Time: {total_turnaround_time / len(processes):.2f} ms")
    print(f"Average Waiting Time: {total_waiting_time / len(processes):.2f} ms")
