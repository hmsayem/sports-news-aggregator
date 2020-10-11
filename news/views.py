from django.shortcuts import render

# Create your views here.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import time

driver_path = "C:/webDrivers/chromedriver.exe"
brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"
option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_argument("--headless")
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

latest_titles = []
latest_images = []
latest_details = []


def getDailyStar(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    image_div = soup.find("div", class_="pane-image")
    if not image_div:
        return

    title = soup.find('h1').text
    latest_titles.append(title)

    image = image_div.find('img')
    latest_images.append(image['src'])

    body = soup.find('p').text
    latest_details.append(body)


url = "https://www.thedailystar.net/sports"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
content = soup.find('div', class_="updates")
headers = content.find_all("h5")

latest_urls = []
for item in headers:
    url = item.find('a')
    complete = 'https://www.thedailystar.net' + url['href']
    latest_urls.append(complete)
    getDailyStar(complete)

latest_data = []
for i in range(len(latest_titles)):
    dict = {}
    dict['title'] = latest_titles[i]
    dict['image'] = latest_images[i]
    dict['url'] = latest_urls[i]
    dict['detail'] = latest_details[i]
    dict['newspaper'] = "The Daily Star"
    latest_data.append(dict)


def get_soup(url):
    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
    browser.get(url)
    page_source = browser.page_source
    browser.close()
    soup = BeautifulSoup(page_source, 'lxml')
    return soup


# Football Prothom Alo
p_football_titles = []
p_football_images = []
p_football_details = []


def getProthomAlo(url):
    soup = get_soup(url)
    title = soup.find('h1', class_='headline').text
    p_football_titles.append(title)
    image = soup.find('img', class_="qt-image")
    if image:
        p_football_images.append('https:' + image['src'])
    else:
        p_football_images.append(None)
    body = soup.find('p').text
    p_football_details.append(body)


soup = get_soup('https://en.prothomalo.com/sports/football')
content = soup.find_all('div', class_='en-story-card')
p_football_urls = []
for item in content:
    url = item.find('a')
    p_football_urls.append(url['href'])
    getProthomAlo(url['href'])

football_data = []
for i in range(len(p_football_titles)):
    dict = {}
    dict['title'] = p_football_titles[i]
    dict['image'] = p_football_images[i]
    dict['url'] = p_football_urls[i]
    dict['detail'] = p_football_details[i]
    dict['newspaper'] = "Prothom Alo"
    football_data.append(dict)

# Cricket Prothom Alo

p_cricket_titles = []
p_cricket_images = []
p_cricket_details = []


def getProthomAlo(url):
    soup = get_soup(url)
    title = soup.find('h1', class_='headline').text
    p_cricket_titles.append(title)
    image = soup.find('img', class_="qt-image")
    if image:
        p_cricket_images.append('https:' + image['src'])
    else:
        p_cricket_images.append(None)

    body = soup.find('p').text
    p_cricket_details.append(body)


soup = get_soup('https://en.prothomalo.com/sports/cricket')
content = soup.find_all('div', class_='en-story-card')
p_cricket_urls = []
for item in content:
    url = item.find('a')
    p_cricket_urls.append(url['href'])
    getProthomAlo(url['href'])

cricket_data = []
for i in range(len(p_cricket_titles)):
    dict = {}
    dict['title'] = p_cricket_titles[i]
    dict['image'] = p_cricket_images[i]
    dict['url'] = p_cricket_urls[i]
    dict['detail'] = p_cricket_details[i]
    dict['newspaper'] = "Prothom Alo"
    cricket_data.append(dict)

# Football Daily Star

d_football_titles = []
d_football_images = []
d_football_details = []


def getDailyStar(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    image_div = soup.find("div", class_="pane-image")
    if not image_div:
        return

    title = soup.find('h1').text
    d_football_titles.append(title)

    image = image_div.find('img')
    d_football_images.append(image['src'])

    field = soup.find('div', class_='field-body')
    body = field.find('p').text
    d_football_details.append(body)


response = requests.get('https://www.thedailystar.net/sports/football')
soup = BeautifulSoup(response.text, 'lxml')
content = soup.find_all('h4')

d_football_urls = []
for item in content:
    url = item.find('a')
    complete = 'https://www.thedailystar.net' + url['href']
    d_football_urls.append(complete)
    getDailyStar(complete)

for i in range(len(d_football_titles)):
    dict = {}
    dict['title'] = d_football_titles[i]
    dict['image'] = d_football_images[i]
    dict['url'] = d_football_urls[i]
    dict['detail'] = d_football_details[i]
    dict['newspaper'] = "The Daily Star"
    football_data.append(dict)

# Cricket Daily Star

d_cricket_titles = []
d_cricket_images = []
d_cricket_details = []


def getDailyStar(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    image_div = soup.find("div", class_="pane-image")
    if not image_div:
        return

    title = soup.find('h1').text
    d_cricket_titles.append(title)

    image = image_div.find('img')
    d_cricket_images.append(image['src'])

    field = soup.find('div', class_='field-body')
    body = field.find('p').text
    d_cricket_details.append(body)


response = requests.get('https://www.thedailystar.net/sports/cricket')
soup = BeautifulSoup(response.text, 'lxml')
content = soup.find_all('h4')

d_cricket_urls = []
for item in content:
    url = item.find('a')
    complete = 'https://www.thedailystar.net' + url['href']
    d_cricket_urls.append(complete)
    getDailyStar(complete)

for i in range(len(d_cricket_titles)):
    dict = {}
    dict['title'] = d_cricket_titles[i]
    dict['image'] = d_cricket_images[i]
    dict['url'] = d_cricket_urls[i]
    dict['detail'] = d_cricket_details[i]
    dict['newspaper'] = "The Daily Star"
    cricket_data.append(dict)


def Home(request):
    content = {
        "latest_data": latest_data
    }
    return render(request, 'index.html', content)


def Football(request):
    content = {
        'football_data': football_data
    }
    return render(request, 'football.html', content)


def Cricket(request):
    content = {
        'cricket_data': cricket_data
    }
    return render(request, 'cricket.html', content)
