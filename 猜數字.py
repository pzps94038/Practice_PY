import tkinter as tk
import random
window = tk.Tk()
window.title('猜數字')
window.geometry('800x600')
window.configure(background='yellow')
電腦=random.randint(1,99)
c=0
small=1
big=99 
def max():
    global c
    global small
    global big          
    me=int(digital_entry.get())
    if me<電腦:
        if me<small:
            small=me+1
            xxxx = '{}~{}猜大一點'.format(small, big)
            c=c+1
            print(xxxx)
        else:
            small=me+1
            xxxx = '{}~{}猜大一點'.format(small, big)
            print(xxxx)
            c=c+1
    elif me==電腦:
        xxxx="猜對了共花了{}場".format(c)
        print(xxxx)        
    else:
        if big>me:
            big=me-1
            xxxx = '{}~{}猜小一點'.format(small, big)
            c=c+1
            print(xxxx)
        else:
            xxxx = '{}~{}猜小一點'.format(small, big)
            c=c+1
            print(xxxx)
    xxxx_label.configure(text=xxxx)
header_label = tk.Label(window, text='猜數字遊戲', font=('Arial', 30))
digital_label = tk.Label(window, text='猜數字', font=('Arial', 30))
digital_entry = tk.Entry(window, font=('Arial', 30))
button_btn = tk.Button(window, text='按鈕',command=max,font=('Arial', 30))
xxxx_label=tk.Label(window,font=('Arial', 15), width=30, height=3)
# 版面配置
header_label.grid(row=0, column=0, columnspan=2)
digital_label.grid(row=1, column=0)
digital_entry.grid(row=1, column=1)
button_btn.grid(row=2, column=0)
xxxx_label.grid(row=2, column=1)

window.mainloop()