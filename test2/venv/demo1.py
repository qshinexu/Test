'''a=0
sum=0
while a<5:
    sum+=a
    a+=1
print("和为",sum)'''


'''求1-100的偶数和改为ifa%2就是奇数和'''
'''
sum=0
a=1
while a<=1000:
    if a%2:
        sum+=a
    a+=1
print("1-100的偶数和",sum)'''


'''用for循环求1-100之间的偶数和'''
'''
sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i
print(sum)'''


'''输出100-999之间的水仙花数：水仙花数是个位的3次方加十位的3次方加百位的3次方之和'''
'''
for i in  range(100,1000):
    ge=i%10
    shi=i//10%10
    bai=i//100
    #print(ge,shi,bai)
    if ge**3+shi**3+bai**3==i:
        print(i)'''

'''break语句从键盘录入密码，最多录入3次，如果正确就结束循环'''
'''
for i in range(3):
    pwd=input("请输入密码：")
    if pwd=="8888":
        print("密码正确")
        break
    else:
        print("密码不正确")'''
#使用while配合break使用
'''
a=0
while a<3:
    pwd=input("请输入密码！")
    if pwd=="8888":满足什么样的条件就退出
        print("密码正确")
        break
    else:
        print("密码错误")
    a+=1'''

'''continue语句要求输出1到50之间的所有5的倍数：和5的余数为0的数
    与5的余数不是5的倍数
'''
'''
for i in range(1,51):
    if i%5==0:
        print(i)
print("使用continue")

for i in  range(1,51):
    if i%5!=0:
        continue
    print(i)
'''

'''else语句'''
'''
for i in range(3):
    pwd=input("请输入密码！")
    if pwd=="8888":
        print("密码正确")
        break
    else:
        print("密码不正确")
else:
    print("对不起，三次密码都不正确")'''
'''while实现与else配合
a=0
while a<3:
    pwd=input("请输入密码")
    if pwd=="8888":
        print("密码正确")
        break
    else:
        print("密码不正确")
    a+=1
else:
    print("三次密码输入错误")
    '''

#嵌套查询,外层控制行数，内层管理每行个数
'''
for i in  range(1,4):
    for j in  range(1,5):
        print('*',end='\t')
    print()

#九九乘法表
for i in  range(1,10):
    for j in  range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()'''

#二重循环的流程控制语句break和continue只用于本层的循环
'''
for i in range(5):
    for j in  range(1,11):
        if j%2==0:
            #break
            continue
        print(j,end='\t')
    print()
'''
