#!/usr/bin/env python3

class Employee:
    def __init__(self, name, phone, salary=10000):
        self.name = name
        self.phone = phone
        self.salary = salary

    def print_salary_info(self):
        print("Employee {} gets {} Rubles".format(self.name, self.salary))

    def add_salary(self, delta=5000):
        self.salary = self.salary + delta

    def add(self, other_empl):
        new_name = self.name + "&" + other_empl.name
        new_phone = str(round((int(self.phone) + int(other_empl.phone)) / 2))
        new_salary = self.salary + other_empl.salary
        return Employee(new_name, new_phone, new_salary)

    __add__ = add

    def __del__(self):
        print(self.name + " is FIRED!!!")


class US_Employee(Employee):
    def print_salary_info(self):
        print("Mister {} gets {} Dollars".format(self.name, self.salary))


if __name__ == "__main__":
    first_empl = Employee("Rasul", "9055", salary=20000)
    first_empl.print_salary_info()

    second_empl = US_Employee("Rasul", "9055", salary=20000)
    second_empl.print_salary_info()
    second_empl = Employee("Merry", "9055", salary=30000)
