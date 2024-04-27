def sjf_scheduling(processes):
    n = len(processes)
    burst_times = [p[1] for p in processes]
    waiting_times = [0] * n
    turnaround_times = [0] * n

    # Sort processes by burst time
    sorted_processes = sorted(processes, key=lambda x: x[1])

    # Calculate waiting times
    waiting_times[0] = 0
    for i in range(1, n):
        waiting_times[i] = burst_times[i-1] + waiting_times[i-1]

    # Calculate turnaround times
    for i in range(n):
        turnaround_times[i] = waiting_times[i] + burst_times[i]

    return sorted_processes, waiting_times, turnaround_times

# Processes with burst times provided directly in the code
processes = [(1, 6), (2, 8), (3, 7), (4, 3), (5, 4)]

sorted_processes, waiting_times, turnaround_times = sjf_scheduling(processes)

print('Process\tBurst Time\tWaiting Time\tTurnaround Time')
for i in range(len(sorted_processes)):
    print(f'{sorted_processes[i][0]}\t{sorted_processes[i][1]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}')

print('Average waiting time:', sum(waiting_times) / len(waiting_times))
print('Average turnaround time:', sum(turnaround_times) / len(turnaround_times))
