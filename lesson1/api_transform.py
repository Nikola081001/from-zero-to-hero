import json

with open("user_from_api.json", "r") as file:
    data = json.load(file)


city_count = {}


for user in data:
    city = user["address"]["city"]

    if city in city_count:
        city_count[city] += 1

    else:
        city_count[city] = 1

sorted_cities = sorted(
    city_count.items(), key=lambda item: item[1], reverse=True)


top_3_cities = sorted_cities[:3]


result = []

for index, (city, count) in enumerate(top_3_cities, start=1):
    result.append({
        "rank": index,
        "city": city,
        "count": count
    })


with open("top_3_ranked_cities.json", "w") as file:
    json.dump(result, file, indent=4)


print("Top 3 ranked cities saved successfully.")
