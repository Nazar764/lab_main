a = input('text:')
a = a.lower()
hft = ""

# виключення з тексту лишніх символів   
sam = ["1", "2", "3", '4', '5', '6', '7', '8', '9', '0', '!', "@", "#", ":", ';', ',', ".", "?", "/"]
for i in sam:
    a = a.replace(i, '')


b = sorted(set(a.split(' ')))
abc = [0]*58

for i in a:
    if 'a' <= i <= 'z':
        abc[ord(i) - ord('a')] += 1
    elif 'а' <= i <= 'я':
        abc[ord(i) - ord('а') + 26] += 1


g = str(input('''
Порахувати текст: - 
Вивести слова: +
= '''))

if g == "-":
    for i in range(26):
        if abc[i] > 0:
            print(chr(i + ord('a')),'=', abc[i])
    
    for i in range(26, 58):
        if abc[i] > 0:
            print(chr(i + ord('а') - 26),'=', abc[i])
          
elif g == "+":
    for i in b:
        if len(i) >= 4:
            hft = hft + i            
            print(hft)