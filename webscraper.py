import requests
from bs4 import BeautifulSoup
import pandas as pd

years = list(range(2010, 2023))

# url_start = "https://www.basketball-reference.com/international/euroleague/{}_totals.html"
# for year in years:
#     url = url_start.format(year)
#
#     # Send an HTTP GET request to the URL to fetch the webpage content
#     data = requests.get(url)
#
#     #Write the retrieved HTML data to a file named after the year
#     with open("stats/{}.html".format(year), "w+") as f:
#         f.write(data.text)

# Create an empty DataFrame called 'totals' to store the collected data
totals = pd.DataFrame()

for year in years:
    # Read the HTML content from the file for the specific year
    with open("stats/{}.html".format(year)) as f:
        page = f.read()

    #Initialize the parser
    soup = BeautifulSoup(page, "html.parser")

    #Find specific metadata of the table and convert the HTML table to DataFrame
    table = soup.find(id="totals-stats-{}".format(year))
    df = pd.read_html(str(table))[0]

    #Add the 'Year' column
    df["Year"] = year

    #Concatenate with current DataFrame
    totals = pd.concat([totals, df], ignore_index=True)

print(totals)