import requests

BASE_URL = "https://apis.data.go.kr/1262000/TravelWarningServiceV3"
SERVICE_KEY = "buHsmRhtQRsG99cGMQpvbhC34ODTTB3TxlHwZEGiyFQmETUPv5NopU9LfLkZiP6n%2FgDkcHOJ31V73yZHN1of9w%3D%3D"
CALL_URL = "/getTravelWarningListV3"

url = f"{BASE_URL}/{CALL_URL}?serviceKey={SERVICE_KEY}&pageNo=1&numOfRows=10"
# print(url)

resp = requests.get(url)
# print(resp.json())

for item in resp.json()["response"]["body"]["items"]["item"]:
    # print(item)
    if item["attention"] == "여행유의":
        print(item["country_name"])