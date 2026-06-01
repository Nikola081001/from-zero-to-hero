import json


def load_people():
    try:
        with open("people_goals.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_people(people):
    with open("people_goals.json", "w") as file:
        json.dump(people, file, indent=4)
