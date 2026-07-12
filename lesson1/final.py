import json


def load_json_file(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data


def save_json_file(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def counted_by_nested_key(data, outer_key, inner_key, value):
    filtered_data = []

    for item in data:
        if item[outer_key][inner_key].lower() == value.lower():
            filtered_data.append(item)
    return (filtered_data)


users = load_json_file("user_from_api.json")

filtered_by_company = counted_by_nested_key(
    users, "company", "name", "Romaguera-Crona")
save_json_file("filtered_by_company.json", filtered_by_company)

print("Filtered data saved successfully")
print("Number of matching users: ", len(filtered_by_company))
