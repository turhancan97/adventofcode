# Read calories.csv with pandas and index

import pandas as pd
df = pd.read_csv('calories.csv', index_col=0)

# Find the three elves who ate the most and sum their calories
df = df.sort_values(by='Calories', ascending=False)
print(df.head(3))
print(df.head(3)['Calories'].sum())
