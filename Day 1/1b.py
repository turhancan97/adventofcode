# Read calories.csv with pandas and index

import pandas as pd
df = pd.read_csv('calories.csv', index_col=0) # Read the csv file and set the index column to 0

# Find the three elves who ate the most and sum their calories
df = df.sort_values(by='Calories', ascending=False) # Sort the dataframe by calories
print(df.head(3)) # Print the first 3 rows
print(df.head(3)['Calories'].sum()) # Print the sum of the first 3 rows
