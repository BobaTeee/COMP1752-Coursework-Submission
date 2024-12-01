import os
import csv
from library_item import LibraryItem

library = {}
def load_library():
    global library
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, 'trackplaylist.csv')
    try:
        with open(csv_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                key = str(row['id']).zfill(2)  
                library[key] = LibraryItem(
                    str(row['name'].strip()),
                    str(row['artist'].strip()),
                    int(row['rating']),
                )
                library[key].play_count = int(row['playcount'])
    except FileNotFoundError:
        print("CSV file not found")
        return False
    return True

load_library()

def list_all():
    output = ""
    for key in sorted(library.keys(), key=int):  
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output
def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None

def get_artist(key):
    try:
        item = library[key]
        return item.artist
    except KeyError:
        return None

def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1

def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1

def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return -1

def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return