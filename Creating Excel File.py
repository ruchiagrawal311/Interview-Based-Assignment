#!/usr/bin/env python
# coding: utf-8

# ### Write a program, which would download the data from the provided link, and then read the data and convert that into properly structured data and return it in Excel format.
# Note - Write comments wherever necessary explaining the code written.
#  
# 
# 
# 
# Link - https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json
# 
# 
# Data Attributes - id: Identification Number - int num: Number of the
# 
# ●	Pokémon in the official Pokédex - int name: Pokémon name -
# ●	string img: URL to an image of this Pokémon - string type:
# ●	Pokémon type -string height: Pokémon height - float
# 
# ●	weight: Pokémon weight - float candy: type of candy used to evolve Pokémon or given
# ●	when transferred - string candy_count: the amount of candies required to evolve
# - int
# ●	egg: Number of kilometers to travel to hatch the egg - float spawn_chance:
# ●	Percentage of spawn chance (NEW) - float avg_spawns: Number of this pokemon on 10.000 spawns (NEW) - int
# ●	spawn_time: Spawns most active at the time on this field. Spawn times are the same for all time zones and are expressed in local time. (NEW) - “minutes: seconds” multipliers: Multiplier of Combat Power (CP) for calculating the CP after evolution See below - list of int weakness: Types of
# ●	Pokémon this Pokémon is weak to - list of strings next_evolution: Number and Name of successive evolutions of Pokémon - list of dict prev_evolution: Number and Name of previous evolutions of Pokémon - - list of dict
# 

# pip install requests pandas openpyxl

# In[2]:


import requests
import pandas as pd

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
    for pokemon in data['pokemon']:
        attributes = {
            'id': pokemon['id'],
            'num': pokemon['num'],
            'name': pokemon['name'],
            'img': pokemon['img'],
            'type': ', '.join(pokemon['type']),
            'height': pokemon['height'],
            'weight': pokemon['weight'],
            'candy': pokemon.get('candy', ''),
            'candy_count': pokemon.get('candy_count', 0),
            'egg': pokemon.get('egg', ''),
            'spawn_chance': pokemon.get('spawn_chance', 0),
            'avg_spawns': pokemon.get('avg_spawns', 0),
            'spawn_time': pokemon.get('spawn_time', ''),
            'multipliers': ', '.join(map(str, pokemon.get('multipliers') or [])),
            'weakness': ', '.join(pokemon.get('weaknesses', []))
        }
        structured_data.append(attributes)
    return structured_data

# Function to save the data in Excel format
def save_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

# Main function to download, process, and save the data
def main():
    url = 'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json'
    filename = 'pokemon_data.xlsx'

    # Download the data
    data = download_data(url)

    # Process the data
    structured_data = process_data(data)

    # Save the data in Excel format
    save_to_excel(structured_data, filename)
    print(f'Data saved to {filename}')

# Run the main function
if __name__ == '__main__':
    main()

