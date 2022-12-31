from datetime import date


def select_man(arr, person):
    """
    Вывод конкретных людей
    """
    result = []
    for employee in arr:
        if employee.get('name', person).lower() == person.lower():
            result.append(employee)

    # Возвратить список выбранных работников.
    return result