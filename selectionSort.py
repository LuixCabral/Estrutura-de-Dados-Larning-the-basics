arrai = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(arrai)

for i in range(n-1):
    index_Minimo= 1
    for j in range(i+1,n):
        if arrai[j] < arrai[index_Minimo]:
            index_Minimo = j
    arrai[i], arrai[index_Minimo] = arrai[index_Minimo], arrai[i]

print("array organizada", arrai)

        

