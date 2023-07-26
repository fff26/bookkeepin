def calculate_salary(list_employees: list, name: str, month_nums: int)-> int:
    """Функция принимаетсписок словарей сотрудников и возвращает размер зарплаты
    по имени сотрудника за заданное количество месяцев """

    for list_employee in list_employees:
        if list_employee["name"] == name:
            return list_employee["salary"] * month_nums