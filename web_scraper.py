
import requests
from bs4 import BeautifulSoup
import json

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    data = []

    for item in soup.find_all("div", class_="quote"):
        quote = item.find("span", class_="text").get_text(strip=True)
        author = item.find("small", class_="author").get_text(strip=True)
        data.append({"quote": quote, "author": author})

    with open("headlines.txt", "w", encoding="utf-8") as file:
        for item in data:
            file.write(item["quote"] + " - " + item["author"] + "\n")

    with open("headlines.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("Data extracted successfully!")
    print("Total records:", len(data))
    print("Saved to headlines.txt and headlines.json")

    for item in data:
        print(item["quote"], "-", item["author"])

except requests.RequestException as error:
    print("Website connection error:", error)
