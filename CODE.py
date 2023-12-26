#Задача: Написать программу, которая из имеющегося массива строк формирует новый массив из строк, длина которых меньше, 
#либо равна 3 символам. Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма. 
#При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.

#Примеры:
# “Hello”, “2”, “world”, “:-)”] → [“2”, “:-)”]
# “1234”, “1567”, “-2”, “computer science”] → [“-2”]
#“Russia”, “Denmark”, “Kazan”] → [] 


def filter_strings(strings):
    new_strings = []
    for string in strings:
        if len(string) <= 3:
            new_strings.append(string)
    return new_strings

# Пример использования
input_strings = input("Введите строки через запятую: ").split(",")
filtered_strings = filter_strings(input_strings)
print(filtered_strings)
