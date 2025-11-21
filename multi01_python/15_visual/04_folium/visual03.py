import folium
import json

my_loc = folium.Map(location=[37.5481533, 127.0733985], zoom_start=10)

with open("starbucks.json", "r", encoding="utf-8") as file:
    starbucks_json = json.load(file)

# print(starbucks_json)
# print("------------------------------")
# print(starbucks_json["list"])

for starbucks in starbucks_json["list"]:
    folium.Marker([starbucks["lat"], starbucks["lot"]],
                  popup=folium.Popup(starbucks["s_name"], max_width=100)).add_to(my_loc)

my_loc.save("visual03.html")