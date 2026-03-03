# Задание: 1
# price = int(input())
# sale = int(input())
# sale_in = price - (price * sale // 100)
# print("Скидка: ", price - sale_in)
# print("Оплата: ", sale_in)


# Задание 2
# a = int(input())
# if a % 2 == 0:
#     if a > 100:
#         print("Четное и > 100")
#     else:
#         print("Четное и <= 100")
# else:
#     print("Нечетное")

# Задание 3
# a = map(int, input().split())
# sum = 0
# for i in a:
#     if i >= 0:
#         sum += i
# print(sum)

# Задание 4
# cnt_gb = int(input("Количество: "))
# flag = int(input())
# sum = 1000
# total = 0
# if cnt_gb > 50:
#     sum += 300
# if cnt_gb > 100:
#     sum += 500
#
# if flag == 1 :
#     total = sum - (sum * 20 // 100)
# print(total)


# Задание 5
# age = int(input())
# salary = int(input())
# flag = int(input())
# if age < 18:
#     print("Отказ: вам меньше 18")
# elif flag == 1:
#     print("Отказ: есть задолженности")
# elif salary < 30000:
#     print("Отказ: маленькая зарплата")
# else:
#     print("Кредит одобрен")


# Задание 6
# mark = int(input())
# if 100 >= mark >= 0:
#     if 90 <= mark <= 100:
#         print("Отлично")
#     elif 70 <= mark < 90:
#         print("Хорошо")
#     elif 50 <= mark < 70:
#         print("Удовлетворительно")
#     else:
#         print("Плохо")
# else:
#     print("ERROR")


# Задание 7
# a = list(map(int, input().split()))
# x = 0
# y = 0
# for i in a:
#     if i % 2 == 0:
#         x += 1
#     else:
#         y += 1
# print("Четных: ", x)
# print("Нечтных: ", y)


# Задание 8
# a = list(map(int, input().split()))
# sum = 0
# five = 0
# four = 0
# three = 0
# two = 0
# one = 0
# avg_cnt = 0
# for i in a:
#     sum += i
#     avg_cnt += 1
#     if i == 5:
#         five += 1
#     elif i == 4:
#         four += 1
#     elif i == 3:
#         three += 1
#     elif i == 2:
#         two += 1
#     elif i == 1:
#         one += 1
# print(sum / avg_cnt)
# print("Кол-во пятерок: ", five)
# print("Кол-во четверок: ", four)
# print("Кол-во троек: ", three)
# print("Кол-во двоек: ", two)
# print("Кол-во однерок: ", one)
# if 0 <= sum / avg_cnt <= 5:
#     if sum / avg_cnt >= 4.5:
#         print("Группа молодцы!")
#     elif 3 <= sum / avg_cnt < 4.5:
#         print("Нужно подтянуться!")
#     elif sum / avg_cnt < 3:
#         print("Группа нужно серьезно поработать!")
# else:
#     print("ERROR")


# Задание 9
a = list(map(int, input().split()))
base = int(input())
cnt = 0
truly = [0] * len(a)
for i in a:
    if i < base:
        print(i)
        base -= i
        truly[cnt] = i
        cnt += 1
print(cnt)
mn = 1902381209312
mx = 0
for i in truly:
    if i < mn:
        mn = i
    if i > mx:
        mx = i
print("Minimum: ", mn, "Maximum: ", mx)

# Задание 10
# a = list(map(int, input().split()))
# sum = 0
# avg_cnt = 0
# for i in a:
#     sum += i
#     avg_cnt += 1
# print(sum)
# print(sum / avg_cnt)
# mx = 0
# for i in a:
#     if i > mx:
#         mx = i
# print(mx)
# if sum / avg_cnt < 300:
#     print("Economniy")
# elif 300 <= sum / avg_cnt <= 700:
#     print("Normalniy")
# else:
#     print("Bez finansovoy gramotnosti")