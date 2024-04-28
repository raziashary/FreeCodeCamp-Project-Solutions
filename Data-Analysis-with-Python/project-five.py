import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as py
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('C:\\Belajar Kode\\FreeCodeCamp\\Data Analytics\\epa-sea-level.csv') 
    years = data["Year"]
    sea_level = data["CSIRO Adjusted Sea Level"]

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(years, sea_level, label='Sea Level')
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(years, sea_level)
    x_all = range(1880, 2051)  # Extend x-axis to include 2050
    plt.plot(x_all, intercept + slope * x_all, 'r', label='Line of Best Fit')

    # Create second line of best fit
    recent_data = data[data["Year"] >= 2000]
    recent_years = recent_data["Year"]
    recent_sea_level = recent_data["CSIRO Adjusted Sea Level"]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
        recent_years, recent_sea_level
    )
    x_recent = range(2000, 2051)
    plt.plot(x_recent, intercept_recent + slope_recent * x_recent, 'g', label='Line of Best Fit (2000)')

    # Add labels and title
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
