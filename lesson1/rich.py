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


def get_new_person():
    name = input("Enter your name: ")
    goal = input("Enter your goal: ")
    hours = int(input("Enter your daily study hours: "))

    return {
        "name": name,
        "goal": goal,
        "daily_study_hours": hours
    }


def show_people(people):
    print("Upgraded list: ")
    for person in people:
        print(
            f"{person['name']} - {person['goal']} - {person['daily_study_hours']}")


people = load_people()


def delete_person(people):
    name_to_delete = input("Enter the name to delete: ")

    for person in people:
        if person["name"].lower() == name_to_delete.lower():
            people.remove(person)
            print("Person deleted successfully!")
            return

    print("Person not found.")


def search_person(people):
    name_to_search = input("Enter the name to search: ")

    for person in people:
        if person["name"].lower() == name_to_search.lower():
            print(
                f"{person['name']} - {person['goal']} - {person['daily_study_hours']}")
            return

    print("Person not found.")


def edit_person(people):
    name_to_edit = input("Enter the name to edit: ")

    for person in people:
        if person["name"].lower() == name_to_edit.lower():
            new_goal = input("Enter the new goal: ")
            new_hours = int(input("Enter the new daily study hours: "))

            person["goal"] = new_goal
            person["daily_study_hours"] = new_hours

            print("Person updated successfully!")
            return

    print("Person not found.")


def person_exsist(people, name):
    for person in people:
        if person["name"].lower() == name.lower():
            return True
    return False


while True:
    print("\nMenu: ")
    print("1. Show people")
    print("2. Add person")
    print("3. Delete person")
    print("4. Search person")
    print("5. Edit person")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_people(people)

    elif choice == "2":
        new_person = get_new_person()

        if person_exsist(people, new_person["name"]):
            print("Person already exists.")
        else:
            people.append(new_person)
            save_people(people)
            print("Person added successfully!")

    elif choice == "3":
        delete_person(people)
        save_people(people)

    elif choice == "4":
        search_person(people)

    elif choice == "5":
        edit_person(people)
        save_people(people)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
