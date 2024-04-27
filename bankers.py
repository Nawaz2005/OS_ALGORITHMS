import numpy as np

# Number of processes
n = 5
# Number of resources
m = 3
 
# Available resources
available = np.array([3, 3, 2])

# Maximum resources that can be allocated to processes
max_resources = np.array([[7, 5, 3],
                           [3, 2, 2],
                           [9, 0, 2],
                           [2, 2, 2],
                           [4, 3, 3]])

# Resources currently allocated to processes
allocated = np.array([[0, 1, 0],
                       [2, 0, 0],
                       [3, 0, 2],
                       [2, 1, 1],
                       [0, 0, 2]])

# Need matrix
need = max_resources - allocated

# Finish array
finish = np.zeros(n, dtype=bool)

# Safe sequence
safe_sequence = []

# Check if a process can be allocated resources
def can_allocate(process_id):
    return all(need[process_id] <= available)

# Find a process that can be allocated resources
def find_process():
    for i in range(n):
        if not finish[i] and can_allocate(i):
            return i
    return None

# Banker's Algorithm
while True:
    process_id = find_process()
    if process_id is None:
        break
    safe_sequence.append(process_id)
    available += allocated[process_id]
    finish[process_id] = True

# Check if all processes are finished
if all(finish):
    print("Safe sequence:", safe_sequence)
else:
    print("Unsafe state, deadlock may occur.")
