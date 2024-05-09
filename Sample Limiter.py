import pandas as pd # Import the library nessecary to edit csv files

df = pd.read_csv('trout.csv') # Import the csv file, change this to you file name

# Assign the gender categories a variable
female_data = df[df['Sex'] == 'Female']
male_data = df[df['Sex'] == 'Male']

# Limit the sample size to 300
female_rows_to_remove = len(female_data) - 300
male_rows_to_remove = len(male_data) - 300

 # Create a new variable to randomly remove the unnecessary rows
female_rows_to_remove_indices = female_data.sample(n=female_rows_to_remove, random_state=42).index
male_rows_to_remove_indices = male_data.sample(n=male_rows_to_remove, random_state=42).index

# Remove the rows
df = df.drop(female_rows_to_remove_indices, axis=0)
df = df.drop(male_rows_to_remove_indices, axis=0)

# Save to a new file, change name to whatever you want
df.to_csv('edited_data.csv', index=False)
