from worker import *
from plots import *

def create_worker(workers):
    print("~~~~Enter new worker~~~~")
    g = gen_id("file.csv")
    ID = next(g)
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    dep = input("Enter department: ")
    try:
        salary = int(input("Enter salary: "))
    except ValueError:
        raise ValueError("Error: Salary might be int")
    new_worker = Worker(ID, name, surname, dep, salary)
    workers.add_worker(new_worker, "file.csv")


def edit_worker_(workers):
    try:
        id_for_edit = int(input("Enter worker ID to edit: "))
    except ValueError:
        raise ValueError("ID might be int")
    print("~~~~Edit worker~~~~")
    field_for_edit = input("Enter field for edit: ")
    workers.edit_worker(id_for_edit, field_for_edit)


def delete_worker_(workers):
    try:
        id_to_delete = int(input("Enter worker ID to delete: "))
    except ValueError:
        raise ValueError("ID might be int")
    workers.delete_worker(id_to_delete)

def menu_for_run():
    try:
        while True:
            print("---Menu---")
            print("1. Run the program")
            print("Anything else to finish the program")
            choice = input("Your choice: ")

            if choice == "1":
                menu_for_functions()
            else:
                break
    except Exception as e:
        print(e)


def menu_for_functions():
    try:
        workers = WorkerDB("file.csv")
        while True:
            print("What to do with workers DB?")
            print("1. Add new worker")
            print("2. Edit worker")
            print("3. Delete worker by ID")
            print("4. Sort workers")
            print("5. Search workers")
            print("6. Print workers")
            print("7. Save workers DB to csv-file")
            print("8. Show how much people get paid")
            print("9. Show number of workers in each department")
            print("Anything else to quit")

            choice = input("Your choice: ")

            if choice == "1":
                create_worker(workers)
            elif choice == "2":
                edit_worker_(workers)
            elif choice == "3":
                delete_worker_(workers)
            elif choice == "4":
                workers.sort_workers()
                workers.print_workers()
            elif choice == "5":
                workers.search_workers()
            elif choice == "6":
                workers.print_workers()
            elif choice == "7":
                workers.write_to_file('new_file.csv')
            elif choice == "8":
                show_histogram()
            elif choice == "9":
                show_pie()
            else:
                break
    except FileNotFoundError as e1:
        raise FileNotFoundError(e1)
    except ValueError as e2:
        raise ValueError(e2)


menu_for_run()
if __name__ == "__name__":
    menu_for_run()
