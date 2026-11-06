#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-30
# Purpose: Create Histograms.
# Usage: ./lab7h.py
import pandas as pd
import matplotlib.pyplot as plot

movies = pd.read_csv('imdb_top_250.csv')

def main():
	# Copy Year column into a new series and sort it in asc order
	sorted_years = movies['Year'].copy().sort_values()
	print(f"Copy and sort year column:\n{sorted_years.head(10)}\n")

	# Find unique years and the number of times each year occurs
	year_counts = sorted_years.value_counts().sort_index()
	print(year_counts.head(10))

	# "If number of unique years is very large display histogram for first 10 years"
	# Since this dataset spans nearly a century, the number of unique years is very large.
	# So I have to slice the first 10 unique years from our sorted data.
	all_unq_years = year_counts.index
	first_10_unq_years = all_unq_years[:10]

	# Filter original sorted Series to include only data from first 10 unique years
	filtered_years = sorted_years[sorted_years.isin(first_10_unq_years)]

	# Render histogram with MatPlotLib
	plot.figure(figsize=(10, 5))

	# Set bins to match exact number of unique years plus one to line up all the bars
	bin_range = range(int(first_10_unq_years.min()), int(first_10_unq_years.max() + 2))
	plot.hist(filtered_years, bins=bin_range, edgecolor='black', color='purple')

	plot.title("Number of Top Movies for the First 10 Unique Years")
	plot.xlabel("Year")
	plot.ylabel("Number of Movies")
	plot.xticks(first_10_unq_years)	# Ensures only 10 target years are labelled
	plot.grid(axis='y', linestyle='--', alpha=0.7)

	plot.show()

if __name__ == "__main__":
	main()

# TO DO 1: Import pandas and matplotlib modules.
# TO DO 2: Draw histogram of the data from movies database.
# TO DO 3: Perform the operations provided in readme.md file on this data.
# TO DO 4: Run the script.

