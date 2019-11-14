import pandas as pd
import datetime


def age(birthdate:str)->int:

    format_str = '%Y-%m-%d'
    birthday = datetime.datetime.strptime(birthdate, format_str)
    now = datetime.datetime.now()
    current_age = now - birthday
    current_age = round(current_age.days/365)
    return current_age


# Read the file into the dataframe
df = pd.read_csv('legislators.csv')

# Fill in null values with blank space
df = df.fillna('')

# Export the file of Republicans with YouTube and Twitter
df.query('party == "R" & youtube_url != "" & twitter_id != ""').to_csv('Republicans with Twitter and Youtube.csv', index=False)

# Create a new column called age
df['age'] = df.apply(lambda x: age(x['birthdate']), axis=1)

# Filter based on age
dems = df.query('party == "D" & age < 45')

# Remove the new column
dems.drop('age', axis=1)

# Export Democrats under 45
dems.to_csv('Democrats under 45.csv', index=False)