# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 11:42:48 2024

@author: naiya
"""

#this goes w my obs final- this is me messing with the ATNF data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the ATNF Pulsar Catalogue Data
file_path = "C:/Users/naiya/Downloads/atf_data.txt"

# Load only the period and period deriv columns
column_names = ["ID", "P0", "Other1", "Other2", "P1", "Other6", "Other7"]
df = pd.read_csv(file_path, delim_whitespace=True, comment='#', names=column_names, usecols=[1, 4], na_values='*')
df.columns = ["Period (s)", "Period Derivative (s/s)"]

# taking out missing values
df.dropna(inplace=True)

# my lil gbt pulsar
your_pulsar_period = 0.004621  # Example: 4.621 ms in seconds
your_pulsar_pdot = 4.4528e-13  # Example: Period derivative

plt.figure(figsize=(10, 7))

# plot the ATNF pulsars
plt.scatter(df["Period (s)"], df["Period Derivative (s/s)"], s=20, color='black', label="ATNF Pulsars", alpha=0.7)

# highlight my pulsar
plt.scatter(your_pulsar_period, your_pulsar_pdot, color='red', s=50, label="GBT Pulsar", zorder=3)


plt.xscale("log")
plt.yscale("log")
plt.xlabel("Period (s)")
plt.ylabel("Period Derivative (s/s)")
plt.title("Pulsar Period vs. Period Derivative")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()
plt.show()


