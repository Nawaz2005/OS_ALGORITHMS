
def priority_scheduling(processes, burst_times, priorities):
    n = len(processes)
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    process_data = [(i, burst_times[i], priorities[i]) for i in range(n)]
    process_data.sort(key=lambda x: x[2])
    completion_time[0] = process_data[0][1]
    for i in range(1, n):
        completion_time[i] = completion_time[i - 1] + process_data[i][1]
    for i in range(n):
        turnaround_time[i] = completion_time[i]
        waiting_time[i] = turnaround_time[i] - burst_times[process_data[i][0]]
        t_sum=0
        w_sum=0
    for i in range(n):
        t_sum+=turnaround_time[i]
        w_sum+=waiting_time[i]
   
    print("Average turnarround:",t_sum/n)
    print("Average waiting time:",w_sum/n)
    print("Process\tBurst Time\tPriority\tCompletion Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        idx = process_data[i][0]
        print(f"{processes[idx]}\t {burst_times[idx]}\t {priorities[idx]}\t {completion_time[i]}\t {waiting_time[i]}\t {turnaround_time[i]}")
if __name__ == "__main__":
    processes = [1, 2, 3, 4, 5]
    burst_times = [8, 4, 6, 3, 7]
    priorities = [3, 1, 4, 2, 5]
    priority_scheduling(processes, burst_times, priorities)

