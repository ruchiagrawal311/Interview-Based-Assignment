#!/usr/bin/env python
# coding: utf-8

# ### Write a program to download the data from the given API link and then extract the following data with proper formatting
# 
# 
# Link - http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes
# 
# Note - Write proper code comments wherever needed for the code understanding
# 
# Excepted Output Data Attributes -
# ●	id - int url - string
# ●	name - string season
# ●	- int number - int
# ●	type - string airdate -
# ●	date format airtime -
# ●	12-hour time format
# ●	runtime - float
# ●	average rating - float
# ●	summary - string
# ●	without html tags
# ●	medium image link - string
# ●	Original image link - string
# 
# 

# In[1]:


import requests
import json

# Function to download data from the API
def download_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Error downloading data from {url}: {response.status_code}")

# Function to process the data and extract the desired attributes
def process_data(data):
    # Print the downloaded data for inspection
    print(json.dumps(data, indent=4))

    # Extract the desired attributes
    extracted_data = {
        'id': data['id'],
        'url': data['url'],
        'name': data['name'],
        'season': data['season'],
        'number': data['number'],
        'type': data['type'],
        'airdate': data['airdate'],
        'airtime': data['airtime'],
        'runtime': data['runtime'],
        'average_rating': data['rating']['average'],
        'summary': data['summary'],
        'medium_image': data['image']['medium'],
        'original_image': data['image']['original']
    }

    return extracted_data

# Main function to download, process, and print the extracted data
def main():
    url = 'http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes'

    # Download the data
    data = download_data(url)

    # Process the data and extract the desired attributes
    extracted_data = process_data(data['_embedded']['episodes'][0])

    # Print the extracted data
    print(json.dumps(extracted_data, indent=4))

# Run the main function
if __name__ == '__main__':
    main()


# In[ ]:




