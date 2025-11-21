purchases = [{"name": "김예은", "cart": ["banana", "apple"]},
            {"name": "이은지", "cart": ["apple", "jelly"]}]

products = [{"banana": 3500, "apple": 3000, "jelly": 2000}]

"""
원하는 출력값

김예은 6500원 사용했습니다.
이은지 5000원 사용했습니다.
"""

for person in purchases:
    # print(item)
    mysum = 0
    for item in person['cart']:
        # print(item)
        if item in products[0].keys():
            mysum += products[0][item]
    print(f"{person['name']} {mysum} 사용했습니다.")


result = list(map(lambda person: f"{person['name']}  {sum(list(map(lambda item : products[0][item] if item in products[0].keys() else None, person['cart'])))}" , purchases))
print(result)













product = products[0]

for purchase in purchases:

    if purchase["name"] == "김예은":
        price = product["banana"] + product["apple"]
    else:
        price = product["apple"] + product["jelly"]

    print(f"{purchase["name"]}", end=" ")
    print(f"{price}원 사용했습니다.")