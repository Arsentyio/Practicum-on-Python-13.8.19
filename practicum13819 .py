a = int(input("Количество приобретаемых билетов "))
L = [int(input("Возраст "+ str(i+1) + "-го ")) for i in range(a)]
j = 0
for j in range(a):
    if L[j] < 18:
        L[j] = 0
    elif L[j] > 25:
        L[j] = 1390
    else:
        L[j] = 990
    print("Стоимость", (j+1), "-го билета ", L[j])
print("Количество билетов = ", a)
print("Полная стоимость =", sum(L))
if a > 3:
    print("Со скидкой 10% =", sum(L) * 0.9)