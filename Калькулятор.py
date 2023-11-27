a = input('+, -, /, *')
a2 = int(input('перше число'))
a3 = int(input('друге число'))

if a == "+":
    print(a2+a3)
elif a =="-":
    print(a2-a3)
elif a == "/":
    if a2 == 0:
        print("На 0 ділити не можна")
    elif a3 == 0:
        print("На 0 ділити не можна")
    else:
        print(a2/a3)
elif a == "*":
    print(a2*a3)
else:
    print('Такого значення нема')