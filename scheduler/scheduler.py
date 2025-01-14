from apscheduler.schedulers.blocking import BlockingScheduler
from scraper.scraper import fetch_custom_website

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', hours=6)
def scheduled_task():
    url = input("Enter the website URL to scrape: ")
    fetch_custom_website(url)
    print("Scheduled scraping completed.")
