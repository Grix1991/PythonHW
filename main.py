# Задачи с семинара 1

# # task 1
# n = 700 # проезжаем в день
# m = 1400 # должны проехать

# print((m + n - 1) // n)


# про парты
# task 3 первое решение
# a = 20
# b = 21
# c = 22
# a1 = (a + 1) // 2
# b1 = (b + 1) // 2
# c1 = (c + 1) // 2
# print(a1 + b1 + c1)

# task 3 второе решение
# first = int(input('Первый класс '))
# second = int(input('Второй класс '))
# three = int(input('Третий класс '))
# sum = (first + 1) // 2
# sum2 = (second + 1) // 2
# sum3 = (three + 1) // 2
# print(sum + sum2 + sum3)





# 5. Вагоны в электричке пронумерованы натуральными числами, начиная с 1 
# (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; 
# это зависит от того, в какую сторону едет электричка). В каждом вагоне написан
# его номер. Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j.
# Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет 
# это делать или сообщать, что без дополнительной информации это сделать невозможно.

# **Input:**
# 3
# 4

# **Output:**
# 6

# i = int(input('i-ый вагон '))
# j = int(input('j-ый вагон '))
# if j != i:
#     total = i+j-1
# else:
#     total = 'невозможно'
# print(f'всего вагонов: {total}')

# # task 5 
# i = int(input('i = '))
# j = int(input('j = '))
# if i == j:
#     print('Мало данных')
# else:
#     print(i + j - 1)





# print("Определить является ли год високосным.")
# y = int(input("Введите год: "))
# if y % 4 == 0:
#     if y % 100 == 0:
#         if y % 400 == 0:
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print("YES")
# else:
#     print("NO")

# # task 7
# n = 2018
# if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
#     print('yes')
# else:
#     print('no')
