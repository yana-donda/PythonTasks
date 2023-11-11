import csv
id_count = 0


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

    def sort_workers(self, field):
        if field == "name":
            self.workers.sort(key=lambda x: x.name)
        elif field == "surname":
            self.workers.sort(key=lambda x: x.surname)
        elif field == "department":
            self.workers.sort(key=lambda x: x.dep)
        elif field == "salary":
            self.workers.sort(key=lambda x: x.salary)

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

workers = WorkerDB("file.csv")
workers.print_workers()

print("~~~~Enter new worker~~~~")
name = input("Enter name: ")
surname = input("Enter surname: ")
dep = input("Enter department: ")
salary = int(input("Enter salary: "))
new_worker = Worker(name, surname, dep, salary)
workers.add_worker(new_worker)
workers.print_workers()

id_for_edit = int(input("Enter worker ID to edit: "))
print("~~~~Edit worker~~~~")
field_for_edit = input("Enter field for edit: ")
workers.edit_worker(id_for_edit, field_for_edit)
workers.print_workers()

id_to_delete = int(input("Enter worker ID to delete: "))
workers.delete_worker(id_to_delete)
workers.print_workers()

field_for_sort = input("Enter field to sort: ")
workers.sort_workers(field_for_sort)
workers.print_workers()

field_for_search = input("Enter field for search: ")
search_workers = workers.search_workers(field_for_search)
if len(search_workers) == 0:
    print("There are no worker in search list")
else:
    print("~~~~Search list~~~~")
    for worker in search_workers:
        print(worker)

workers.write_to_file('new_file.csv')