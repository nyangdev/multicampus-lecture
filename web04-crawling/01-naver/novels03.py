from bs4 import BeautifulSoup
import requests
import json

target_url = "https://novel.naver.com/webnovel/weekday"
resp = requests.get(target_url)
print(resp)
soup = BeautifulSoup(resp.text, "html.parser")

section = soup.find("div", class_="component_section")

novel_list = list()
item_list = section.find_all("li", class_="item")
for item in item_list:
    lank = item.p.text.strip()
    title = item.select("span.title")[0].text
    novel_url = item.a.attrs["href"]
    # print(f"{lank:2}위 : {title} \t https://novel.naver.com{novel_url}")
    tmp = dict()
    tmp["lank"] = lank
    tmp["title"] = title
    tmp["url"] = novel_url

    novel_list.append(tmp)


result = dict()
result["novels"] = novel_list

result_json = json.dumps(result, ensure_ascii=False)
# ensure_ascii 속성이 뭔지?
# 파이썬 공식 문서 확인

with open("novels.json", "w", encoding="utf-8") as f:
    f.write(result_json)