from storage import load_people, save_people
from people import (
    get_new_person, show_people, delete_person,
    search_person, edit_person, person_exsist, get_non_empty_input, get_valid_number
)


def main():
    people = load_people()

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


if __name__ == "__main__":
    main()
