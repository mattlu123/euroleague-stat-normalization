import requests
from bs4 import BeautifulSoup
import pandas as pd

years = list(range(2010, 2023))

## EUROLEAGE PER GAME

# url_start = "https://www.basketball-reference.com/international/euroleague/{}_per_game.html"
# for year in years:
#     url = url_start.format(year)

#     # Send an HTTP GET request to the URL to fetch the webpage content
#     data = requests.get(url)

#     #Write the retrieved HTML data to a file named after the year
#     with open("euro_pg/{}.html".format(year), "w+") as f:
#         f.write(data.text)

#Create an empty DataFrame to store the collected data
euro_perGame = pd.DataFrame()

for year in years:
    # Read the HTML content from the file for the specific year
    with open("euro_pg/{}.html".format(year)) as f:
        page = f.read()

    #Initialize the parser
    soup = BeautifulSoup(page, "html.parser")

    #Find specific metadata of the table and convert the HTML table to DataFrame
    table = soup.find(id="per_game-stats-{}".format(year))
    df = pd.read_html(str(table))[0]

    #Add the 'Year' column
    df["Year"] = year

    #Concatenate with current DataFrame
    euro_perGame = pd.concat([euro_perGame, df], ignore_index=True)

print(euro_perGame)


## EUROLEAGE PER 36

# url_start = "https://www.basketball-reference.com/international/euroleague/{}_per_minute.html"
# for year in years:
#     url = url_start.format(year)

#     # Send an HTTP GET request to the URL to fetch the webpage content
#     data = requests.get(url)

#     #Write the retrieved HTML data to a file named after the year
#     with open("euro_p36/{}.html".format(year), "w+") as f:
#         f.write(data.text)

# Create an empty DataFrame to store the collected data
euro_per36 = pd.DataFrame()

for year in years:
    # Read the HTML content from the file for the specific year
    with open("euro_p36/{}.html".format(year)) as f:
        page = f.read()

    #Initialize the parser
    soup = BeautifulSoup(page, "html.parser")

    #Find specific metadata of the table and convert the HTML table to DataFrame
    table = soup.find(id="per_minute-stats-{}".format(year))
    df = pd.read_html(str(table))[0]

    #Add the 'Year' column
    df["Year"] = year

    #Concatenate with current DataFrame
    euro_per36 = pd.concat([euro_per36, df], ignore_index=True)

print(euro_per36)

## NBA PER GAME

# url_start = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html"
# for year in years:
#     url = url_start.format(year)

#     # Send an HTTP GET request to the URL to fetch the webpage content
#     data = requests.get(url)

#     #Write the retrieved HTML data to a file named after the year
#     with open("nba_pg/{}.html".format(year), "w+") as f:
#         f.write(data.text)

# Create an empty DataFrame to store the collected data
nba_perGame = pd.DataFrame()

for year in years:
    # Read the HTML content from the file for the specific year
    with open("nba_pg/{}.html".format(year)) as f:
        page = f.read()

    #Initialize the parser
    soup = BeautifulSoup(page, "html.parser")

    #Find specific metadata of the table and convert the HTML table to DataFrame
    table = soup.find(id="per_game_stats")
    df = pd.read_html(str(table))[0]

    #Add the 'Year' column
    df["Year"] = year

    #Concatenate with current DataFrame
    nba_perGame = pd.concat([nba_perGame, df], ignore_index=True)

print(nba_perGame)

## NBA PER 36

# url_start = "https://www.basketball-reference.com/leagues/NBA_{}_per_minute.html"
# for year in years:
#     url = url_start.format(year)

#     # Send an HTTP GET request to the URL to fetch the webpage content
#     data = requests.get(url)

#     #Write the retrieved HTML data to a file named after the year
#     with open("nba_p36/{}.html".format(year), "w+") as f:
#         f.write(data.text)

# Create an empty DataFrame to store the collected data
nba_per36 = pd.DataFrame()

for year in years:
    # Read the HTML content from the file for the specific year
    with open("nba_p36/{}.html".format(year)) as f:
        page = f.read()

    #Initialize the parser
    soup = BeautifulSoup(page, "html.parser")

    #Find specific metadata of the table and convert the HTML table to DataFrame
    table = soup.find(id="per_minute_stats")
    df = pd.read_html(str(table))[0]

    #Add the 'Year' column
    df["Year"] = year

    #Concatenate with current DataFrame
    nba_per36 = pd.concat([nba_per36, df], ignore_index=True)

print(nba_per36)