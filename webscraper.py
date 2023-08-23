import requests
from bs4 import BeautifulSoup
import pandas as pd

years = list(range(2010, 2023))
# url_start = "https://www.basketball-reference.com/international/euroleague/{}_totals.html"
# for year in years:
#     url = url_start.format(year)
#     data = requests.get(url)
#
#     with open("stats/{}.html".format(year), "w+") as f:
#         f.write(data.text)

totals = pd.DataFrame()

for year in years:
    with open("stats/{}.html".format(year)) as f:
        page = f.read()

    soup = BeautifulSoup(page, "html.parser")

    table = soup.find(id="totals-stats-{}".format(year))
    df = pd.read_html(str(table))[0]
    df["Year"] = year

    totals = pd.concat([totals, df], ignore_index=True)

print(totals)