key = int(input("""key??
2
3 
4
="""))
text = input("mein text:")
text = text.lower()
text = text.split()
f2 = 2
f3 = 3
f4 = 4
hft = ""


if key == 2:
    for x in range(0, len(text)):
        text1 = []
        text2 = []
        text[x] = list(text[x])
        for i in range(1, len(text[x]), 2): 
            text1.append(text[x][i])  
              
        for i in range(0, len(text[x]), 2): 
            text2.append(text[x][i])
        
        for i in text:
            textmein = text1+text2
            
        print(textmein)