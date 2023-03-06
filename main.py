import random


def timestamp_to_date(timestamp):
    days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # количество дней в месяце
    year = 1970
    beginning_days = timestamp // (24 * 60 * 60)  # Дни с начала эпохи
    count_seconds = timestamp % (24 * 60 * 60)  # Количество секунд после вычета дней с начала эпохи
    leap_year = False  # Високосный год или нет
    while beginning_days >= 365:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            leap_year = True
            if beginning_days < 366:
                break

            beginning_days -= 366
        else:
            beginning_days -= 365

        year += 1

    # Включаем текущий день (для подсчета времени)
    count_days = beginning_days + 1  # Количество оставшихся дней после вычета лет
    month = 0     # Счёт месяцев
    month_index = 0
    if leap_year:
        while True:
            if month_index == 1:  # февраль(високосный год)
                if count_days - 29 < 0:
                    break

                month += 1
                count_days -= 29
            else:
                if count_days - days_month[month_index] < 0:
                    break

                month += 1
                count_days -= days_month[month_index]

            month_index += 1
    else:
        while True:
            if count_days - days_month[month_index] < 0:
                break

            month += 1
            count_days -= days_month[month_index]
            month_index += 1
    if count_days > 0:     # Подсчет дня
        month += 1
        day = count_days
    else:
        if month == 2 and leap_year == 1:
            day = 29
        else:
            day = days_month[month - 1]

    hours = count_seconds // (60 * 60)     # Подсчет времени
    minutes = (count_seconds % (60 * 60)) // 60
    seconds = (count_seconds % (60 * 60)) % 60

    print(str(year) + "-" + str(month) + "-" + str(day))
    print(str(hours + 4) + ":" + str(minutes) + ":" + str(seconds))


def search_min(lst):
    minim = lst[0]
    for j in range(len(lst)):
        if minim > lst[j]:
            minim = lst[j]
    return minim


if __name__ == "__main__":
    ts = 1678003932
    timestamp_to_date(ts)
    lst = []
    for i in range(random.randint(5, 15)):
        lst.append(random.randint(-10, 15))
    print("С неотсортированным списком:")
    print(str(lst))
    print("Минимальное со сложностью O(n): " + str(search_min(lst)) + "\n")
    print("С отсортированным списком:")
    lst = sorted(lst)
    print(lst)
    print("Минимальное со сложностью O(1): " + str(lst[0]) + "\n")
