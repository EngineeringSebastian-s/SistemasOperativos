def calculate_metrics(processes):
    for process in processes:
        process['turnaround_time'] = process['completion_time'] - process['arrival_time']
        process['waiting_time'] = process['turnaround_time'] - process['cpu_time']

def display_gantt_chart(gantt_chart):
    print("\nGantt Chart:")
    for entry in gantt_chart:
        print(f"Process {entry[0]}: {entry[1]} ms -> {entry[2]} ms")
