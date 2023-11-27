import unittest
from worker import *


class Testcase(unittest.TestCase):
    def test_add_worker(self):
        workers = WorkerDB("file.csv")
        number_of_workers = len(workers.workers)
        g = gen_id("file.csv")
        ID = next(g)
        name = "John"
        surname = "Don"
        department = "goods"
        salary = 25000
        new_worker = Worker(ID, name, surname, department, salary)
        workers.add_worker(new_worker, "file.csv")
        new_number_of_workers = len(workers.workers)
        self.assertEqual(number_of_workers + 1, new_number_of_workers)

    def test_delete_worker(self):
        workers = WorkerDB("file.csv")
        number_of_workers = len(workers.workers)
        workers.delete_worker('3')
        new_number_of_workers = len(workers.workers)
        self.assertEqual(number_of_workers - 1, new_number_of_workers)

    def test_sort_workers(self):
        workers = WorkerDB("file.csv")
        workers.sort_workers("name")
        self.assertTrue(workers.workers[0].name == "Anastasiya")

    def test_search_worker(self):
        workers = WorkerDB("file.csv")
        search_list = workers.search_workers("ID", "350")
        self.assertTrue(search_list[0].name == "Sofia")

    def test_edit_worker(self):
        workers = WorkerDB("file.csv")
        workers.edit_worker("4", "name", "Nastya")
        self.assertTrue(workers.workers[3].name == "Nastya")


if __name__ == "__main__":
    unittest.main()
