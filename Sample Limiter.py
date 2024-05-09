import pandas as pd

df = pd.read_csv('trout.csv')

female_data = df[df['Sex'] == 'Female']
male_data = df[df['Sex'] == 'Male']

female_rows_to_remove = len(female_data) - 300
male_rows_to_remove = len(male_data) - 300

female_rows_to_remove_indices = female_data.sample(n=female_rows_to_remove, random_state=42).index
male_rows_to_remove_indices = male_data.sample(n=male_rows_to_remove, random_state=42).index

df = df.drop(female_rows_to_remove_indices, axis=0)
df = df.drop(male_rows_to_remove_indices, axis=0)

df.to_csv('edited_data.csv', index=False)