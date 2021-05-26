import cmath

'''ac1="Python is popular"
b=ac1.replace('Python','java')
print(ac1)
c=b.split( )
c[0]="JAVA"
d=' '.join(c)
print(b)
print(c)
print(d)

a={'name':'xuqiang','sex':'nan','province':'四川'}
a['province']="江苏"
print(a)
Test_str="Python was  created in 1989,Python is  using in AI,big data,IOT."
#第一题
print(Test_str.lower())
print(Test_str.split())
b=Test_str.split()
print(','.join(b))

list1 = ['python', 5, 6, 8]
list2 = ['python', 5, 6, 8, 10]
a = list1 + list2
print(a)
b = set(a).difference()
print(b)

a = input("请输入1个加数:")
a = int(a)
b = input("请输入另外一个加数")
b=int(b)
print(a+b)
money = 1000
s = int(input("请输入整数："))
if s % 2 == 0:
    print(s, "是偶数")
else:
    print(s, "是奇数")'''
'''
score = int(input("请输入一个成绩"))
if 90 <= score <= 100:
    print("A级")
elif 80 <= score <= 89:
    print("B级")
elif 70 <= score <= 79:
    print("C级")
elif 60 <= score <= 69:
    print("D级")
elif 0 <= score <= 59:
    print("不及格")
else:
    print("对不起成绩不合格")'''
'''
    会员 》=200 8折
        >=100 9折
        不打折
    非会员>=200 9.5折
        不打折

anser = input("您是会员吗？y/n")
money = float(input("请输入您的购物金额"))
if anser == "y":
    if money >= 200:
        print("打八折，付款金额为：", money * 0.8)
    elif money >= 100:
        print("打9折，付款金额为：", money * 0.9)
    else:
        print("不打折")
else:
    if money >= 200:
        print("打95折，付款金额为：", money * 0.95)
    else:
        print("不打折，付款金额为：", money)'''
'''range()函数'''
print(range(10))
