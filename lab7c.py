#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-23
# Purpose: Slice NumPy Arrays.
# Usage: ./lab7c.py

import numpy as np

def main():
	# Here's an array of a hundred random integers between 0 and 100
	numArray = np.random.randint(0, 100, (100,))

	first_10_values = numArray[:10]
	print(f"First 10 values:\n{first_10_values}\n")

	last_10_values = numArray[-10:]
	print(f"Last 10 values:\n{last_10_values}\n")

	thirty_values_from_21 = numArray[21:21+30]
	print(f"30 values from index 21:\n{thirty_values_from_21}\n")

	numArray[50:65] = 101
	print(f"Indexes 50 to 65 overwritten with 101:\n{numArray}\n")

if __name__ == "__main__":
	main()
