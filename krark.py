from numpy import random
import tkinter


krark = tkinter.Tk()
krark.title('Krark Flips')
krark.geometry("350x250")

def start(thum, krarks):
    
    n=krarks
    thumb = False
    
    if thum.get()==1:
        thumb = True

    flips = []

    if not thumb:

        for i in range(1,n+1):
            flips.append(random.choice([-1,1]))
        
        l.config(text = "Wins : "+str(flips.count(1))+"\n"+"Losses : "+str(n - flips.count(1)))

    if thumb:
        
        for i in range(1,n+1):
            flips.append([random.choice([-1,1]), random.choice([-1,1])])
            
        l.config(text = "Both Wins : "+str(flips.count([1,1]))+"\n"+"Half Wins : "+str(flips.count([1,-1]) + flips.count([-1,1]))+"\n"+"Both Losses : "+str(flips.count([-1,-1])))
        


thum = tkinter.IntVar()
krarks = 10

C1 = tkinter.Checkbutton(text = "Thumb", variable = thum, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)


button_1 = tkinter.Button(text = 'Start', width = '10', height = '1', command=lambda: start(thum, int(E1.get())))

l = tkinter.Label(bg='white', width=20, height = 200, text='')

E1 = tkinter.Entry(bd =5)

C1.pack(side = "top")
button_1.pack(side = "bottom", pady = 15)
E1.pack(side="top", pady=15)
l.pack(ipadx=10, ipady=10)
krark.mainloop()
