a=int(input("請輸入第一次期中考成績?"))
b=int(input("請輸入第二次期中考成績?"))
c=int(input("請輸入期末考成績?"))
print("總分為",a+b+c,"平均為",(a+b+c)/3)
#%%
a=int(input("請輸入幾尺"))
b=int(input("請輸入幾吋"))
c=((a*12)+b)*2.54
print("轉換成",c,"公分")
#%%
a=int(input("請輸入購買飲料的罐數?"))
if  a>12:
    print("需花費",(a//12)*200+(a%12)*20)
else:
    print("需花費",a*20)
#%%
a=str(input("請輸入一句英文句子"))
b=a.split(" ")
print("拿到字元",b)
c=(" ").join(b)
print("組合",c)
print("字首大寫",c.title())
#%%
s=0#設定一個數字為0
for x in range(1,100,1): #設定一個迴圈 從1開始 到100不包含100結束 每次間隔1
    s=s+x #設定s=s+x 是因為 如果設定一個新的值d=s+x 只會一直讓s不斷+新的x導致顯示出來的一直只會是x目前的值
    print("1+100",s)