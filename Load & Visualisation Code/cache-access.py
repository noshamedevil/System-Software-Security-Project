import numpy as np
import time

# Function to simulate memory access
def access_memory(cache_level):
    # Simulate different sizes of memory access for different cache levels
    if cache_level == 'L1':
        print("Simulating L1 cache access...")
        size = 100000  # Small size to trigger L1 cache access
    elif cache_level == 'L2':
        print("Simulating L2 cache access...")
        size = 1000000  # Medium size to trigger L2 cache access
    elif cache_level == 'L3':
        print("Simulating L3 cache access...")
        size = 10000000  # Larger size to trigger L3 cache access
    else:
        print("Invalid cache level selected.")
        return

    # Create a large array that will access memory in a sequential pattern
    data = np.arange(size)

    # Perform read operations to access memory (sequential access)
    print(f"Accessing {size} elements to simulate {cache_level} cache accesses...\n")
    start_time = time.time()
    for _ in range(10):
    	for i in range(size):
        	_ = data[i]  # Access the array sequentially
    	end_time = time.time()
    	time.sleep(0.5)
    print(f"Time taken to access {size} elements: {end_time - start_time:.4f} seconds.\n")

def main():
    # Ask the user for the memory level they want to test
    print("Choose the level of memory cache to access (L1, L2, L3): ")
    cache_level = input().strip().upper()

    # Perform memory access based on user's input
    access_memory(cache_level)

    print("Cache access simulation complete.")

if __name__ == '__main__':
    main()

