import re

binary_7: str = input("Введите семизначный бинарный код: ")
while bool(re.search(r'[^10]', binary_7)) or (len(binary_7) != 7):
    print("Вы ввели недопустимое значение")
    binary_7 = input("Введите семизначный бинарный код: ")

lst = []
for letter in binary_7:
    lst.append(int(letter))
print("Введённый бинарный код: ", lst)
print("Введённые информационные биты: ", lst[2], lst[4], lst[5], lst[6])

r1_source, r2_source, r3_source = lst[0], lst[1], lst[3]
r1_res = (lst[2] + lst[4] + lst[6]) % 2
r2_res = (lst[2] + lst[5] + lst[6]) % 2
r3_res = (lst[4] + lst[5] + lst[6]) % 2
s1 = (r1_res + r1_source) % 2
s2 = (r2_res + r2_source) % 2
s3 = (r3_res + r3_source) % 2
err_bit: int = (s1 + s2 * 2 + s3 * 4) - 1
print("Неправильный бит: ", err_bit + 1)
lst[err_bit] = (lst[err_bit] + 1) % 2

print("Правильный бинарный код: ", lst)
print("Правильные информационные биты: ", lst[2], lst[4], lst[5], lst[6])
