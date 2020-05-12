import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import json
import os

driver = webdriver.Chrome()
url = "https://www.youtube.com/watch?v=wsiArTIqetE"

def VideoLinks(url):
    driver.get(url)
    sleep(2)
    html = driver.find_element_by_tag_name('html')
    while True:
        firstList = driver.find_elements_by_id("thumbnail")
        html.send_keys(Keys.END)
        sleep(2)
        secondList = driver.find_elements_by_id("thumbnail")
        if(firstList == secondList):
            videoList = []
            for x in secondList:
                link = x.get_attribute('href')
                videoList.append(link)
            return videoList
            break
    

def UserNames(url):
    driver.get(url)
    sleep(2)
    html = driver.find_element_by_tag_name('html')
    nameList = []
    driver.execute_script("window.scrollTo(0, window.scrollY + 400)")
    sleep(3)
    i=0
    
    
    #number = [int(s) for s in commentCount.split() if s.isdigit()]
    #print(number[0])
    while(i < number[0]/9):
        driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
        sleep(3)
        i+=1    

    names = driver.find_elements_by_id("author-text")
    for x in names:
        nameList.append(x.text)
    return nameList
        
def WriteToFile():
    name = UserNames()
    with open("names.json", "w", encoding='utf-8') as write_file:
        json.dump(name, write_file, ensure_ascii=False)

# videos = VideoLinks(url)
# json3 = UserNames(videos[2])
# print(json3)
