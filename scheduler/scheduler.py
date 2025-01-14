# scheduler/scheduler.py
from apscheduler.schedulers.blocking import BlockingScheduler
from scraper.scraper import fetch_web_content

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', hours=6)
def scheduled_task():
    url = input("Please enter the URL to scrape: ")
    if url:
        content = fetch_web_content(url)
        print(f"Data has been scraped from {url}.")
    else:
        print("No URL entered, skipping this scraping task.")
