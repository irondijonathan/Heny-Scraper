from bs4 import BeautifulSoup
import requests
import csv

# Define the URL to scrape
url = "https://jetsanza.com/best-tourist-sites-to-visit-in-each-of-the-16-regions-of-ghana/"

# Send a GET request to the URL
result = requests.get(url)

# Parse the HTML content
doc = BeautifulSoup(result.text, "html.parser")

# Initialize a list to store the extracted data
ymap = []

# Find all tags containing the strong elements
tags = doc.find_all("strong")
for tag in tags:
    # Append the text content of the strong element to the list
    ymap.append(tag.text)

# Print the extracted data (optional)
print(ymap)

# Initialize a counter
x = 0

# Loop until the counter reaches 16
while x < 16:
    # Find all tags containing ordered lists
    places = doc.find_all("ol")
    for place in places:
        # Print the text content of the ordered list along with the corresponding element from ymap
        print(place.text + "---" + ymap[x])

        # Increment the counter
        x += 1

        # Prepare data for writing to CSV file
        header = ["Place"]
        data = [place.text]

        # Write data to CSV file
        with open("Places_to_visit.csv", "a+", newline="", encoding="UTF8") as f:
            writer = csv.writer(f)
            # Uncomment the next line if you want to include headers
            # writer.writerow(header)
            writer.writerow(data)
