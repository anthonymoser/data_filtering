import csv
import datetime


def get_data(filename:str)->list:

    data = []
    with open(filename) as csvfile:
        readCSV = csv.DictReader(csvfile)
        for row in readCSV:
            row = {k: row[k] for k in row.keys()}
            data.append(row)

    return data


def include(data:list, field:str, value:any)->list:

    response = [d for d in data if d[field] == value]
    return response


def exclude(data:list, field:str, value:any)->list:

    response = [d for d in data if d[field] != value]
    return response


def age(birthdate:str)->int:

    format_str = '%Y-%m-%d'
    birthday = datetime.datetime.strptime(birthdate, format_str)
    now = datetime.datetime.now()
    current_age = now - birthday
    current_age = round(current_age.days/365)
    return current_age


def export_csv(filename:str, data:list):

    try:
        with open(filename, 'w', newline='') as csvfile:

            fieldnames = [k for k in data[0].keys()]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for d in data:
                writer.writerow(d)

        print("Exported file " + filename)

    except Exception as e:
        print("Error exporting file: ", e)


def main():

    # Import initial file
    legislators = get_data('legislators.csv')

    # Filter and export Republicans with Twitter and YouTube accounts
    republicans = include(legislators, field='party', value='R')
    republicans = exclude(republicans, field='twitter_id', value= '')
    republicans = exclude(republicans, field='youtube_url', value='')
    export_csv('Republicans with Twitter and YouTube Accounts.csv', republicans)

    # Filter and export Democrats under the age of 45
    dems = include(legislators, field='party', value='D')
    dems = [d for d in dems if age(d['birthdate']) < 45]
    export_csv('Democrats Under 45.csv', dems)

main()
