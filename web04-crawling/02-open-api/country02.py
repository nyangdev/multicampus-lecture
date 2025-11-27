import requests
from xml.etree import ElementTree

BASE_URL = "https://apis.data.go.kr/1262000/TravelWarningServiceV3"
SERVICE_KEY = "buHsmRhtQRsG99cGMQpvbhC34ODTTB3TxlHwZEGiyFQmETUPv5NopU9LfLkZiP6n%2FgDkcHOJ31V73yZHN1of9w%3D%3D"
CALL_URL = "/getTravelWarningListV3"

url = f"{BASE_URL}/{CALL_URL}?serviceKey={SERVICE_KEY}&pageNo=1&numOfRows=10&returnType=xml"

resp = requests.get(url)
# print(resp.text)
tree = ElementTree.fromstring(resp.text)
# print(tree)
# print(tree[0][1])

for item in tree[0][1]:
    if item.find("attention").text == "여행유의":
        print(item.find("country_name").text)