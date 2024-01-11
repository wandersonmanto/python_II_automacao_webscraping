from bs4 import BeautifulSoup
import requests


# 1 - Coletando Vagas em Python
url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
  print(job.h3.text.strip())
