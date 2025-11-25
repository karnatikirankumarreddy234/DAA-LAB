import time

def find_pairs_brute(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs

# Sample input
arr = list(range(1, 1000))  # Adjust size for experiment
target = 1500

# Run the code 5 times and measure execution time
for run in range(1, 6):
    start = time.time()
    pairs = find_pairs_brute(arr, target)
    end = time.time()
    print(f"Run {run}: Execution Time = {(end - start):.6f} seconds")