# Про орбиты

from random import randint

planets = 10
list_of_orbits = [(randint(1, 10), (randint(1, 10))) for i in range(planets)]

print(list_of_orbits)

def find_farthest_orbit(list_of_orbits):
    maximumS = 0
    max = 0
    count = 0
    for item in list_of_orbits:
        S = item[0] * item[1] * 3.14 #округляем П. Для правильного нахождения планеты этого должно быть достаточно
        count += 1
        if S > maximumS:
            maximumS = S
            max = count
    #Печатаю площадь и номер планеты для проверки
    print(S)
    print(max)
    return list_of_orbits[max - 1]

print(f"самая дальняя планета {find_farthest_orbit(list_of_orbits)}")
