# Parse the HTML for the "Top Playstation 4 Games (By Metascore)" on Metacritic's PS4 page
import requests
from bs4 import BeautifulSoup


def scrapeTopPS4Games(soup):
  titles = []
  metascores = []
  # Find the elements of the a tag with class name title
  games = soup.find_all("a", class_="title")
  for each_game in games:
    title = each_game.find("h3").get_text().strip()
    titles.append(title)
  # Find the elements of the div tag with given class name
  scores = soup.find_all("div", class_="clamp-score-wrap")
  for each_score in scores:
    score = each_score.find("div", class_="metascore_w large game positive").get_text().strip()
    metascores.append(score)
  gamesbymetascore = {key:value for key, value in zip(titles, metascores)}
  result = []
  for key in gamesbymetascore:
      result.append({"title": key, "score": gamesbymetascore[key]})
  return sorted(result, key=lambda k: k['score'], reverse=True)



ps_url = 'https://www.metacritic.com/game/playstation-4'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
try:
  html_text = requests.get(ps_url, headers=headers).content
  soup = BeautifulSoup(html_text, 'html.parser')
  topps4games = scrapeTopPS4Games(soup)
except Exception as e:
  print(e)



