from bs4 import BeautifulSoup
import requests
import pandas as pd

print("the web you want to scrape in: https://", end="")
url = "https://" + input()

web = requests.get(url)
bs = BeautifulSoup(web.content, "html.parser")

res = requests.get(url)
htmlData = res.content
parsedData = BeautifulSoup(htmlData, "html.parser")
print(parsedData.prettify())