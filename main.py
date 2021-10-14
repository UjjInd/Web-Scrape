import re
import requests
from bs4 import BeautifulSoup
from collections import Counter

url = "https://venturebeat.com/"
regex_url = url.replace(":","\:").replace("/","\/").replace(".","\.")

response = requests.get(url)
html = response.text

#print(response.text[:1000])

soup = BeautifulSoup(html, "html.parser")
links = soup.findAll("a")

news_urls = []
for link in links:
  href = link.get("href")
  if href and re.search("^" + regex_url + "[0-9]{4}\/[0-9]{2}\/[0-9]{2}", href):
    news_urls.append(href)

all_nouns = []

#for url in news_urls[:20]:
for url in news_urls:
  #print("Fetching{}".format(url))
  response = requests.get(url)
  html = response.text
  soup = BeautifulSoup(html, "html.parser")

  words = soup.text.split()
  nouns = [word for word in words if re.search("^[A-Z][a-zA-Z]*",word)]
  all_nouns += nouns

print(Counter(all_nouns).most_common(100))