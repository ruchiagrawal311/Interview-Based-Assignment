#!/usr/bin/env python
# coding: utf-8

# ### Write a program to download the data from the link given below and then read the data and convert the into the proper structure and return it as a CSV file.
# Link - https://data.nasa.gov/resource/y77d-th95.json
# 
# Note - Write code comments wherever needed for code understanding.
#  
# 
# Excepted Output Data Attributes
# 
# 
# ●	Name of Earth Meteorite - string id - ID of Earth
# ●	Meteorite - int nametype - string recclass - string
# ●	mass - Mass of Earth Meteorite - float year - Year at which Earth
# ●	Meteorite was hit - datetime format reclat - float recclong - float
# ●	point coordinates - list of int
# 

# In[1]:


import requests
import csv

# Function to download the data from the provided link
def download_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Error downloading data from {url}: {response.status_code}")

# Function to process the data and convert it into a structured format
def process_data(data):
    structured_data = []
    for meteorite in data:
        reclat = float(meteorite.get('reclat', 0))
        reclong = float(meteorite.get('reclong', 0))
        coordinates = [reclat, reclong] if reclat != 0 and reclong != 0 else []
        attributes = {
            'name': meteorite['name'],
            'id': meteorite['id'],
            'nametype': meteorite['nametype'],
            'recclass': meteorite['recclass'],
            'mass': float(meteorite.get('mass (g)', 0)),
            'year': meteorite.get('year', ''),
            'reclat': reclat,
            'reclong': reclong,
            'coordinates': coordinates
        }
        structured_data.append(attributes)
    return structured_data


# Function to save the data in CSV format
def save_to_csv(data, csv_filename):
    # Specify the field names for the CSV file
    field_names = ['name', 'id', 'nametype', 'recclass', 'mass', 'year', 'reclat', 'reclong', 'coordinates']

    # Write the data to a CSV file
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)

# Main function to download, process, and save the data
def main():
    url = 'https://data.nasa.gov/resource/y77d-th95.json'
    csv_filename = 'meteorite_data.csv'

    # Download the data
    data = download_data(url)

    # Process the data
    structured_data = process_data(data)

    # Save the data in CSV format
    save_to_csv(structured_data, csv_filename)
    print(f'Data saved to {csv_filename}')

# Run the main function
if __name__ == '__main__':
    main()

