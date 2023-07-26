import datetime

from application.db.people import get_employees
from application.salary import calculate_salary


if __name__ == '__main__':
    current_date = datetime.datetime.now()
    print(f"Текущая дата: {str(current_date)[:10]}\nТочное время: {str(current_date)[11:19]}\n")

    print("Имена наших сотрудников:\n")
    for employee in get_employees():
        name = employee["name"]
        print(name)
    print()
    print("Для вывода зарплаты сотрудника введите его данные.\n")
    staff_name = input("Имя и фамилия сотрудника:\n")
    number_months = int(input("Введите число месяцев для подсчёта:\n"))

    #print(f"Employees: {get_employees()}")
    print(f"Зарплата {staff_name} за {number_months} мес.: {calculate_salary(get_employees(),staff_name, number_months)} руб. 00 копеек")