# Introduction
This code uses the [Mastik Framework](https://github.com/0xADE1A1DE/Mastik) as a base to run Side Channel Attack on L1 Cache of Intel x86 x64 based CPU, the testing is also done on AMD x86 x64 CPU and the Framework is able to analyse the L1 cache but is not producing required results, the original creator used AES encryption and analyse the data access pattern and find out the original data by just observing the L1 data access patterns.

# How to run the code
## System Requirements:
- `Linux x86_64`
- `RAM: 4GB`
- `HDD: 10GB`
- `Intel CPU x86_64 preferred`
- `Admin Privileges to Run the L3 cache access`
- `Numpy installed in python used to visualise the text file generated later`

## How to test L1 cache access:
The code is precompiled so need to run only the files directly,
- `./testl1` this is produce a long output of 100 lines of number which is the data access pattern,
- Use `./testl1 > text.txt` to take the output in a text file and later analyse it, these outputs can be viewed in the 'Outputs' folder and Visualisation for the same can be seen
in the 'Figures' folder, it is divided as per each CPU

## How to test L1i cache access:
- `./testl1i` This will again produce a large 100 lines of numbers of data access pattern
- `./tesl1i > text.txt` use this to store the output in file and analyse it later

## How to test L3 cache access:
- `sudo ./testl3 /dev/zero` this will produce an output of number of sets of memory analysed as well as the lines as per earlier
- `sudo ./testl3 /dev/zero > text.txt` this is used to store data in a text file and analyse it later

## How to run RSA experiment:
- `./test4096` this will generate the data access pattern
- `./test4096 > text.txt` to store the data in a text file and analyse it later

## How to run AES experiment:
- `./testaes` use this to run AES and run Prime Probe attack on the L1 cache and generate a guess of the original data while the encryption is running and guess the original data which is being encrypted, the code will generate a heatmap in the console itself and give a approximate guess of the original data.

## How to Visulise the Text file:
Use the python code under 'Load & Visualisation Code' to visualise the text data, use the `visualise_L1.py` to generate the graphs for L1 and RSA experiment, use `visualise_L3.py` to generate the graphs for L3 cache.

## Implement Load on the cache:
Use the `cache_access.py` to generate load on L1 and L3 cache and generate a data access pattern
