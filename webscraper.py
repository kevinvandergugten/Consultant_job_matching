from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup

# from dataclasses import dataclass
import requests
import boto3
import time

from boto_upload_file import upload_file


# @dataclass
# class Scraper:
#
#     url: str
#     source: str
#
#
#     def __post_init__(self):


if __name__ == '__main__':

    url = 'https://www.headfirst.nl/opdrachten/'
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    driver.find_element(By.LINK_TEXT, "Alle cookies accepteren").click()

    # click on button multiple times to load all the jobs
    driver.find_element(By.LINK_TEXT, "Meer opdrachten laden").click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Meer opdrachten laden").click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Meer opdrachten laden").click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Meer opdrachten laden").click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Meer opdrachten laden").click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Meer opdrachten laden").click()

    divs = driver.find_elements(By.CLASS_NAME, 'col-md-4')

    links = []

    for div in divs:

        link = div.find_element(By.TAG_NAME, 'a').get_attribute('href')

        if 'mailto' in link:
            continue

        links.append(link)

    for index, job_url in enumerate(links):

        rr = requests.get(job_url)
        soup = BeautifulSoup(rr.text, 'html.parser')
        job_text = soup.find("div", {"class": "hfp_read-more"}).text

        file_name = f'job_{index}'
        bucket_name = 'consultant-skill-matching'

        with open(f'./job_posts/{file_name}.txt', 'w') as f:
            f.write(job_text)

        upload_file(f'./job_posts/{file_name}.txt', bucket_name)

        # s3 = boto3.client('s3')
        # with open(f'./job_posts/{file_name}.txt', "rb") as f:
        #     s3.upload_fileobj(f, bucket_name)

        # print(job_text)