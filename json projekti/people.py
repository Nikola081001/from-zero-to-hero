def get_new_person():
    name = get_non_empty_input("Enter your name: ")
    goal = get_non_empty_input("Enter your goal: ")
    hours = get_valid_number("Enter your daily study hours: ")
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
    name_to_edit = get_non_empty_input("Enter the name to edit: ")

    for person in people:
        if person["name"].lower() == name_to_edit.lower():
            new_goal = get_non_empty_input("Enter the new goal: ")
            new_hours = get_valid_number("Enter the new daily study hours: ")

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


def get_valid_number(message):
    while True:
        try:
            number = int(input(message))

            if number < 0:
                raise ValueError("Number must be non-negative.")

            return number

        except ValueError as error:
            print("Error:", error)
            print("Please try again.")


def get_non_empty_input(message):
    while True:
        try:
            value = input(message)

            if not value.strip():
                raise ValueError("Input cannot be empty.")
            return value
        except ValueError as error:
            print("Error:", error)
            print("Please try again.")
