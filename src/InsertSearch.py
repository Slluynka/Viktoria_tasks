listin=[5,3,2,6,8,1,7,4,9]
def insertion_sort(listin):
    for i in range(len(listin)):
        val = listin[i]
        ind = i

        while ind > 0 and listin[ind-1] > val:
        #Змінюємо місцями число, просовуючи по списку
            listin[ind] = listin[ind-1]
            ind = ind - 1
        #Записуємо значення, яке ми запам'ятали спочатку
        listin[ind] = val
    return listin
print(listin)
print(insertion_sort(listin))