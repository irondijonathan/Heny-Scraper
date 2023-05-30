#this script scrapes places for recreation and fun places to visit in ghana
from bs4 import BeautifulSoup
import requests
import csv

# Define the URLs to scrape
url = "https://blog.meqasa.com/recreational-parks-gardens-in-accra/"
url2 = "https://www.thedreamafrica.com/20-must-visit-tourist-attractions-in-ghana/"

# Send GET requests to the URLs
result = requests.get(url)
result2 = requests.get(url2)

# Parse the HTML content
doc = BeautifulSoup(result.text, "html.parser")
doc2 = BeautifulSoup(result2.text, "html.parser")

# Scraping for recreational parks and gardens in Accra
tags = doc.find_all("h3", class_="p4")

data = []

# Loop through the tags
for tag in tags:
    # Extract the name
    name = tag.text
    print(name)

    # Append the name to the data list
    data.append([name])

    # Write data to CSV file
    with open("Recreation.csv", "a+", newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow([name])



# Scraping for tourist attractions in Ghana
tags2 = doc2.find_all("strong")

# Loop through the tags
for tag2 in tags2:
    # Extract the name
    name = tag2.text
    print(name)

    # Write data to CSV file
    with open("Recreation.csv", "a+", newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow([name])





