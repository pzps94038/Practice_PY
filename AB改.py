import tkinter as tk
import random

window = tk.Tk()
window.title('猜四位數')
window.geometry('800x600')
window.configure(background='red')
c=0
y=random.sample(range(1,9),4)
def z():
    ll=len(digital_entry.get())
    if ll>4:
        error="超過4個數字了"
        xxxx_label.configure(text=error)
    elif ll<4:
        error="小於4個數字了"
        xxxx_label.configure(text=error)
    else:
        x()        
def x():    
    A=0
    B=0
    global y
    x=list(digital_entry.get())    
    for c in range(0,4):##強制轉int去比較
        x[c]=int(x[c])#自己猜的數字字串一個一個抓出來轉換
    for i in range(0,4):                
        if x[i]==y[i]:
            A=A+1
    for b in range(0,4):
        for v in range(0,4):
            if x[b]==y[v]:
                B=B+1
                B=B-A
    nn='{}A{}B'.format(A,B)
    xxxx_label.configure(text=nn)        
    s.insert('end',str(x)+':'+nn+"\n")
header_label = tk.Label(window, text='猜四位數遊戲', font=('Arial', 30))
digital_label = tk.Label(window, text='猜數字', font=('Arial', 30))
digital_entry = tk.Entry(window, font=('Arial', 30))
button_btn = tk.Button(window, text='按鈕',command=z,font=('Arial', 30))
xxxx_label=tk.Label(window,font=('Arial', 15), width=30, height=3)
s=tk.scrolledtext.ScrolledText(window,height=20,width=30,font=('Arial',10))
s.insert('end','history:\n')
# 版面配置
header_label.grid(row=0, column=0, columnspan=2)
digital_label.grid(row=1, column=0)
digital_entry.grid(row=1, column=1)
button_btn.grid(row=2, column=0)
xxxx_label.grid(row=2, column=1)
s.grid(row=3, column=1)
window.mainloop()