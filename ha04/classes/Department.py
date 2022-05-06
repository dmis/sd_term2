from typing import List
from .Activities import Activities
from .Employees import Position, Employee


class Department:

    def __init__(self, name, boss: Employee, activities: Activities):
        self.boss = boss
        self.name = name
        self._activities = activities
        self._departments = []
        self._employees = []
        self.hire(boss)

    def add_department(self, department):
        self._departments.append(department)

    @property
    def department(self):
        return self._departments

    @property
    def employees(self) -> List[Employee]:
        return self._employees

    def all_employees(self, position: Position = None) -> List[Employee]:
        result = []
        for e in self._activities.all_employees(self):
            if position is None:
                result.append(e)
            elif e == position:
                result.append(e)

        return result

    def hire(self, employee: Employee):
        self.employees.append(employee)
        employee.department = self

    # is_percent - True if amount is percentage of change otherwise false
    # amount - amount of change
    def change_salary(self, is_percent: bool, amount: int, position: Position = None):
        empl = self.all_employees(position)
        self._activities.change_salary(empl, is_percent, amount)

    def select_workers_by_salary(self, frm: int, to: int) -> List[Employee]:
        return self._activities.select_workers_by_salary(self, frm, to)

    def __check_class(func):
        def wrapper(one, two):
            if not isinstance(two, Department):
                return None
            return func(one, two)

        return wrapper

    @__check_class
    def __gt__(self, other):
        return len(self.all_employees()) > len(other.all_employees)

    @__check_class
    def __ge__(self, other):
        return len(self.all_employees()) >= len(other.all_employees())

    @__check_class
    def __lt__(self, other):
        return len(self.all_employees()) < len(other.all_employees())

    @__check_class
    def __le__(self, other):
        return len(self.all_employees()) <= len(other.all_employees())

    @__check_class
    def __eq__(self, other):
        return len(self.all_employees()) == len(other.all_employees())

    @__check_class
    def __ne__(self, other):
        return len(self.all_employees()) != len(other.all_employees())

    @__check_class
    def __sub__(self, other):
        result = self._vacancies.copy()
        for key in result.keys():
            count = other.vacancies.get(key, 0)
            result[key] = abs(result[key] - count)
        return result

    @__check_class
    def __or__(self, other):
        result = self._vacancies.copy()
        for key, value in other.vacancies.items():
            result[key] = result.get(key, 0) + value
        return result

    @__check_class
    def __and__(self, other):
        result = {}
        for key, value in self._vacancies.items():
            count = other.vacancies.get(key, 0)
            if count > 0:
                result[key] = min(value, count)
        return result
