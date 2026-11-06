#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-23
# Purpose: Change Dimensions and create special arrays.
# Usage: ./lab7b.py

import numpy as np

def init():
	array1 = np.array([20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
					30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
					40, 41, 42, 43, 44, 45, 46, 47, 48, 49])
	array2 = np.array(range(20, 50))
	array3 = np.arange(1, 10).reshape((3, 3))
	months = ["January", "February", "March", "April", "May", "June",
			"July", "August", "September", "October", "November", "December"]
	array4 = np.array(months).reshape((2, 3, 2))

	# Reshaping array1 and array2
	array1 = array1.reshape((5, 6))
	array2 = array2.reshape((2, 3, 5))
	print(f"Reshaped array1 and array2:\n{array1}\n{array2}")

	# Adding array5, which is a matrix with custom diagonal values
	array5 = np.diag([45, 7, 61, 8, 9])
	print(f"array5:\n{array5}")

	# Adding array6, which is a 7x7 matrix with values sampled from a normal distribution
	array6 = np.random.rand(7, 7)
	print(f"array6:\n{array6}")

if __name__ == "__main__":
	init()

