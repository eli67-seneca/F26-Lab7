#!/usr/bin/env python3
# Author: Enoch Li (eli67)
# Date: 2026-10-29
# Purpose: Create data frame from CSV file.
# Usage: ./lab7g.py
import pandas as pd
import matplotlib.pyplot as plot

def get_decade(year:int):
	return (year // 10) * 10

def main():
	movies = pd.read_csv('imdb_top_250.csv')

	print(f"Summary:\n{movies.describe()}\n")

	# Heads & Tails
	print(f"First ten entries:\n{movies.head(10)}\n")
	print(f"Last ten entries:\n{movies.tail(10)}\n")

	# Use operation on DF to print the year of earliest and latest movie
	print(f"The earliest movie:\t{movies['Year'].min()}")
	print(f"The latest movie:\t{movies['Year'].max()}\n")

	# All the genres
	genres = movies['Genre'].unique()
	print(f"List of genres:\n{genres}")

	# All the *unique* genres
	# Basically, this splits the genres by its own delimeter, explodes the list into
	# individual rows, strips all the whitespace, and then reports the unique values
	unq_genres = movies['Genre'].str.split('|').explode().str.strip().unique()
	print(f"List of individually unique genres:\n{unq_genres}\n")

	# Number of movies not made in the US
	columns = ["Title", "Origin"]
	not_in_US = movies[movies['Origin'] != 'USA'][columns]
	print(f"List of movies not made in the US:\n{not_in_US}\n")

	# Same problem
	#
	truly_intl = movies[~movies['Origin'].str.contains('USA', na=False)][columns]
	print(f"List of movies with no US involvement whatsoever:\n{truly_intl}\n")

	# The top ten highest-rated movies
	columns = ["Title", "IMDB rating"]
	highest_rated = movies.nlargest(10, columns="IMDB rating")[columns]
	print(f"Top Ten Highest-Rated Movies:\n{highest_rated}\n")

	# The best decade for movies according to this list.
	# To do that, add a `decade` column and calculate the decade for every entry
	movies['Decade'] = movies['Year'].apply(get_decade)

	# Now, group by decade, get the average, reset the index, and inputting the index for the highest one
	groupby_decade = movies.groupby("Decade")['IMDB rating'].mean().reset_index()
	best_decade = groupby_decade.loc[groupby_decade['IMDB rating'].idxmax()]	# type: ignore

	# It's the 1990s
	print(f"As it turns out, the best decade for movies is the {int(best_decade['Decade'])}s with an average rating of {best_decade['IMDB rating']:.2f}")

	# Now, to make a scatterplot
	plot.figure(figsize=(8, 5))
	plot.scatter(groupby_decade['Decade'], groupby_decade['IMDB rating'], color='blue', edgecolors='black', s=100)
	plot.title('Average IMDB Rating by Decade')
	plot.xlabel('Decade')
	plot.ylabel('Mean IMDB Rating')
	plot.grid(True)

	plot.show()
if __name__ == "__main__":
	main()

