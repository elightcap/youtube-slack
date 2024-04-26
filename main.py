import os
import time

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv, find_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv(find_dotenv())
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
SLACK_SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET')
print(SLACK_BOT_TOKEN)

app = App(
    token = SLACK_BOT_TOKEN,
    signing_secret = SLACK_SIGNING_SECRET
)

@app.command("/youtube")
def play_video(ack,body):
    ack()
    url = body["text"]
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    time.sleep(5)
    video = driver.find_element("id","movie_player")
    video.send_keys("K")
    video.send_keys("F")
    title = (driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[1]/h1/yt-formatted-string")).text
    print(title)
    while True:
        try:
            button = driver.find_element('class name','ytp-ad-skip-button-container')
        except:
            title2 = (driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[1]/h1/yt-formatted-string")).text
            if title != title2:
                driver.close()
                return

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
