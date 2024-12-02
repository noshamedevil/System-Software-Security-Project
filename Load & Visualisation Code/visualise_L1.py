import matplotlib.pyplot as plt
import numpy as np

# Load the data from the file
file_path = "l1-capture-rsa.txt"  # Path to your L1-capture output file

# Read the data
with open(file_path, "r") as file:
    raw_data = file.read()

# Split the data into a list of integers
data = [int(x) for x in raw_data.split() if x.isdigit()]

# Summary statistics
print(f"Total data points: {len(data)}")
print(f"Mean value: {np.mean(data):.2f}")
print(f"Median value: {np.median(data):.2f}")
print(f"Max value: {max(data)}")
print(f"Min value: {min(data)}")

# Plot the data
plt.figure(figsize=(10, 6))

# Histogram
plt.hist(data, bins=50, alpha=0.7, color="blue", edgecolor="black")
plt.title("Histogram of Cache Access Times (L1-capture)")
plt.xlabel("Access Time (cycles)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Line plot for sequential analysis
plt.figure(figsize=(10, 6))
plt.plot(data, color="red", linewidth=0.8)
plt.title("Sequential Cache Access Times (L1-capture)")
plt.xlabel("Sample Index")
plt.ylabel("Access Time (cycles)")
plt.grid(True)
plt.show()
