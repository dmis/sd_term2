from datetime import date
from abc import abstractmethod
from enum import Enum


class Position(Enum):
    CEO = 'Chief Execution Officer'
    HEAD_OF_DEPARTMENT = 'Head of Department'
    TEAM_LEADER = 'Team Leader'
    DEVELOPER = 'Engineer'


class Employee:
    def __init__(self, name: str, salary: int, hired_date: date):
        self._name = name
        self._salary = salary
        self._hired_date = hired_date
        self._active = True
        self._department = None
        self._position = None


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        self.name = new_name

    @abstractmethod
    def position(self) -> Position:
        pass

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, dep):
        self._department = dep

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary: str):
        self._salary = new_salary

    @property
    def active(self):
        return self._active

    def fire(self):
        self._active = False


class CEO(Employee):
    @property
    def position(self) -> Position:
        return Position.CEO


class Head(Employee):
    @property
    def position(self) -> Position:
        return Position.HEAD_OF_DEPARTMENT


class TeamLeader(Employee):
    @property
    def position(self) -> Position:
        return Position.TEAM_LEADER


class Developer(Employee):
    @property
    def position(self) -> Position:
        return Position.DEVELOPER
