from bs4 import BeautifulSoup
import requests
import csv

# Open a text file to write output (optional)
f = open("demofile2.txt", "w")

# Define the base URL to scrape
base_url = "https://egotickets.com/events/page/"

# Loop through the page numbers from 0 to 11
for page in range(12):
    # Construct the URL by appending the page number
    url = base_url + str(page)
    print(url)
    # Send a GET request to the URL
    result = requests.get(url)

    # Parse the HTML content
    doc = BeautifulSoup(result.text, "html.parser")

    # Find all tags containing event information
    tags = doc.find_all("div", class_="post-content")

    # Loop through the event tags
    for tag in tags:
        # Extract event details
        name_tag = tag.find("h3", class_="title uk-text-nowrap uk-text-truncate")
        name = name_tag.string if name_tag is not None else ""

        price_tag = tag.find("span", class_="uk-align-right uk-margin-remove-bottom price")
        price = price_tag.string if price_tag is not None else ""

        month_tag = tag.find("span", class_="start-date-month")
        month = month_tag.string if month_tag is not None else ""

        day_tag = tag.find("span", class_="start-date-day")
        day = day_tag.string if day_tag is not None else ""

        location_tag = tag.find("div", class_="venue")
        location = location_tag.text if location_tag is not None else ""

        # Print event details
        print(name + "------" + day + "/" + month + "--------" + price + "-------" + location)

        # Prepare data for writing to CSV file
        header = ['Title', 'Price', 'Date', 'Month']
        data = [name, price, day, month]

        # Write data to CSV file
        with open('Events.csv', 'a+', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            # Uncomment the next line if you want to include headers
            # writer.writerow(header)
            writer.writerow(data)











