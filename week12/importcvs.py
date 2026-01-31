#We wish to create a program that reads data from a CSV file.
#The file name is data.csv.
#The program should start by opening the CSV file.
#The program should then read the headings from the CSV file and store these in suitable variable.
#The program should then read each record from the file and display it.
#The program should suitably close the file and handle errors that occur when the reading the file.
#Order the following lines of code so that they create a program that satisfies the above description:
#1 
import csv                         # Import the csv module to work with CSV files

csv_file = "data.csv"              # Store the name/path of the CSV file

with open(csv_file) as src:        # Open the CSV file safely using a with statement
    data = csv.reader(src)         # Create a CSV reader object to read the file
    headings = next(data)          # Read and store the header row from the CSV file
    for record in data:            # Loop through each remaining row in the CSV file
        print(record)              # Print each row (record) to the screen

#2 
import json   
                            # Import the json module to work with JSON files
file_path = "countries.json"              # Store the path to the JSON file

with open(file_path) as file:              # Open the JSON file safely using a with statement
    data = json.load(file)                 # Load the JSON data from the file into a variable
    for record in data['countries']:       # Loop through each country record in the JSON data
        country = record['country']        # Extract the country name
        capital = record['capital']        # Extract the capital city
        print(f"The capital of {country} is {capital}")  # Display the country and its capital

#3

import csv                     # Import the csv module to work with CSV files

try:                            # Start a try block to handle possible file errors

    with open("results.csv") as results_file:   # Open the CSV file safely (auto-closes)
        reader = csv.reader(results_file)       # Create a CSV reader object
        headings = next(reader)                  # Read and store the header row
        results = []                             # Create an empty list to store results
        for row in reader:                       # Loop through each remaining row
            results.append(row)                  # Add each row to the results list

        print(headings)                          # Display the CSV headings
        print(results)                           # Display all results from the CSV

except FileNotFoundError:                        # Handle the error if the file is missing
    print("The file could not be found.")        # Display an error message


#4
import csv                                    # Import the csv module to work with CSV files

try:                                         # Start a try block to handle file-related errors

    with open("data.csv") as file:            # Open the CSV file safely using with
        csv_reader = csv.reader(file)         # Create a CSV reader object
        heading = next(csv_reader)[0]         # Read the first heading (first column header)
        values = []                           # Create an empty list to store column values
        for line in csv_reader:               # Loop through each remaining row in the CSV
            values.append(line[0])            # Store the first column value in the list
        print(heading, values)                # Display the heading and the collected values

except FileNotFoundError:                     # Handle the error if the file does not exist
    print("Error: The file could not be found.")  # Display an error message

#5
import json                              # Import the json module to work with JSON files

with open("languages.json") as f:        # Open the JSON file safely using a with statement
    countries = json.load(f)             # Load the JSON data from the file into a variable

for country in countries:                # Loop through each country in the JSON data
    country_name = country["country"]    # Extract the country name
    main_language = country["languages"][0]   # Get the first language (main language)
    other_languages = country["languages"][1:]  # Get all remaining languages

    print(f"The main language of {country_name} is {main_language}.")   # Display the main language
    print(f"The other languages of {country_name} are {other_languages}.")  # Display other languages
    print()                           