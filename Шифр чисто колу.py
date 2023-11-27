from tkinter import*

g = Tk()
g.title("Шифр")
g.geometry("600x500")
g.resizable(width=False, height=False)

frame = Frame(g, bg="yellow")
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text="Ведіть текст для шифрування", bg="gray", font=42)
title.pack()


key123 = Entry(frame, bg="white")
key123.pack()

keyy = Label(frame, text="Ключ для шифру", bg="gray", font=42)
keyy.pack()

def baton1():
    teext = key123.get()
    teext.lower()
    teext.split()
    
    for x in range(0, len(teext)):
        teext[x] = list(teext[x])
        text1 = []
        text2 = []
        for i in range(1, len(teext[x]), 2): 
            text1.append(teext[x][i])  
              
        for i in range(0, len(teext[x]), 2): 
            text2.append(teext[x][i])
        
        for i in teext:
            hft = text1+text2 
    
    sam_text = Tk()
    sam_text.geometry("600x500")
    sam_text2 = Label(sam_text, text= hft, font = 30)
    sam_text2.pack()
    sam_text.mainloop()
    

btn = Button(frame, text="ключ 2:", bg="gray", command=baton1)
btn.pack()

def baton2():
    hft = ""
    pass 
    
    sam_text = Tk()
    sam_text.geometry("600x500")
    sam_text2 = Label(sam_text, text= hft, font = 30)
    sam_text2.pack()
    sam_text.mainloop()

btn1 = Button(frame, text="ключ 3:", bg="gray", command=baton2)
btn1.pack()

def baton3():
    hft = ""
    pass
    
    sam_text = Tk()
    sam_text.geometry("600x500")
    sam_text2 = Label(sam_text, text= hft, font = 30)
    sam_text2.pack()
    sam_text.mainloop()

btn2 = Button(frame, text="ключ 4:", bg="gray", command=baton3)
btn2.pack()



g.mainloop()
   