import csv
id_count = 0

def dec_sort(func):
    def sort_wrapper(self):
        field_for_sort = input("Enter field to sort (name, surname, department, salary): ")
        func(self, field_for_sort)
        print("~~Sorted by", field_for_sort, "~~")
    return  sort_wrapper

def dec_search(func):
    def search_wrapper(self):
        field_for_search = input("Enter field for search (name, surname, department, salary): ")
        print("~~Search by ", field_for_search, "~~", sep="")
        search_list = func(self, field_for_search)
        if len(search_list) == 0:
            print("There are no worker in search list")
        else:
            print("~~~~Search list~~~~")
            for worker in search_list:
                print(worker)
    return search_wrapper

class Worker:
    def __init__(self, name, surname, dep, salary):
        global id_count
        id_count = id_count + 1
        ID = id_count
        self.set_id(ID)
        self.name = name
        self.surname = surname
        self.dep = dep
        self.salary = int(salary)

    def set_id(self, id): self.__ID = id
    def get_id(self): return self.__ID

    def __str__(self):
        return (f"ID: {self.__ID}\n"
                f"Name: {self.name}\n"
                f"Surname: {self.surname}\n"
                f"Department: {self.dep}\n"
                f"Salary: {self.salary}")


class WorkerDB:
    def __init__(self, filename):
        self.workers = self.read(filename)

    def read(self, filename):
        workers_list = []
        with open(filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                worker = Worker(row["name"], row["surname"], row["department"], row["salary"])
                workers_list.append(worker)
        return workers_list

    def write_to_file(self, filename):
        with open(filename, 'w') as new_csv_file:
            fieldnames = ["name", "surname", "department", "salary"]
            csv_writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames, delimiter=",")
            csv_writer.writeheader()
            for worker in self.workers:
                line = {fieldnames[0]: worker.name, fieldnames[1]: worker.surname, fieldnames[2]: worker.dep,
                        fieldnames[3]: worker.salary}
                csv_writer.writerow(line)


    def add_worker(self, new_worker):
        self.workers.append(new_worker)

    def edit_worker(self, id, field):
        for worker in self.workers:
            if worker.get_id() == id:
                if field == "name":
                    new_name = input("Enter new name: ")
                    worker.name = new_name
                elif field == "surname":
                    new_surname = input("Enter new surname: ")
                    worker.surname = new_surname
                elif field == "department":
                    new_dep = input("Enter new department: ")
                    worker.dep = new_dep
                elif field == "salary":
                    new_salary = int(input("Enter new salary: "))
                    worker.salary = new_salary

    def delete_worker(self, id):
        for worker in self.workers:
            if worker.get_id() == id:
                self.workers.remove(worker)

    @dec_sort
    def sort_workers(self, field):
        if field == "name":
            self.workers.sort(key=lambda x: x.name)
        elif field == "surname":
            self.workers.sort(key=lambda x: x.surname)
        elif field == "department":
            self.workers.sort(key=lambda x: x.dep)
        elif field == "salary":
            self.workers.sort(key=lambda x: x.salary)

    @dec_search
    def search_workers(self, field):
        search_list = []
        if field == "name":
            name_for_search = input("Enter name for search: ")
            for worker in self.workers:
                if worker.name == name_for_search:
                    search_list.append(worker)
        elif field == "surname":
            surname_for_search = input("Enter surname for search: ")
            for worker in self.workers:
                if worker.surname == surname_for_search:
                    search_list.append(worker)
        elif field == "department":
            dep_for_search = input("Enter department for search: ")
            for worker in self.workers:
                if worker.dep == dep_for_search:
                    search_list.append(worker)
        elif field == "salary":
            salary_for_search = int(input("Enter salary for search: "))
            for worker in self.workers:
                if worker.salary == salary_for_search:
                    search_list.append(worker)
        return search_list

    def print_workers(self):
        for worker in self.workers:
            print(worker)
            print("~~~~~~~~~~~~~~~~~~~~~~")

def menu_for_run():
    while True:
        print("---Menu---")
        print("1. Run the program")
        print("Anything else to finish the program")
        choice = input("Your choice: ")

        if choice == "1":
            menu_for_functions()
        else:
            break

def menu_for_functions():
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
        print("Anything else to quit")

        choice = input("Your choice: ")

        if choice == "1":
            print("~~~~Enter new worker~~~~")
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            dep = input("Enter department: ")
            salary = int(input("Enter salary: "))
            new_worker = Worker(name, surname, dep, salary)
            workers.add_worker(new_worker)
        elif choice == "2":
            id_for_edit = int(input("Enter worker ID to edit: "))
            print("~~~~Edit worker~~~~")
            field_for_edit = input("Enter field for edit: ")
            workers.edit_worker(id_for_edit, field_for_edit)
        elif choice == "3":
            id_to_delete = int(input("Enter worker ID to delete: "))
            workers.delete_worker(id_to_delete)
        elif choice == "4":
            workers.sort_workers()
            workers.print_workers()
        elif choice == "5":
            workers.search_workers()
        elif choice == "6":
            workers.print_workers()
        elif choice == "7":
            workers.write_to_file('new_file.csv')
        else:
            break

menu_for_run()