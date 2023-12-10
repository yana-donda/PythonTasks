import matplotlib.pyplot as plt
import csv
import sys
import numpy as np


def show_histogram():
    x = []
    with open("file.csv", 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            x.append(int(line['salary']))
    plt.hist(x)
    plt.xlabel("Зарплата")
    plt.ylabel("Кількість людей")
    plt.title("Розподіл заробітньої плати")
    plt.show()

def show_pie():
    x = []
    with open("file.csv", 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            x.append((line['department']))

    departments = {}

    for department in x:
        if department in departments:
            departments[department] += 1
        else:
            departments[department] = 1

    departments = sorted(departments.items(), key=lambda x: x[0])
    departments = dict(departments)
    department_label = np.array(list(departments.keys()))
    y = np.array(list(departments.values()))

    plt.pie(y, labels=department_label, shadow=True)
    plt.title("Кількість працівників у кожному відділі")
    plt.show()
