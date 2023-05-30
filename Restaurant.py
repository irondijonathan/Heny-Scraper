from bs4 import BeautifulSoup
import requests
import csv

f = open("demofile2.txt", "w")


def loop():
    # Define the initial URL to scrape
    y = "https://ofadaa.com/accra/restaurants?page=0"
    x = int(y[42])

    # Loop through the pages
    while x < 25:
        y = "https://ofadaa.com/accra/restaurants?page=0"
        x += 1
        new = str(x)
        url = y.replace(y[42], new)

        # Send a GET request to the URL
        result = requests.get(url)

        # Parse the HTML content
        doc = BeautifulSoup(result.text, "html.parser")

        # Find all tags containing restaurant information
        tags = doc.find_all("div", class_="restaurant-information")

        # Loop through the restaurant tags
        for tag in tags:
            # Extract restaurant details
            name = tag.find("div", class_="restaurant-name")
            vote = tag.find("div", class_="restaurant-votes")
            location = tag.find("div", class_="restaurant-location")
            kitchen = tag.find("div", class_="restaurant-kitchen")
            accept = tag.find("div", class_="restaurant-accept")
            price = tag.find("div", class_="restaurant-price")

            try:
                # Print restaurant details
                print(
                    name.string + "--" + vote.text + "--" + location.text + "--" + kitchen.text + "--" + accept.text + "--" + price.text)
                print("\n")

                # Prepare data for writing to CSV file
                header = ['Name', 'Vote', 'Location', 'Kitchen', 'accept', 'price']
                data = [name.text, vote.text, location.text, kitchen.text, accept.text, price.text]

                # Write data to CSV file
                with open('Restaurant.csv', 'a+', newline='', encoding='UTF8') as f:
                    writer = csv.writer(f)
                    # writer.writerow(header)
                    writer.writerow(data)
            except:
                print("An exception occurred")
                print("\n")

                # Prepare data for writing to CSV file
                header = ['Title', 'Price', 'Date', 'month']
                data = ["An exception occurred"]

                # Write data to CSV file
                with open('Restaurant.csv', 'a+', newline='', encoding='UTF8') as f:
                    writer = csv.writer(f)
                    # writer.writerow(header)
                    writer.writerow(data)

        print(url)


loop()
