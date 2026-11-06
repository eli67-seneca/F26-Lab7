#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-24
# Purpose: Create Series.
# Usage: ./lab7e.py

import pandas as pd

def main():
	grades = ["F", "D", "C", "B", "A", "A+"]
	values = ["<50", "50-59", "60-69", "70-79", "80-89", "90-100"]
	pd_grades = pd.Series(data=values, index=grades)
	
	print(f"Series from List:\n{pd_grades}")

	print("\nPrints A+ and C onto the screen:")
	print(f"A+ {pd_grades['A+']}\nC {pd_grades['C']}")

	print("\nPrints the value '60-69' directly:")
	print(f"{pd_grades.index[2]}")

	print("\nUsing the unpack operator (*):")
	print(*pd_grades)
	print("\nAnd on its index:")
	print(*pd_grades.index)

if __name__ == "__main__":
	main()
