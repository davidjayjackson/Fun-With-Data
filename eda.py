#!/usr/bin/python3.8

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_csv(filename, date_column_name=None):
    df = pd.read_csv(filename)
    if date_column_name:
        df[date_column_name] = pd.to_datetime(df[date_column_name])
        df.set_index(date_column_name, inplace=True)
    return df

filename = sys.argv[1]
column_name = sys.argv[2]
date_column_name = sys.argv[3] if len(sys.argv) > 3 else None

df = read_csv(filename, date_column_name)
column = df[column_name].dropna()

print("Number of non-NA values:", len(column))
print("Mean:", column.mean())
print("Standard deviation:", column.std())
print("Minimum:", column.min())
print("25th percentile:", np.percentile(column, 25))
print("Median:", np.median(column))
print("75th percentile:", np.percentile(column, 75))
print("Maximum:", column.max())
print("Interquartile range:", np.percentile(column, 75) - np.percentile(column, 25))
print("Data types:")
print(df.dtypes)
print("Describe:")
print(df.describe())

plt.figure()
df.plot(y=column_name, kind='line', figsize=(10, 5))
plt.xlabel('Year')
plt.ylabel(column_name)
plt.title('Line plot of ' + column_name)
plt.tight_layout()
plt.savefig('lineplot.png')

plt.figure()
df[column_name].plot(kind='box', vert=False, figsize=(10, 5))
plt.title('Box plot of ' + column_name)
plt.tight_layout()
plt.savefig('boxplot.png')

plt.figure()
df[column_name].plot(kind='hist', figsize=(10, 5))
plt.xlabel(column_name)
plt.ylabel('Frequency')
plt.title('Histogram of ' + column_name)
plt.tight_layout()
plt.savefig('histogram.png')

plt.show()

