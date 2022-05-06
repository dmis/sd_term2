from datetime import date
from classes.Department import Department
from classes.Employees import Employee, CEO, Head, TeamLeader, Developer
from classes.Enumerates import Position
from classes.Activities import ActivitiesImpl


if __name__ == "__main__":
    activity = ActivitiesImpl()
    ceo = CEO('Timothy Donald Cook', 1000000,
              date(1998, 6, 3))
    company = Department('Apple', ceo, activity)

    hosd = Head('John Smith', 10000, date(2015, 6, 3))
    sd = Department('Strategy department', hosd, activity)
    e1 = Developer('Ann', 1000, date(2019, 6, 3))
    sd.hire(e1)
    e2 = Developer('Kate', 2000, date(2020, 6, 3))
    sd.hire(e2)
    company.add_department(sd)

    hod = Head('Neo', 1500, date(2008, 6, 3))
    dd = Department('Development department', hod, activity)
    e3 = Developer('Mary', 1200, date(2019, 6, 3))
    dd.hire(e3)
    e4 = Developer('Alex', 1500, date(2020, 6, 3))
    dd.hire(e4)
    company.add_department(dd)

    ceo2 = CEO('Satya Nadella', 1000000,
               date(1998, 6, 3))
    company2 = Department('Microsoft', ceo2, activity)
    # ---  HA 04 -------
    # --- Compare companies by staff size(A > B = True)
    print('staff size of company :', len(company.all_employees()))
    print('staff size of company2 :', len(company2.all_employees()))
    assert company >= company2
    print(company >= company2)
    assert company2 <= company
    print(company <= company2)
    assert company != company2
    print(company != company2)
    assert company == company
    print(company == company2)

    print('\nCheck  salary before increasing')
    for i in sd.employees:
        print(i.name + ' : ' + str(i.salary))
    sd.change_salary(True, 10)

    print('\nCheck  salary after increasing')
    for i in sd.employees:
        print(i.name + ' : ' + str(i.salary))

    print('\nSearch employees with salary more than 0 but less than 1500')
    fltr = company.select_workers_by_salary(0, 1500)
    for i in fltr:
        print(i.name + ' : ' + str(i.salary))

    print('\nSearch employees with position Head')
    fltr2 = company.all_employees(Position.HEAD_OF_DEPARTMENT)
    for i in fltr2:
        print(i.name + ' : ' + str(i.position.value))

    print('\n All employees list ')
    all = company.all_employees()
    for a in all:
        print(a.name + ' | ' + a.department.name + ' | ' + a.position.value)
