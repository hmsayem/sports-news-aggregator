# Sports News Aggregator
### About
A web application built with Django which aggregates latest sports news from multiple websites using Web Scraping and presents the data in one location. The combination of two python packages, Beautiful Soup and Selenium has been used for dynamic scraping.
The news articles have been aggregated from Prothom Alo and The Daily Star. Sports category is also available in this application which makes the navigation easier for the users.
### Why build a news aggregator ?
There are hundreds of news websites, they do cover news on several broad topics, out of which only a few of them are of our interest. A news aggregator can be a tool to save a lot of time and with some modifications and filtration we can fine tune it to show only news of our interest. A news aggregator can be an useful tool to get information within short time.

### Screenshot

<img src="media/screenshot.png">

### How to set up
##### Clone project & Install Requirements
> Make sure you have already installed python3 and git.
```
git clone https://github.com/hmsayem/Sports-News-Aggregator.git && cd Sports-News-Aggregator
pip install -r requirements.txt
```
##### Run Server
```
python manage.py runserver
```

> The website should be available at `localhost:8000`.
