"""
get streaming url from KBS live radio website
default channel: KBS 2FM
requirement: BeautifulSoup, requests
"""

from bs4 import BeautifulSoup
from selenium import webdriver
# import requests
import json
# import re
import time
import subprocess

DEFAULT_URL = 'http://onair.kbs.co.kr/index.html?sname=onair&stype=live&ch_code=25&ch_type=radioList&openradio=on'
DEFAULT_DIR = '/Users/bonseungkoo/airflow'
DEFAULT_TIME = 10

def get_info(radio_url):
    # req = requests.get(radio_url)
    # html = req.text
    driver = webdriver.Edge()
    driver.get(DEFAULT_URL)
    jdat = str(driver.execute_script('return channel;'))
    jdat = jdat.replace("\'", '\"')
    scrm_jdat = json.loads(jdat)
    channel = scrm_jdat["channel_item"][1]["channel_id"]
    url = scrm_jdat["channel_item"][1]["service_url"]
    url = url.replace('amp;','')
    return url, channel

def record(site_url, duration):
    str_url, name = get_info(site_url)
    timestr = time.strftime('%y%m%d_%H%M%S')
    dir = DEFAULT_DIR
    # os.system('ffmpeg -i "{}" -t {} -c copy {}_{}.ts'.format(str_url, duration, name, timestr))
    cmd = 'ffmpeg -i "{}" -t {} -c copy "{}/{}_{}.ts"'.format(str_url, duration, dir, name, timestr)
    subprocess.run(cmd, shell=True, check=True)

if __name__ == '__main__':
   record(DEFAULT_URL, DEFAULT_TIME)