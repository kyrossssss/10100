import random

numbers = []
for i in range(200):
    numbers.append(random.randint(0,200))
print(numbers)





print("Число 24 есть в нашем списке") if 24 in numbers else  print("Числа 24 нет в нашем списке")



