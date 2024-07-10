import random
import time
import os

# Check if array is sorted
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# BogoSort Algorithm
def bogo_sort(arr):
    attempts = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
    return attempts

def main():
    # Get elements count
    n = int(os.getenv('NUM_ELEMENTS', 1))
    save_output = os.getenv('SAVE_OUTPUT', 'false').lower() == 'true'
    
    # Fill array with the specified amount of random elements
    arr = [random.randint(1, 100) for _ in range(n)]
    
    output = []
    output.append(f"Ursprüngliches Array: {arr}")
    
    # Start time measurement
    start_time = time.time()
    
    # Run BogoSort
    attempts = bogo_sort(arr)
    
    # Stop time measurement
    end_time = time.time()
    
    # Output
    output.append(f"Sortiertes Array: {arr}")
    output.append(f"Anzahl der Versuche: {attempts}")
    output.append(f"Zeit benötigt: {end_time - start_time} Sekunden")
    
    output_text = "\n".join(output)
    print(output_text)
    
    # Write to file if SAVE_OUTPUT=true is set
    if save_output:
        os.makedirs("/output", exist_ok=True)
        with open("/output/bogosort_output.txt", "w") as f:
            f.write(output_text)

if __name__ == "__main__":
    main()
