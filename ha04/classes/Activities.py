from abc import abstractmethod
from typing import List
from .Employees import Employee
import sys


class Activities:

    @abstractmethod
    def all_employees(self, department) -> List[Employee]:
        pass

    @abstractmethod
    def change_salary(self, employees, is_percent: bool, amount: int):
        pass

    @abstractmethod
    def select_workers_by_salary(self, department, frm: int, to: int) -> List[Employee]:
        pass


class ActivitiesImpl(Activities):

    def all_employees(self, department) -> List[Employee]:
        result = department.employees
        dep = department.department
        while len(dep) > 0:
            d = dep.pop()
            result.extend(d.employees)
            dep.extend(d.department)
        return result

    # is_percent - True if amount is percentage of change otherwise false
    # amount - amount of change
    def change_salary(self, employees, is_percent: bool, amount: int):
        for e in employees:
            if e.active:
                e.salary = e.salary * (amount / 100 + 1) if is_percent else e.salary + amount

    def select_workers_by_salary(self, department, frm: int, to: int) -> List[Employee]:
        result: List[Employee] = []
        if frm is None:
            frm = 0

        if to is None:
            to = sys.maxsize

        for e in department.employees:
            if frm <= e.salary <= to:
                result.append(e)

        for d in department.department:
            result.extend(self.select_workers_by_salary(d, frm, to))

        return result


