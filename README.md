Лабораторна робота №9: Регулярні вирази в Python
Мета роботи:
Мета лабораторної роботи: Ознайомлення з використанням регулярних виразів для обробки текстових даних в Python.
Очікуваний результат: Набуття практичних навичок створення та використання регулярних виразів для пошуку та маніпуляції текстовими даними.
Опис завдання:
В цій лабораторній роботі потрібно було виконати декілька завдань, в кожному з яких потрібно написати функцію з регулярним виразом для розв’язання різноманітних задач, пов’язаних з обробкою рядків. Наприклад: перевірка формату електронної пошти, пошук IP-адрес, перевірка паролів тощо.
Виконання роботи:
Структура проекту:
Код розділений на різні функції, кожна функція відповідає за окреме завдання з відповідною назвою, наприклад: task1, task2, task3 тощо.
Опис файлів:
student_main.py: містить код Python з функціями для вирішення необхідних завдань.
README.md: описує структуру проекту, призначення кожного файлу, основні функції та методи з поясненням їх роботи тощо.
Опис основних функцій та методів з поясненням їх роботи:
task1(string): Перевіряє, чи рядок містить тільки малі літери та цифри.
Приклад використання:
python
Копировать код
import re

def task1(string):
    pattern = r'^[a-z0-9]+$'
    return bool(re.match(pattern, string))

# Приклад використання
print(task1("hello123"))  # Виведе: True
print(task1("Hello123"))  # Виведе: False
print(task1("hello_123"))  # Виведе: False
task2(string): Перевіряє, чи рядок містить принаймні одну велику літеру.
Приклад використання:
python
Копировать код
import re

def task2(string):
    pattern = r'[A-Z]'
    return bool(re.search(pattern, string))

# Приклад використання
print(task2("Hello"))  # Виведе: True
print(task2("hello"))  # Виведе: False
print(task2("HELLO"))  # Виведе: True
Результати:
Кожен рядок відповідає за виведення відповідної функції, тобто: 1 рядок - task1, 2 рядок - task2 і так далі.
Висновки:
Мета роботи була досягнута: були розглянуті та реалізовані різні методи обробки текстових даних за допомогою регулярних виразів у Python, також вийшло розібратися та почати розумітися в цій темі.
Інструкції з запуску:
Потрібно відкрити файл будь-яким зручним вам способом, головне щоб там був та працював інтерпретатор Python. Після цього потрібно додати необхідні виклики функцій, які присутні в файлі README.md. Після виконання цих дій нам потрібно лише запустити виконання файлу, після чого і виведуться необхідні нам дані.
