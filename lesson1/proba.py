import json

name = input("Enter your name: ")
country = input("Enter your country: ")
goal = input("Enter your goal: ")
hours = int(input("Enter your daily study hours: "))


person = {
    "name": name,
    "country": country,
    "goal": goal,
    "daily_study_hours": hours
}

with open("my_goal.json", "w") as file:
    json.dump(person, file, indent=4)


with open("my_goal.json", "r") as file:
    data = json.load(file)


print("Saved data: ")
print(data)
print("Name: ", data["name"])
print("Main goal: ", data["goal"])
