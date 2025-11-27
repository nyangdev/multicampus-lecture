import chromedriver_autoinstaller

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from bs4 import BeautifulSoup
from time import sleep
import json

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split(".")[0]
# print(chrome_ver)

if os.path.exists(f"./{chrome_ver}"):
    print("exists")
else:
    chromedriver_autoinstaller.install(True)

target_url = "https://comic.naver.com/webtoon?tab=thu"

service = Service(executable_path=f"./{chrome_ver}/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(target_url)

sleep(2)
soup = BeautifulSoup(driver.page_source, "html.parser")
# print(soup)

webtoons_list = list()
li_list = soup.select(".component_wrap .item")
for li in li_list:
    star = li.find("span", class_="Rating__star_area--dFzsb").text
    title = li.find("span", class_="ContentTitle__title--e3qXt").text

    print(f"{star} \t {title}")
    webtoon = dict()
    webtoon["star"] = star[2:]
    webtoon["title"] = title
    webtoons_list.append(webtoon)

driver.quit()

result = dict()
result["webtoons"] = webtoons_list

result_json = json.dumps(result, ensure_ascii=False)
# json.dumps가 뭔지 찾아보기

with open("webtoons.json", "w", encoding="utf-8") as file:
    file.write(result_json)

driver.quit()