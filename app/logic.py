
import requests
from bs4 import BeautifulSoup
import json


if __name__ == "__main__":
    print("\033[1m" + "COVID-19 Status of Goa" + "\033[0m\n")

    url = 'https://www.mohfw.gov.in/data/datanew.json'
    res = requests.get(url)  

    whole_data = res.json()

    goa_stats = [x for x in whole_data if x['state_name'] == 'Goa']

    print(goa_stats)

    with open("data.json", "w") as f:
        json.dump(goa_stats, f)   