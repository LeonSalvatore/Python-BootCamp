
import json
import csv
from pprint import pprint


laureats_ref = 'laureates.csv'
reading_mode = "r"
wrting_mode = "w"

# `r`stans for read mode
# `w` stands for write mode
# `a` stands for append mode
# `x` stands for exclusive creation, failing if the file already exists
# `b` stands for binary mode
# `t` stands for text mode
# `+` stands for read and write mode
with open(laureats_ref, reading_mode) as file:
    # Read CSV file
    reader = csv.DictReader(file)
    # create a list of dictionaries
    laureates = list(reader)
  
    # Print the list of dictionaries
    pprint(laureates)
    
with open('laureates.json', wrting_mode) as json_file:
        # Convert the list of dictionaries to JSON
     json_data = json.dumps(laureates, indent=2)
     json_file.write(json_data)
       
        # Print the JSON data
#print(json_data)

laureates_beggining_with_a = []
# Function to filter laureates by name starting with 'A'
def filter_laureates_by_name_a():
    for lareate in laureates:
        # Check if the name contains 'A'
        if lareate['name'][0] == 'A':
            # Print the laureate's name
            laureates_beggining_with_a.append(lareate)
            print(laureates_beggining_with_a)
    # Filter the list of dictionaries by name
    #with open(laureats_ref, wrting_mode) as file:
        
    return laureates_beggining_with_a
    
    
filter_laureates_by_name_a()
   