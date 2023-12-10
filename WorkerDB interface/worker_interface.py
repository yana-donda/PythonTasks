from worker import WorkerDB, Worker, gen_id
from plots import *
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class WorkersApp:
    filename = "file.csv"
    workers = WorkerDB(filename)

    def __init__(self, root):
        self.root = root
        self.root.title("Worker database")
        self.root.configure(bg="plum1")

        self.text_title = tk.Label(root, text="Список робітників: ", bg="cyan2")
        self.field1_title = tk.Label(root, text="Введіть (ID/name/surname/department/salary):", bg="cyan2")
        self.field2_title = tk.Label(root, text="Введіть параметр для пошуку: ", bg="cyan2")
        self.enter_name_title = tk.Label(root, text="Введіть ім'я: ", bg="cyan2")
        self.enter_surname_title = tk.Label(root, text="Введіть прізвище: ", bg="cyan2")
        self.enter_dep_title = tk.Label(root, text="Введіть відділ: ", bg="cyan2")
        self.enter_salary_title = tk.Label(root, text="Введіть зарплату: ", bg="cyan2")
        self.enter_ID_label = tk.Label(root, text="Введіть ID робітника, якого хочете видалити", bg="cyan2")

        self.text_display = tk.Text(root, width=25, height=18)

        self.enter_field1 = tk.Entry(root, width=20)
        self.enter_field2 = tk.Entry(root, width=20)
        self.enter_name = tk.Entry(root, width=15)
        self.enter_surname = tk.Entry(root, width=15)
        self.enter_dep = tk.Entry(root, width=15)
        self.enter_salary = tk.Entry(root, width=15)
        self.enter_ID = tk.Entry(root, width=5)

        self.button_histogram = tk.Button(root, text="Відобразити гістограму", command=self.display_histogram, bg="orchid4")
        self.button_pie = tk.Button(root, text="Відобразити кругову діаграму", command=self.display_pie, bg="orchid4")
        self.button_print = tk.Button(root, text="Відобразити список робітників", command=self.display_workers, bg="orchid4")
        self.button_sort = tk.Button(root, text="Посортувати робітників", command=self.display_sort_workers, bg="orchid4")
        self.button_search = tk.Button(root, text="Знайти робітників за параметрами", command=self.display_search_workers, bg="orchid4")
        self.button_add_worker = tk.Button(root, text="Додати робітника", command=self.display_add_worker, bg="orchid4")
        self.button_delete_worker = tk.Button(root, text="Видалити робітника", command=self.delete_worker_, bg="orchid4")

        self.button_print.pack(side=tk.TOP)
        self.button_sort.pack(side=tk.TOP)
        self.button_search.pack(side=tk.TOP)
        self.field1_title.pack(side=tk.TOP)
        self.enter_field1.pack(side=tk.TOP)
        self.field2_title.pack(side=tk.TOP)
        self.enter_field2.pack(side=tk.TOP)
        self.text_title.pack(side=tk.TOP)
        self.text_display.pack(side=tk.TOP)
        self.button_add_worker.pack(side=tk.TOP)
        self.enter_name_title.pack(side=tk.TOP)
        self.enter_name.pack(side=tk.TOP)
        self.enter_surname_title.pack(side=tk.TOP)
        self.enter_surname.pack(side=tk.TOP)
        self.enter_dep_title.pack(side=tk.TOP)
        self.enter_dep.pack(side=tk.TOP)
        self.enter_salary_title.pack(side=tk.TOP)
        self.enter_salary.pack(side=tk.TOP)
        self.button_delete_worker.pack(side=tk.TOP)
        self.enter_ID_label.pack(side=tk.TOP)
        self.enter_ID.pack(side=tk.TOP)
        self.button_histogram.pack(side=tk.BOTTOM)
        self.button_pie.pack(side=tk.BOTTOM)

    def display_histogram(self):
        show_histogram()

    def display_pie(self):
        show_pie()

    def display_workers(self):
        workers_str = "\n".join(str(worker) for worker in self.workers.workers)
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(tk.END, workers_str)

    def display_sort_workers(self):
        field = self.enter_field1.get()
        self.workers.sort_workers(field)
        workers_str = "\n".join(str(worker) for worker in self.workers.workers)
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(tk.END, workers_str)

    def display_search_workers(self):
        field1 = self.enter_field1.get()
        if field1 == "salary":
            field2 = int(self.enter_field2.get())
        else:
            field2 = self.enter_field2.get()
        search_list = self.workers.search_workers(field1, field2)
        if len(search_list) == 0:
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, "There are no worker")
        else:
            search_list_str = "\n".join(str(worker) for worker in search_list)
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, search_list_str)

    def display_add_worker(self):
        g = gen_id("file.csv")
        ID = next(g)
        name = self.enter_name.get()
        surname = self.enter_surname.get()
        department = self.enter_dep.get()
        salary = int(self.enter_salary.get())
        new_worker = Worker(ID, name, surname, department, salary)
        self.workers.add_worker(new_worker, self.filename)
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(tk.END, str(new_worker))

    def delete_worker_(self):
        ID = int(self.enter_ID.get())
        self.workers.delete_worker(ID, self.filename)


if __name__ == "__main__":
    root = tk.Tk()
    app_worker = WorkersApp(root)
    root.mainloop()
