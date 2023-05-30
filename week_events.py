from bs4 import BeautifulSoup
import requests
import re
import csv

data_dict = {}

for page_number in range(15):
    url = f"https://viewghana.com/events/c/weekly-bar-events/page/{page_number}/"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    tags = doc.find_all("div", class_="card")

    for tag in tags:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        event = tag.find("h2", class_="geodir-entry-title")

        for substring in days:
            if substring.lower() in event.text.lower():
                day = substring.capitalize()
                break
        else:
            continue

        x = event.text.find("@")
        y = event.text.find("-")
        title = event.text[:y]
        place = event.text[x+2:y-1]

        image = tag.find("img")
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex, str(image))
        image_links = [x[0] for x in url]
        photo = image_links[0]

        date = tag.find("div", class_="geodir-schedule")
        z = date.text.find("2022")
        time = date.text[12+6:]

        data_dict[place] = [title, day, time, photo]

# Write dictionary to CSV file
with open("week_events.csv", "w", newline="", encoding="UTF8") as file:
    writer = csv.writer(file)
    writer.writerow(["Place", "Title", "Day", "Time", "Photo"])
    for place, values in data_dict.items():
        writer.writerow([place] + values)

print("Data written to data.csv file.")
