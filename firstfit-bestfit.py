def first_fit(block_sizes, process_sizes):
    allocation = [-1] * len(process_sizes)
    for i in range(len(process_sizes)):
        for j in range(len(block_sizes)):
            if block_sizes[j] >= process_sizes[i]:
                allocation[i] = j
                block_sizes[j] -= process_sizes[i]
                break
    return allocation

def best_fit(block_sizes, process_sizes):
    allocation = [-1] * len(process_sizes)
    for i in range(len(process_sizes)):
        best_index = -1
        for j in range(len(block_sizes)):
            if block_sizes[j] >= process_sizes[i]:
                if best_index == -1 or block_sizes[j] < block_sizes[best_index]:
                    best_index = j
        if best_index != -1:
            allocation[i] = best_index
            block_sizes[best_index] -= process_sizes[i]
    return allocation

def worst_fit(block_sizes, process_sizes):
    allocation = [-1] * len(process_sizes)
    for i in range(len(process_sizes)):
        worst_index = -1
        for j in range(len(block_sizes)):
            if block_sizes[j] >= process_sizes[i]:
                if worst_index == -1 or block_sizes[j] > block_sizes[worst_index]:
                    worst_index = j
        if worst_index != -1:
            allocation[i] = worst_index
            block_sizes[worst_index] -= process_sizes[i]
    return allocation

# Example usage
if __name__ == "__main__":
    block_sizes = [100, 500, 200, 300, 600]
    process_sizes = [212, 417, 112, 426]
    
    print("First Fit Allocation:", first_fit(block_sizes.copy(), process_sizes.copy()))
    print("Best Fit Allocation:", best_fit(block_sizes.copy(), process_sizes.copy()))
    print("Worst Fit Allocation:", worst_fit(block_sizes.copy(), process_sizes.copy()))