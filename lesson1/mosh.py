import json


def load_json_file(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data


def save_json_file(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def count_by_nested_key(data, outer_key, inner_key):
    count = {}
    for item in data:
        value = item[outer_key][inner_key]
        if value in count:
            count[value] += 1
        else:
            count[value] = 1
    return count


def sort_count_dict(count):
    sorted_items = sorted(
        count.items(), key=lambda item: item[1], reverse=True)
    return sorted_items


def get_top_n(sorted_items, n):
    return sorted_items[:n]


users = load_json_file("user_from_api.json")

company_counts = count_by_nested_key(users, "company", "name")
sorted_company_counts = sort_count_dict(company_counts)
top_5_companies = get_top_n(sorted_company_counts, 5)

result = []


for index, (company, count) in enumerate(top_5_companies, start=1):
    result.append({
        "rank": index,
        "company": company,
        "count": count
    })

save_json_file("top_5_companies.json", result)
print("Top 5 companies saved successfully")
