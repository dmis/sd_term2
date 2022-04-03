from typing import List

from .Enumerates import Position, Growth
from datetime import date


class History:
    def __init__(self, init_date: date, position: Position, growth: Growth, description: str):
        self.init_date = init_date
        self.position = position
        self.growth = growth
        self.description = description


class Employee:
    def __init__(self, name: str, position: Position, salary: int, hired_date: date):
        self.name = name
        self._position = position
        self.salary = salary
        self._hired_date = hired_date
        self.active = True
        self._department = None
        self._growth = []
        self.add_growth_list(position, Growth.HIRED)

    def change_name(self, new_name: str):
        self.name = new_name

    @property
    def position(self) -> Position:
        return self._position

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, dep):
        self._department = dep

    def change_position(self, new_position: Position, growth: Growth):
        self.add_growth_list(new_position, growth)
        self._position = new_position
        if growth is Growth.FIRED:
            self.active = False

    @property
    def history(self) -> List[History]:
        return self._growth

    def fire(self):
        self.active = False

    def add_growth_list(self, new_position: Position, growth: Growth):
        if growth is Growth.HIRED:
            history = History(self._hired_date, new_position, growth, self.name + ' was ' + growth.value)
        else:
            history = History(date.today(), new_position, growth, self.name + ' was ' + growth.value + (
                ' from ' + self._position.value + 'to ' + new_position.value if new_position is not None else ''))
        self._growth.append(history)


class Department:

    def __init__(self, name, boss: Employee):
        self.boss = boss
        self.name = name
        self._departments = []
        self._employees = []
        self._vacancies = {}
        self.hire(boss)

    def add_department(self, department):
        self._departments.append(department)

    @property
    def department(self):
        return self._departments

    @property
    def employees(self) -> List[Employee]:
        return self._employees

    @property
    def all_employees(self) -> List[Employee]:
        result = self._employees
        dep = self._departments
        while len(dep) > 0:
            d = dep.pop()
            result.extend(d.employees)
            dep.extend(d.department)
        return result

    def hire(self, employee: Employee):
        self.employees.append(employee)
        employee.department = self

    # is_percent - True if amount is percentage of change otherwise false
    # amount - amount of change
    def change_salary(self, is_percent: bool, amount: int):
        for e in self._employees:
            if e.active:
                e.salary = e.salary * (amount / 100 + 1) if is_percent else e.salary + amount

    def add_vacancy(self, position: Position):
        count = self._vacancies.get(position, 0)
        self._vacancies[position] = count + 1

    @property
    def vacancies(self) -> List[Position]:
        return self._vacancies

    def __check_class(func):
        def wrapper(one, two):
            if not isinstance(two, Department):
                return None
            return func(one, two)

        return wrapper

    @__check_class
    def __gt__(self, other):
        return len(self.all_employees) > len(other.all_employees)

    @__check_class
    def __ge__(self, other):
        return len(self.all_employees) >= len(other.all_employees)

    @__check_class
    def __lt__(self, other):
        return len(self.all_employees) < len(other.all_employees)

    @__check_class
    def __le__(self, other):
        return len(self.all_employees) <= len(other.all_employees)

    @__check_class
    def __eq__(self, other):
        return len(self.all_employees) == len(other.all_employees)

    @__check_class
    def __ne__(self, other):
        return len(self.all_employees) != len(other.all_employees)

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
