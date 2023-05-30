from __future__ import print_function
from bs4 import BeautifulSoup
import requests
import csv


# Function to scrape and write club data to a CSV file
def clubs():
    # Initialize the URL
    url = "https://www.ghanayello.com/category/night_clubs/0"

    # Loop through the pages
    for page in range(1, 3):
        # Modify the URL with the page number
        url = url.replace('/0', f'/{page}')

        # Send a GET request to the URL
        result = requests.get(url)

        # Parse the HTML content
        doc = BeautifulSoup(result.text, "html.parser")

        # Find all club tags on the page
        tags = doc.find_all("div", class_="company g_0")

        # Store club data
        data = []

        # Iterate over club tags
        for tag in tags:
            # Extract club name
            name = tag.find("h4").string

            # Extract club address
            address = tag.find("div", class_="address").text

            # Print club name and address
            print(name + " ---- " + address)
            print("\n")

            # Append club data to the list
            real = [name, address]
            data.append(real)

        # Write club data to a CSV file
        with open("Clubs.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)


# Call the clubs function to start scraping
clubs()








