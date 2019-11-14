import pandas as pd
import datetime

# Read the file into the dataframe
df = pd.read_csv('legislators.csv')

# Fill in null values with blank space	
df = df.fillna('')

# Export the file of Republicans with YouTube and Twitter
df.query('party == "R" & youtube_url != "" & twitter_id != ""').to_csv('Republicans with Twitter and Youtube.csv', index=False)

# Create a new column called age
df['age'] = ''
format_str = '%Y-%m-%d'

# Populate the age value based on the birthdate
for d in df['birthdate']:
    birthday = datetime.datetime.strptime(d, format_str)
    now = datetime.datetime.now()
    age = now - birthday
    age = round(age.days/365)
    df.loc[df.birthdate == d, 'age'] = age
	
# Filter based on age
dems = df.query('party == "D" & age < 45')

# Remove the new column
dems.drop('age', axis=1)

# Export Democrats under 45
dems.to_csv('Democrats under 45.csv', index=False)