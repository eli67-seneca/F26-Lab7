#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-23
# Purpose: Slice NumPy Arrays, Part II
# Usage: ./lab7d.py

import numpy as np

def main():
	# Creating a 2D NumPy array
	arr_2d = np.array([[10, 20, 30, 40, 50],[60, 70, 80, 90, 100],[110, 120, 130, 140, 150],[160, 170, 180, 190, 200]])

	# And then overwriting it programmatically; it's the same, I swear
	arr_2d = np.arange(10, 201, 10).reshape((4, 5))

	slice_1 = arr_2d[:2, -3:]
	print(f"First two rows & last three columns:\n{slice_1}")

	slice_2 = arr_2d[1:3, 1:3]
	print(f"The left-middle 2\u00d72 sub-array:\n{slice_2}")

	slice_3 = arr_2d[::2, ::2]
	print(f"Every other row and column:\n{slice_3}")

if __name__ == "__main__":
	main()