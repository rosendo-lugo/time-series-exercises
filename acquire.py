import pandas as pd
import requests


def download_data(url):
    response = requests.get(url)
    return response.content

def save_csv(data, filepath):
    with open(filepath, 'wb') as file:
        file.write(data)

def load_csv(filepath):
    return pd.read_csv(filepath)

def main():
    url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'
    filepath = 'open_power_sys.csv'

    # Download the data
    data = download_data(url)

    # Save the data to a CSV file
    save_csv(data, filepath)

    # Load the data from the CSV file
    ops_df = load_csv(filepath)

    # Display the first few rows of the DataFrame
    print(ops_df.head())

if __name__ == '__main__':
    main()