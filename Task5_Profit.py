print ("Введите значение выручки фирмы в рублях")
a = int(input ())
print ("Введите значение издержек фирмы в рублях")
b = int(input ())
c = a - b
if c > 0:
    print ("Ваша фирма работает с прибылью", c)
else:
    print ("Ваша фирма работает в убыток", c)
print ("Рентабельность выручки", c / a)
print ("Введите колличество сотрудников фирмы")
d = int(input ())
print ("Прибыль фирмы в расчете на одного сотрудника составляет:", c / d)