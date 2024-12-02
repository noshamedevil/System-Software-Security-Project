import matplotlib.pyplot as plt
import numpy as np

# Path to the output file containing the cache access timings
file_path = "L3-capture.txt"  # Update with your actual file path

# Initialize an empty list to store collected timing data
cache_access_times = []

# Read the file and start processing from line 5
with open(file_path, "r") as file:
    lines = file.readlines()[4:]  # Skip the first 4 lines

    for line in lines:
        # Check if any non-zero value exists in the line
        if any(int(value) > 0 for value in line.split() if value.isdigit()):
            # Convert the entire line into integers and extend the list
            cache_access_times.extend(map(int, filter(str.isdigit, line.split())))

# Convert to a numpy array for easier manipulation
cache_access_times = np.array(cache_access_times)

# Check how much data was collected
print(f"Collected {len(cache_access_times)} cache access times.")

# If no data collected, exit early
if len(cache_access_times) == 0:
    print("No non-zero data found in the file.")
else:
    # Visualization 1: Histogram of Cache Access Times
    plt.figure(figsize=(10, 6))
    plt.hist(cache_access_times, bins=50, alpha=0.7, color="blue", edgecolor="black")
    plt.title("Histogram of Cache Access Times (L3 Cache)")
    plt.xlabel("Access Time (cycles)")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

    # Visualization 2: Sequential Plot of Cache Access Times
    plt.figure(figsize=(10, 6))
    plt.plot(cache_access_times, color="red", linewidth=0.8)
    plt.title("Sequential Cache Access Times (L3 Cache)")
    plt.xlabel("Sample Index")
    plt.ylabel("Access Time (cycles)")
    plt.grid(True)
    plt.show()