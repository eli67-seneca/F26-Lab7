#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-29 (Sorry, family matters)
# Purpose: Create Data Frames.
# Usage: ./lab7f.py

import pandas as pd

def main():
	fruits_list = [
		{"Apple": "Green", "Carrot": "Red", "Radish": "Purple"},
		{"Okra": "Thin", "Potato": "Blob", "Radish": "Round"},
		{"Apple": 2.1, "Okra": 3.5, "Carrot": 1.3, "Potato": 2.0, "Radish": 3.0}
	]

	df1 = pd.DataFrame(fruits_list)
	print(f"Naive DataFrame containerisation:\n{df1}\n")

	# We can do better than that, though.

	fruits_list = {
		"Color": {"Apple": "Green", "Carrot": "Red", "Radish": "Purple"},
		"Shape": {"Okra": "Thin", "Potato": "Blob", "Radish": "Round"},
		"Price": {"Apple": 2.1, "Okra": 3.5, "Carrot": 1.3, "Potato": 2.0, "Radish": 3.0}
	}

	df2 = pd.DataFrame(fruits_list)
	print(f"Actually useful DataFrame container:\n{df2}\n")

if __name__ == "__main__":
	main()