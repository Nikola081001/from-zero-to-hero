import json


def load_json_file(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data


def save_json_file(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def count_by_nested_key(data, outer_key, inner_key):
    counts = {}

    for item in data:
        value = item[outer_key][inner_key]

        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts


def sort_count_dict(counts):
    sorted_items = sorted(
        counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_items


def get_top_n(sorted_items, n):
    return sorted_items[:n]


users = load_json_file("user_from_api.json")


city_counts = count_by_nested_key(users, "address", "city")
sorted_city_counts = sort_count_dict(city_counts)
top_3_cities = get_top_n(sorted_city_counts, 3)

result = []

for index, (city, count) in enumerate(top_3_cities, start=1):
    result.append({
        "rank": index,
        "city": city,
        "count": count
    })


save_json_file("final_top_3_cities.json", result)

print("Final top 3 cities saved successfuly")
