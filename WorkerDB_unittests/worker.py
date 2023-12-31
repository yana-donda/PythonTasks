import csv


def dec_sort(func):
    def sort_wrapper(self):
        field_for_sort = input("Enter field to sort (ID, name, surname, department, salary): ")
        func(self, field_for_sort)
        print("~~Sorted by", field_for_sort, "~~")
    return  sort_wrapper


def dec_search(func):
    def search_wrapper(self):
        field_for_search = input("Enter field for search (ID, name, surname, department, salary): ")
        print("~~Search by ", field_for_search, "~~", sep="")
        search_list = func(self, field_for_search)
        if len(search_list) == 0:
            print("There are no worker in search list")
        else:
            print("~~~~Search list~~~~")
            for worker in search_list:
                print(worker)
    return search_wrapper


def dec_file_not_found(func):
    def for_functions():
        try:
            func(for_functions())
        except FileNotFoundError as e:
            print(e)
    return for_functions



def gen_id(filename):
    all_id = [0]
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            all_id.append(int(line[0]))
    max_id = max(all_id)
    next_id = max_id + 1
    yield next_id


class Worker:
    def __init__(self, ID, name, surname, dep, salary):
        self.__ID = ID
        self.name = name
        self.surname = surname
        self.dep = dep
        self.salary = int(salary)

    def get_id(self): return self.__ID

    def __str__(self):
        return (f"ID: {self.get_id()}\n"
                f"Name: {self.name}\n"
                f"Surname: {self.surname}\n"
                f"Department: {self.dep}\n"
                f"Salary: {self.salary}")


class WorkerDB:
    def __init__(self, filename):
        self.workers = self.read_from_file(filename)

    def read_from_file(self, filename):
        workers_list = []
        try:
            with open(filename, 'r', newline='') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    worker = Worker(row["ID"], row["name"], row["surname"], row["department"], row["salary"])
                    workers_list.append(worker)
            return workers_list
        except FileNotFoundError:
            raise FileNotFoundError("Error: File not found")

    def write_to_file(self, filename):
        with open(filename, 'w', newline='') as new_csv_file:
            fieldnames = ["id", "name", "surname", "department", "salary"]
            csv_writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames, delimiter=",")
            csv_writer.writeheader()
            for worker in self.workers:
                line = {fieldnames[0]: worker.get_id(), fieldnames[1]: worker.name, fieldnames[2]: worker.surname,
                        fieldnames[3]: worker.dep, fieldnames[4]: worker.salary}
                csv_writer.writerow(line)

    def add_worker(self, new_worker, filename):
        self.workers.append(new_worker)
        with open(filename, 'a', newline='') as new_csv_file:
            fieldnames = ["ID", "name", "surname", "department", "salary"]
            csv_writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames, delimiter=",")
            line = {fieldnames[0]: new_worker.get_id(), fieldnames[1]: new_worker.name,
                    fieldnames[2]: new_worker.surname, fieldnames[3]: new_worker.dep, fieldnames[4]: new_worker.salary}
            csv_writer.writerow(line)

    def edit_worker(self, id, field, new_field):
        for worker in self.workers:
            if worker.get_id() == id:
                if field == "name":
                    worker.name = new_field
                elif field == "surname":
                    worker.surname = new_field
                elif field == "department":
                    worker.dep = new_field
                elif field == "salary":
                    worker.salary = new_field
                else:
                    print("Something wrong with field for edit")
                    break

    def delete_worker(self, id):
        count = 0
        for worker in self.workers:
            if worker.get_id() == id:
                self.workers.remove(worker)
                count += 1
        if count == 0:
            print("There are no worker with this ID")

    def sort_workers(self, field):
        if field == "ID":
            self.workers.sort(key=lambda x: x.get_id())
        elif field == "name":
            self.workers.sort(key=lambda x: x.name)
        elif field == "surname":
            self.workers.sort(key=lambda x: x.surname)
        elif field == "department":
            self.workers.sort(key=lambda x: x.dep)
        elif field == "salary":
            self.workers.sort(key=lambda x: x.salary)
        else:
            print("Something wrong with field for sort")



    def search_workers(self, field, for_search):
        search_list = []
        if field == "ID":
            for worker in self.workers:
                if worker.get_id() == for_search:
                    search_list.append(worker)
        if field == "name":
            for worker in self.workers:
                if worker.name == for_search:
                    search_list.append(worker)
        elif field == "surname":
            for worker in self.workers:
                if worker.surname == for_search:
                    search_list.append(worker)
        elif field == "department":
            for worker in self.workers:
                if worker.dep == for_search:
                    search_list.append(worker)
        elif field == "salary":
            for worker in self.workers:
                if worker.salary == for_search:
                    search_list.append(worker)
        return search_list

    def print_workers(self):
        for worker in self.workers:
            print(worker)
            print("~~~~~~~~~~~~~~~~~~~~~~")
