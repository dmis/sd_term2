import sys
from typing import List
from datetime import date
from classes.Entities import Department, Employee
from classes.Enumerates import Position, Growth


def select_workers_by_salary(department: Department, frm: int, to: int) -> List[Employee]:
    result: List[Employee] = []
    if frm is None:
        frm = 0

    if to is None:
        to = sys.maxsize

    for e in department.employees:
        if frm <= e.salary <= to:
            result.append(e)

    for d in department.department:
        result.extend(select_workers_by_salary(d, frm, to))

    return result


def select_workers_by_position(department: Department, position: Position) -> List[Employee]:
    result: List[Employee] = []

    for e in department.employees:
        if e.position == position:
            result.append(e)

    for d in department.department:
        result.extend(select_workers_by_position(d, position))

    return result


if __name__ == "__main__":
    ceo = Employee('Timothy Donald Cook', Position.CEO, 1000000,
                   date(1998, 6, 3))
    company = Department('Apple', ceo)

    hosd = Employee('John Smith', Position.HEAD_OF_DEPARTMENT, 10000, date(2015, 6, 3))
    sd = Department('Strategy department', hosd)
    e1 = Employee('Ann', Position.DEVELOPER, 1000, date(2019, 6, 3))
    sd.hire(e1)
    e2 = Employee('Kate', Position.DEVELOPER, 2000, date(2020, 6, 3))
    sd.hire(e2)
    company.add_department(sd)

    hod = Employee('Neo', Position.HEAD_OF_DEPARTMENT, 1500, date(2008, 6, 3))
    dd = Department('Development department', hod)
    e3 = Employee('Mary', Position.DEVELOPER, 1200, date(2019, 6, 3))
    dd.hire(e3)
    e4 = Employee('Alex', Position.DEVELOPER, 1500, date(2020, 6, 3))
    dd.hire(e4)
    company.add_department(dd)

    e4.change_position(Position.TEAM_LEADER, Growth.PROMOTED)

    ceo2 = Employee('Satya Nadella', Position.CEO, 1000000,
                   date(1998, 6, 3))
    company2 = Department('Microsoft', ceo)
    # ---  HA 04 -------
    # --- Compare companies by staff size(A > B = True)
    print('staff size of company :', len(company.all_employees))
    print('staff size of company2 :', len(company2.all_employees))
    assert company >= company2
    print(company >= company2)
    assert company2 <= company
    print(company <= company2)
    assert company != company2
    print(company != company2)
    assert company == company
    print(company == company2)


    # --- Get companies vacancies list

    company.add_vacancy(Position.TEAM_LEADER)
    company.add_vacancy(Position.TEAM_LEADER)
    company.add_vacancy(Position.HEAD_OF_DEPARTMENT)

    company2.add_vacancy(Position.TEAM_LEADER)
    company2.add_vacancy(Position.DEVELOPER)
    # --- difference abs(A - B)
    print(company - company2)
    print(company2 - company)

    # --- union (A or B)
    print(company | company2)
    print(company2 | company)

    # --- intersection (and getting min of them) (A and B)
    print(company & company2)
    print(company2 & company)

    # --- Test HA 03 -----
    # print('Show changing history of ' + e4.name)
    # for h in e4.history:
    #     print(str(h.init_date) + ' : ' + h.description)
    #
    # print('\nCheck  salary before increasing')
    # for i in sd.employees:
    #     print(i.name + ' : ' + str(i.salary))
    # sd.change_salary(True, 10)
    #
    # print('\nCheck  salary after increasing')
    # for i in sd.employees:
    #     print(i.name + ' : ' + str(i.salary))
    #
    # print('\nSearch employees with salary more than 0 but less than 1500')
    # fltr = select_workers_by_salary(company, 0, 1500)
    # for i in fltr:
    #     print(i.name + ' : ' + str(i.salary))
    #
    # print('\nSearch employees with position Head')
    # fltr2 = select_workers_by_position(company, Position.HEAD_OF_DEPARTMENT)
    # for i in fltr2:
    #     print(i.name + ' : ' + str(i.position.value))
    #
    # print('\n All employees list ')
    # all = company.all_employees
    # for a in all:
    #     print(a.name + ' | ' + a.department.name+ ' | ' + a.position.value)
