import pandas as pd # Import pandas

dicts = dict() # Create a dictionary to store the data
elves_number = 0 # Create a variable to store the number of elves
calories = 0 # Create a variable to store the calories

# ✅ check if a line is NOT empty
with open('calories.txt', 'r', encoding="utf-8") as f: # Open the file
    lines = f.readlines() # Read the lines

    for line in lines: # For each line
        if line.strip(): # If the line is NOT empty
            calories += int(line) # Add the calories to the variable
            print('The line is NOT empty ->', line)
        else: # If the line is empty 
            elves_number += 1 # Add 1 to the number of elves
            dicts[f'Elves {elves_number}'] = calories # Add the calories to the dictionary
            calories = 0 # Reset the calories
            print('The line is empty')

# convert dictionary with elves and their calories to dataframe
df = pd.DataFrame.from_dict(dicts, orient='index', columns=['Calories']) # Create a dataframe from the dictionary

#print the maximum calories and the elves who ate the most
print(df)
print(df['Calories'].max())
print(df[df['Calories'] == df['Calories'].max()].index[0]) 

# save df as csv
df.to_csv('calories.csv')
