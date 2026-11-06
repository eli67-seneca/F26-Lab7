#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-23
# Purpose: Create Arrays.
# Usage: ./lab7a.py

import numpy as np

def main():
	# You can use lists, but the `array` function can cast just about any list-like
	# structure into an numpy array.
	array1 = np.array([20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
					30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
					40, 41, 42, 43, 44, 45, 46, 47, 48, 49])
	array2 = np.array(range(20, 50))

	# Normally, it's list comprehension to the rescue:
	dim = (3, 3)
	x, y = dim
	array3 = np.array([[(row * col) + col + 1 for col in range(y)] for row in range(x)])

	# And that is technically a valid solution, but this being NumPy:
	array3 = np.arange(1, 10).reshape(dim)

	# All the months
	months = ["January", "February", "March", "April", "May", "June",
			"July", "August", "September", "October", "November", "December"]
	array4 = np.array(months).reshape((2, 3, 2))

	arrays = [array1, array2, array3, array4]
	for i in range(len(arrays)):
		print(f"array{i}:\n{arrays[i]}")

if __name__ == "__main__":
	main()

