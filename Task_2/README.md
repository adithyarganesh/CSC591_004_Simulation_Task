# CSC591_IOT_Analytics_Simulation_Task_2

# Important Information
All the code was run from on eos after installing pip and the pandas library.

# Description
The code to perform simulation of real and non-real time signals has been implemented and the results got both are generated and saved in two separate CSV files namely 
- Result_Task2-1.csv
- Result_Task2-2.csv

Here, the two simulations (normal and swapped values) have been tabulated one below the other after leaving two lines of space

# Instructions

First, add pip access in the eos so that we can install the required libraries and then install the pandas library for file generation.

Commands:

    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    pip install pandas

Once the three commands have been successfully run, we can go ahead with the implementation

# Implementation
The code is implemented in a single script called SimulationTask2.py. This code will be
called as follows:

    python SimulationTask2.py 

# Results
All the results have been analysed and the analysis metrics have been saved in separate CSV files for verification

# Issues
pip/ pip3 based on Python usage 
Since both the tasks use the same script, two separate files have not been created and instead two output files are generated separately for each task when the script is run.