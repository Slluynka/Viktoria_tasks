listin=[128,135,60,46,5,66]
def sort_select(listin):
    #шукаємо максимальне значення і його індекс
    k=0
    while  k<=len(listin)-1:
        i=k+1
        maxval=listin[k]
        maxind=k
        while i<=len(listin)-1:
            if maxval<listin[i]:
                maxval=listin[i]
                maxind=i
            i+=1
        #перший maxval знайдено
        #міняємо місяцями значення максимального з k-тим значенням
        listin[maxind] = listin[k]
        listin[k] = maxval
        k+=1
    return listin
print(listin)
print(sort_select(listin))
