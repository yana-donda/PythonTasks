import csv


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
                    worker = Worker(int(row["ID"]), row["name"], row["surname"], row["department"], row["salary"])
                    workers_list.append(worker)
            return workers_list
        except FileNotFoundError:
            raise FileNotFoundError("Error: File not found")

    def write_to_file(self, filename):
        with open(filename, 'w', newline='') as new_csv_file:
            fieldnames = ["ID", "name", "surname", "department", "salary"]
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
                    try:
                        new_salary = int(input("Enter new salary: "))
                        worker.salary = new_salary
                    except ValueError:
                        raise ValueError("Error: Salary might be int")
                else:
                    print("Something wrong with field for edit")
                    break
            else:
                print("Something wrong with ID")
                break

    def delete_worker(self, id, filename):
        count = 0
        for worker in self.workers:
            if worker.get_id() == id:
                self.workers.remove(worker)
                count += 1
        if count != 0:
            self.write_to_file(filename)

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

    def search_workers(self, field, field2):
        search_list = []
        if field == "ID":
            for worker in self.workers:
                if worker.get_id() == field2:
                    search_list.append(worker)
        if field == "name":
            for worker in self.workers:
                if worker.name == field2:
                    search_list.append(worker)
        elif field == "surname":
            for worker in self.workers:
                if worker.surname == field2:
                    search_list.append(worker)
        elif field == "department":
            for worker in self.workers:
                if worker.dep == field2:
                    search_list.append(worker)
        elif field == "salary":
            for worker in self.workers:
                if worker.salary == field2:
                    search_list.append(worker)
        return search_list

    def print_workers(self):
        for worker in self.workers:
            print(worker)
            print("~~~~~~~~~~~~~~~~~~~~~~")
