import tkinter as tk
import bs4, requests
window = tk.Tk()
window.title('News')
window.geometry('1080x900')
window.configure(background='black')                 
def hots():
    x=''
    url = 'https://www.ettoday.net/news/hot-news.htm'   
    html = requests.get(url)
    print("網頁下載中 ...")
    html.raise_for_status()                             # 驗證網頁是否下載成功                      
    print("網頁下載完成")
    objSoup = bs4.BeautifulSoup(html.text, 'lxml')      # 建立BeautifulSoup物件
    # 找尋新聞
    news = objSoup.find_all('div', {'class':'piece clearfix'})
    print("前5個新聞順序: ")
    for i in range(5):       
        x=x+news[i].text+' '
    ans_label.configure(text=x)
def socs():
    x=''
    url = 'https://www.ettoday.net/news/focus/%E7%A4%BE%E6%9C%83/'   
    html = requests.get(url)
    print("網頁下載中 ...")
    html.raise_for_status()                             # 驗證網頁是否下載成功                      
    print("網頁下載完成")
    objSoup = bs4.BeautifulSoup(html.text, 'lxml')      # 建立BeautifulSoup物件
    # 找尋新聞
    news = objSoup.find_all('div', {'class':'piece clearfix'})
    print("前5個新聞順序: ")
    for i in range(5):       
        x=x+news[i].text+' '
    ans_label.configure(text=x)
def pols():
    x=''
    url = 'https://www.ettoday.net/news/focus/%E6%94%BF%E6%B2%BB/'   
    html = requests.get(url)
    print("網頁下載中 ...")
    html.raise_for_status()                             # 驗證網頁是否下載成功                      
    print("網頁下載完成")
    objSoup = bs4.BeautifulSoup(html.text, 'lxml')      # 建立BeautifulSoup物件
    # 找尋新聞
    news = objSoup.find_all('div', {'class':'piece clearfix'})
    print("前5個新聞順序: ")
    for i in range(5):       
        x=x+news[i].text+' '
    ans_label.configure(text=x)
def Non():
    x=''
    ans_label.configure(text=x)
News_label = tk.Label(window, text='當日新聞前五則', font=('Arial', 30))
hots_btn = tk.Button(window, text='熱門新聞',command=hots,font=('Arial',24))#熱門按鈕呼叫熱門函式
soc_btn = tk.Button(window, text='社會新聞',command=socs,font=('Arial', 24))#社會按鈕呼叫社會函式
pol_btn = tk.Button(window, text='政治新聞',command=pols,font=('Arial', 24))#政治按鈕呼叫政治函式
Non_btn = tk.Button(window, text='清除',command=Non,font=('Arial', 24))#清除按鈕呼叫清除函式

ans_label=tk.Label(window,font=('Arial',10,), width=80, height=40,justify = 'left',wraplength = 600)
# 版面配置
News_label.grid(row=0, column=2)
hots_btn.grid(row=1, column=1)
soc_btn.grid(row=1, column=2)
pol_btn.grid(row=1, column=3)
Non_btn.grid(row=4, column=3)
ans_label.grid(row=2, column=2,rowspan=2)

window.mainloop()