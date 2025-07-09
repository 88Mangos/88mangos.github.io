import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.premierleague.com/results?co=1&se=489&cl=-1');
soup = BeautifulSoup(page.content, 'html.parser')

