# PRG101-Lab7
### Submission Details

In this lab, you will create eight simple scripts. Write the scripts in Jupyter Notebook or Codespaces.
Please note that you must complete the lab during class hours and show your progress to the professor to receive the marks for the lab.

### Lab Objectives

- To be able to create and use arrays in NumPy.
- To be able to create and use series and data frames in Pandas.

## INVESTIGATION 1: CREATING AND USING ARRAYS IN NumPy

NumPy is a Python library implemented in C language for creating and manipulating data in large arrays at speed. In the slides you saw different ways of creating arrays and initializing them. This lab deals with testing your understanding of those methods discussed in the slides.

### lab7a.py
#### Creating Arrays 

NumPy, provides an array object similar to a list in Python but with added functionality for numerical operations.
```Python
import numpy as np  # Step 1: Import NumPy

# Creating a 1D array using a Python list
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:\n", arr1)

# Creating a 2D array using a nested Python list
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
print("3D Array:\n", arr3d)
```

- In your lab10a.py file write code to show two different ways of creating a NumPy array that has integer values from 20 to 49 (including both as well). Save them in two different variables: array1 and array2.
- Write code that will create a 3x3 matrix and should have values 1 to 9 arranged in 3 rows and three columns. Save it in variable: array3.
- Write code to create a 3D matrix of shape 2x3x2 and initialize with month names. Save it in variable: array4.
- Run your script using the command: python ./lab7a.py.
- Take screenshot of code and output and add them in a document to be exported as pdf.

### lab7b.py
#### Changing Dimensions and creating special arrays

The `np.reshape` function allows you to change the shape of an existing array without altering its data.
```Python
import numpy as np

# Original array (1D)
arr = np.arange(1, 13)
print("Original 1D Array:", arr)

# Reshape to 2D (3x4)
arr_2d = np.reshape(arr, (3, 4))
print("\nReshaped to 2D Array (3x4):\n", arr_2d)

# Reshape to 3D (2x3x2)
arr_3d = np.reshape(arr, (2, 3, 2))
print("\nReshaped to 3D Array (2x3x2):\n", arr_3d)
```

Flattening an array means converting it from multi-dimensional to a 1D array using the ravel or flatten method.
```Python
# Flatten the 2D array back to 1D
arr_flattened = arr_2d.ravel()  # or use arr_2d.flatten()
print("\nFlattened Array:", arr_flattened)
```

The `np.eye` function creates an identity matrix, which is a square matrix with ones on the diagonal and zeros elsewhere.
```Python
# Identity matrix of size 3x3
identity_matrix = np.eye(3)
print("\nIdentity Matrix (3x3):\n", identity_matrix)
```

The `np.diag` function creates a diagonal matrix, where the specified values appear on the diagonal.
```Python
# Diagonal matrix with specified diagonal elements
diagonal_matrix = np.diag([10, 20, 30])
print("\nDiagonal Matrix:\n", diagonal_matrix)
```

NumPy provides functions like np.random.rand, np.random.randn, and np.random.randint to create arrays filled with random values.
```Python
# Array with random values from a uniform distribution [0, 1)
random_array = np.random.rand(3, 3)  # 3x3 array
print("\nRandom Array (Uniform distribution):\n", random_array)

# Array with random values from a normal distribution
random_normal_array = np.random.randn(3, 3)  # 3x3 array
print("\nRandom Array (Normal distribution):\n", random_normal_array)

# Array with random integers between 0 and 10
random_int_array = np.random.randint(0, 10, (3, 3))  # 3x3 array
print("\nRandom Integer Array (0 to 10):\n", random_int_array)
```

- Copy the code from your lab8a.py file and paste in lab7b.py file.
- Write code that changes array1 to 5x6 shape (5 rows, 6 columns) and reshapes array2 to a 2x3x5 (a 3D matrix).
- Create NumPy matrix called array5 that has 5 rows and 5 columns and initialize diagonal values to (45, 7, 61, 8, 9) and rest of the values should be zeros.
- Create a NumPy 7x7 matrix called array6 and initialize with values sampled from a normal distribution.
- Run the program using command python ./lab7b.py for both test cases.

### lab7c.py
#### Slicing NumPy Arrays

Slicing in NumPy allows you to access and manipulate subsets of an array's elements. It's similar to slicing lists in Python, but with more functionality due to NumPy's multi-dimensional array capabilities.
```Python
import numpy as np

# Creating a 1D NumPy array
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print("Original 1D Array:", arr)

# Slicing elements from index 1 to 5 (exclusive)
slice_1 = arr[1:5]
print("\nSliced 1D Array (arr[1:5]):", slice_1)

# Slicing elements from the beginning to index 4 (exclusive)
slice_2 = arr[:4]
print("\nSliced 1D Array (arr[:4]):", slice_2)

# Slicing elements from index 3 to the end
slice_3 = arr[3:]
print("\nSliced 1D Array (arr[3:]):", slice_3)

# Slicing with a step of 2
slice_4 = arr[::2]
print("\nSliced 1D Array with Step 2 (arr[::2]):", slice_4)
```

Slicing in 2D arrays is done by specifying slices for each dimension.
```Python
# Creating a 2D NumPy array
arr_2d = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]])
print("\nOriginal 2D Array:\n", arr_2d)

# Slicing a subarray (first two rows, first three columns)
sub_array_1 = arr_2d[:2, :3]
print("\nSliced 2D Array (arr_2d[:2, :3]):\n", sub_array_1)

# Slicing all rows but only the last two columns
sub_array_2 = arr_2d[:, -2:]
print("\nSliced 2D Array (arr_2d[:, -2:]):\n", sub_array_2)

# Slicing the last two rows and last two columns
sub_array_3 = arr_2d[-2:, -2:]
print("\nSliced 2D Array (arr_2d[-2:, -2:]):\n", sub_array_3)
```

- In your lab7c.py file, create a 1D array numArray and initialize it with 100 random numbers and do following:
  - Slice and print first 10 values.
  - Slice and print last 10 values.
  - Slice and print 30 values starting from index 21.
  - With one statement, change all values to 101 from index 50 to 65.
- Run the program using the command python ./lab7c.py.

### lab7d.py
#### Slicing 2D NumPy Arrays

- Create the given array in your lab7d.py file :
```Python
# Creating a 2D NumPy array
arr_2d = np.array([[10, 20, 30, 40, 50],[60, 70, 80, 90, 100],[110, 120, 130, 140, 150],[160, 170, 180, 190, 200]])
```
- Perform the following operations on this array :
  - Slice the first two rows and the last three columns of arr_2d. Store the result in a variable called slice_1.
  - Extract the middle 2x2 subarray (elements 70, 80, 120, 130) from arr_2d and store it in a variable called slice_2.
  - Slice every other row and every other column from arr_2d. Store the result in a variable called slice_3.

## INVESTIGATION 2: CREATING AND USING SERIES AND DATA FRAMES FROM Pandas

### lab7e.py
#### Creating Series 

In pandas, a Series is a one-dimensional labeled array capable of holding any data type (integer, string, float, Python objects, etc.). The labels (index) are used to access the data. Series is like a column in a DataFrame or a single dimension of data in an array.
```Python
import pandas as pd

# Creating a Series from a list
data_list = [10, 20, 30, 40, 50]
series_from_list = pd.Series(data_list)
print("Series from List:\n", series_from_list)
```

You can specify a custom index for the Series using:
```Python
pd.Series(data_list, index=['a', 'b', 'c', 'd', 'e'])
```

- Import pandas module in your lab7e.py file.
- Create a series with values "<50", "50-59", "60-69", "70-79", "80-89", "90-100" and corresponding index names as "F", "D", "C", "B", "A", "A+". Print this series on screen.
- Write code to print the values of indices "C" and "A+".
- Write code to print value "60-69" directly without printing its index name.
- Write code to show the * operation on this list
- Run your script using the command python ./lab7e.py.

### lab7f.py
#### Creating Data Frames

A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types, similar to a spreadsheet or SQL table.
```Python
import pandas as pd  # Step 1: Import Pandas

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

# Step 2: Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame created from dictionary:\n", df)
```

- In your lab8f.py file, using pandas create and print a data frame from the following dictionaries.
  - {"Apple": "Green", "Carrot": "Red", "Radish": "Purple"}
  - {"Okra": "Thin", "Potato": "blob", "Radish": "Round"}
  - {"Apple": 2.1, "Okra": 3.5, "Carrot": 1.3, "Potato": 2.0, "Radish": 3.0}
- Using Pandas create a data frame that looks like in the image dataframe.jpg file.
- Run your script using the command python ./lab7f.py.

### lab7g.py
#### Data Frames and CSV files

CSV (Comma-Separated Values) files are widely used for storing tabular data. Pandas provides simple functions to read from and write to CSV files.
To read a CSV file into a DataFrame, you can use the pd.read_csv function.
```Python
# Reading data from a CSV file
df_from_csv = pd.read_csv('sample.csv')  # Replace 'sample.csv' with your file path
print("\nDataFrame from CSV:\n", df_from_csv)
```

`head()` and `tail()` allow you to quickly view the first or last few rows of a DataFrame.
```Python
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

# Viewing the first few rows
print("First 3 rows:\n", df.head(3))

# Viewing the last few rows
print("\nLast 2 rows:\n", df.tail(2))
```

You can select one or more columns from a DataFrame.
```Python
# Selecting a single column
ages = df['Age']
print("\nAges:\n", ages)

# Selecting multiple columns
name_city = df[['Name', 'City']]
print("\nNames and Cities:\n", name_city)
```

Use `loc[]` for label-based indexing and `iloc[]` for integer-based indexing.
```Python
# Selecting a row by label/index
row_2 = df.loc[2]  # Selects the row with index label 2
print("\nRow with index 2:\n", row_2)

# Selecting multiple rows by integer position
rows_1_3 = df.iloc[1:4]  # Selects rows from index 1 to 3 (4 is exclusive)
print("\nRows 1 to 3:\n", rows_1_3)
```

To get a summary of the data, you can use the describe() method. It provides statistics like mean, standard deviation, minimum, and maximum values for numerical columns.
```Python
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 22],
    'Salary': [70000, 80000, 90000, 100000, 65000]
}
df = pd.DataFrame(data)

# Summary statistics
summary = df.describe()
print("Summary Statistics:\n", summary)
```

To get the unique values in a column, use the unique() method. This is particularly useful for categorical data.
```Python
# Unique values in the 'Name' column
unique_names = df['Name'].unique()
print("\nUnique Names:\n", unique_names)

# Unique values in the 'Age' column
unique_ages = df['Age'].unique()
print("\nUnique Ages:\n", unique_ages)
```

To count the number of occurrences of each unique value in a column, use the value_counts() method.
```Python
# Count of occurrences for each unique value in the 'Age' column
age_counts = df['Age'].value_counts()
print("\nValue Counts for Age:\n", age_counts)

# Count of occurrences for each unique value in the 'Name' column
name_counts = df['Name'].value_counts()
print("\nValue Counts for Name:\n", name_counts)
```

- In your lab7g.py file, create a new data frame from a csv file located in : https://github.com/itiievskyi/IMDB-Top-250/blob/master/imdb_top_250.csv.
- Using Pandas, perform the following operations: 
  - Print summary of the data contained in data frame
  - Print first 10 and last 10 rows of this data frame.
  - Using operation on data frame print the year of earliest and latest movie (hint: min function on year column).
  - Print unique values in the "Genre" column.
  - Count how many moves are not made in USA.
  - Find top 10 Highest-Rated Movies.
  - Find out what the best decade of movies is. Also display using a scatter plot.
  - You can follow the steps.
          1. First define a python function that gets the decade from the year
          2. Add a decade column to the dataframe.
          3. group by decade to get the mean rating for each decade
          4. Create a scatterplot using MATPLOT.
   


- Run your script using the command python ./lab7g.py.

## INVESTIGATION 3: PLOTTING DATA WITH Matplotlib

### lab7h.py
#### Creating Histograms

Histograms are a type of plot used to represent the distribution of numerical data. They are particularly useful for visualizing the frequency of data within different bins or intervals. In Python, histograms can be created using the `matplotlib` library, which provides various functions for plotting and customizing histograms.
To create a histogram using Matplotlib, you primarily use the `plt.hist()` function.
```Python
import matplotlib.pyplot as plt
import numpy as np

# Generating random data
data = np.random.randn(1000)  # 1000 random values from a normal distribution

# Creating the histogram
plt.hist(data, bins=30, edgecolor='black', alpha=0.7)

# Adding titles and labels
plt.title('Histogram of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Displaying the plot
plt.show()
```

You can customize histograms in various ways:
```Python
# Creating a histogram with customization
plt.hist(data, bins=20, color='skyblue', edgecolor='black', alpha=0.8, density=True)

# Adding titles and labels
plt.title('Customized Histogram')
plt.xlabel('Value')
plt.ylabel('Probability Density')

# Adding grid lines for better readability
plt.grid(True)

# Displaying the plot
plt.show()
```
`color`: Sets the color of the bars.
`density`: If True, the histogram displays the probability density instead of raw counts. This scales the histogram so that the area under the histogram sums to 1.
`grid`: Adds grid lines to the plot for better readability.

- In your lab7h.py file, import pandas and matplotlib modules.
- Using pandas and matplotlib draw a histogram of the data from movies database file given in activity 6 above.
- Perform the following operations:
  - Copy Year column in a new series.
  - Sort years data in ascending order.
  - Process this sorted years data to find unique year and number of times a year occurs (this is essentially number of movies for that year in this file).
  - Draw a histogram with X-axis as the years and bar height equal to corresponding count. If number of unique years is very large only display histogram for first 10 years.
- Run your script using the command python ./lab7h.py.

## lab7 Sign-Off
- Submit the screenshots of each individual script in the form of a pdf, the screenshot must show your scripts and command line interface and output.
- The screenshot must also show your username on github codespaces.
- Submit pdf of the screenshots of the following scripts on blackboard. If the screenshots do not correctly show the information mentioned above, you will get zero marks for the lab.
    - lab7a.py
    - lab7b.py
    - lab7c.py
    - lab7d.py
    - lab7e.py
    - lab7f.py
    - lab7g.py
    - lab7h.py
