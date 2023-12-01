a = input('Вдетіть слово')
list = a.split()
g = ""
for i in list:
    g += i[: : -1] + ""
print(g)