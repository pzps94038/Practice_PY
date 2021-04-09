姓名=[]#aa bb cc
學號=[]#11 22 33
成績=[]#AA BB CC
字典={"姓名字典":姓名,"學號字典":學號,"成績字典":成績}
選擇="n"
while 選擇!="y":
    name=input("請輸入姓名")
    姓名.append(name)
    student_id=input("請輸入學號")
    學號.append(student_id)
    grades=input("請輸入成績")
    成績.append(grades)
    選擇=input("是否要結束新增y/n")
查詢=input("請輸入要查詢的人")
index=姓名.index(查詢)
print(姓名[index],"查詢結果為","學號為",字典["學號字典"][index],"成績為",字典["成績字典"][index])
