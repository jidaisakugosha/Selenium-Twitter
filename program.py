# args: text, username, password

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import sys
import time
import random




class Twitter():
    def __init__(self):
        
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome('chromedriver', options = options)
        self.driver.implicitly_wait(10)
        self.driver.get("https://twitter.com/login")

    def login(self):
        write_email = self.driver.find_element_by_class_name(
            "js-username-field")
        write_email.send_keys(sys.argv[2])  # Email de Login do Twitter

        write_pass = self.driver.find_element_by_class_name(
            "js-password-field")

        write_pass.send_keys(sys.argv[3])  # Senha de Acesso do Twitter

        write_pass.send_keys(Keys.RETURN)

    def scrap(self):
        # page = requests.get("http://g1.globo.com/ultimas-noticias.html")
        # soup = BeautifulSoup(page.text, "html.parser")

        # news = [soup.find(class_="feed-post-link")]

        # for show_news in news:
        # 	text = (str(show_news.contents[0]) + "\n" + str(show_news.get("href")) + "\n" + str("Selenium and Twitter"))

        # for show_news in news:
        # 	text1 = (str(show_news.contents[0]) + "\n" + str(show_news.get("href")) + "\n" + str("Selenium and Twitter"))
        text = sys.argv[1]+'\n'+'\n'+str(random.randrange(100000))+'\n'+'\n'+'#東大'+' #駒場'+' #教養'+' #休講'

        return text

    def twitar(self):
        post = self.scrap()

        twitar = self.driver.find_element_by_name("tweet")
        twitar.send_keys("{}".format(post))
        send_tweet = self.driver.find_element_by_class_name("tweet-action")

        return send_tweet.click()

timer=random.randrange(20)
print(20+timer)
time.sleep(20+timer)
Twi = Twitter()
Twi.login()
Twi.twitar()
