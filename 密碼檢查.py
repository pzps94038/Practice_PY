a=input("密碼")
b=len(a)
數字=0
小寫=0
大寫=0
錯誤=0
for x in range(b):
    if a[x]>="0" and a[x]<="9":
        數字=數字+1
    elif a[x]>="a" and a[x]<="z":
        小寫=小寫+1
    elif a[x]>="A" and a[x]<="Z":
        大寫=大寫+1
    else:
        錯誤=錯誤+1
if 錯誤==0:
    if 數字==0:
        if 小寫+大寫<6:
            print("不安全的密碼")
        else:
            print("可能安全的密碼")
    elif 小寫==0 and 大寫==0:
        if 數字>6:
            print("可能安全的密碼")
        else:
            print("不安全的密碼")
    else: 
        if 數字+大寫+小寫<6:
            print("不安全的密碼")
        elif 數字+大寫+小寫>=6 and 數字+大寫+小寫<=10:
            print("安全的密碼")
        else:
            print("非常安全的密碼")
else:
    print("False")
def abc(oo):
    b=len(oo)
    數字=0
    小寫=0
    大寫=0
    錯誤=0
    for x in range(b):
        if a[x]>="0" and a[x]<="9":
            數字=數字+1
        elif a[x]>="a" and a[x]<="z":
            小寫=小寫+1
        elif a[x]>="A" and a[x]<="Z":
            大寫=大寫+1
        else:
            錯誤=+1
    if 錯誤==0:
        if 數字==0:
            if 小寫+大寫<6:
                print("不安全的密碼")
            else:
                print("可能安全的密碼")
        elif 小寫==0 and 大寫==0:
            if 數字>6:
                print("可能安全的密碼")
            else:
                print("不安全的密碼")
        else: 
            if 數字+大寫+小寫<6:
                print("不安全的密碼")
            elif 數字+大寫+小寫>=6 and 數字+大寫+小寫<=10:
                print("安全的密碼")
            else:
                print("非常安全的密碼")
    else:
        print("False")
abc(a)