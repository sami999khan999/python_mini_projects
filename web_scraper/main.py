from bs4 import BeautifulSoup
import requests
import json

url = "https://en.wikipedia.org/wiki/Table_(information)"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

table_soup = soup.findAll("table", class_="wikitable")[0]

table_title = [title.text for title in table_soup.findAll("th")][:-1]

table_data = table_soup.findAll("tr")[1:]

table = []

for row in table_data:
    row_data = row.findAll("td")

    individual_row_data = [data.text for data in row_data]

    row_dist = {
        table_title[i]: individual_row_data[i] for i in range(len(individual_row_data))
    }

    table.append(row_dist)

table_json = json.dumps(table, indent=4)

print(table_json)
