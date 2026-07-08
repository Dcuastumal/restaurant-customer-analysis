# Wikipedia Scraper
# Chicago Cultural Information
import requests
import pandas as pd
from bs4 import BeautifulSoup


def scrape_chicago_culture():

    url = "https://en.wikipedia.org/wiki/Chicago"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Wikipedia page could not be loaded.")

    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = soup.find_all("p")

    culture_text = []

    for paragraph in paragraphs[:10]:

        text = paragraph.get_text(strip=True)

        if len(text) > 80:
            culture_text.append(text)

    chicago_culture = pd.DataFrame(
        {"culture_information": culture_text}
    )

    return chicago_culture


