# Код к домашнему заданию «Import. Module. Package»

1. Разработана структуру программы «Бухгалтерия»:
- main.py;
- application/salary.py;
- application/db/people.py.
Main.py — основной модуль для запуска программы.
В модуле salary.py присутствует функция calculate_salary.
В модуле people.py есть функция get_employees.

2. Импортированы функции в модуль main.py. а также вызваны в конструкции:
`if __name__ == '__main__':`
Добавлен вывод.

3. Познакомился с модулем datetime. При вызове функций модуля main.py выводится текущая дата и время.

4. Найден интересный для себя пакет на pypi - cryptochaos (с одним форком и нолём звёзд). Он установлен в окружение, но не импортирован. В файле requirements.txt указал его с актуальной версией. Желания написать программу с этим пакетом не возникло.