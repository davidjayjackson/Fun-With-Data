#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import sys

# Get the file name, X variable, and Y variable from the command line
file_name = sys.argv[1] 
x_variable = sys.argv[2]
y_variable = sys.argv[3]
z_variable = sys.argv[4] # kind of plot to make

# Read CSV file into a DataFrame
df = pd.read_csv(file_name)

# Plot the X and Y variables
plt.plot(df[x_variable], df[y_variable])
plt.xlabel(x_variable)
plt.ylabel(y_variable)
plt.title(f"{y_variable} vs {x_variable}")

# Show the plot
plt.show()
