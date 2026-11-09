#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-30
# Purpose: Create Histograms.
# Usage: ./lab7h.py
import pandas as pd
import matplotlib.pyplot as plot
import sys
from pandas import Index, Series

movies = pd.read_csv("imdb_top_250.csv")

def get_years(years:int=10):
	# Copy Year column into a new series and sort in asc order
	sorted_years = movies['Year'].copy().sort_values()
	print(f"Copy and sort year column:\n{sorted_years.head(10)}\n")

	# Find unique years and number of times each year occurs
	year_counts = sorted_years.value_counts().sort_index()
	print(year_counts.head(10))

	# Since the dataset spans nearly a century, the number of unique years is indeed very large (83).
	# By default args, it will display the first 10 unique years.
	unique_years = year_counts.index[:years]

	# Filter original sorted Series to include only unique_years
	filtered_years = sorted_years[sorted_years.isin(unique_years)]
	return filtered_years

def main():
	if len(sys.argv) > 1:
		year_range = int(sys.argv[1])
		years = get_years(year_range)
	else:
		year_range = int(10)
		years = get_years()

	year_range = max(1, min(83, year_range))
	bin_range = range(int(years.min()), int(years.max() + 2))
	title = f"Number of Top Movies for {f'the First {year_range}' if year_range != 83 else ' All '} Unique Years"

	plot.figure(figsize=(16, 8))
	plot.hist(years, bins=bin_range, edgecolor='black', color='#4080FF')
	plot.title(title)

	plot.xlabel("Year")
	plot.xticks(years, rotation='vertical')
	plot.ylabel("Number of Movies")
	plot.grid(axis='y', linestyle='--', alpha=0.7)

	plot.show()

if __name__ == "__main__":
	main()
