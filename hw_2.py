
from random import randint, sample
#Створюємо функцію з трьома аргументами
def get_numbers_ticket(min_value,max_value,lenght):
    # додаємо клас set - неупорядкована множина унікальних елементів
    all_ticket = set()
    # Перебираємо випадковис чином з довжини множини яку задали 
    # в діапазоні унікальні елементи і додаємо їх в нову множину 
    # доки в нів не буде набрана кількість елементів що дорівнює змінній lenght
    while len(all_ticket) != lenght:
        all_ticket.add(randint(min_value,max_value))
    # Повертаємо утворену множину розміром lenght
    return(sorted(sample(range(min_value, max_value), lenght)))
# Викликаємо функцію та задаємо їй аргументи
lottery_numbers = get_numbers_ticket(1, 49, 6)
# Виводимо лотерейні числа
print("Ваші лотерейні числа:", lottery_numbers)


