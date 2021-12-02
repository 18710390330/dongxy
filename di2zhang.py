'''
print("Hello Python World!")


name = "abc def"
#首字母大写
print(name.title())
#全大写
print(name.upper())
#全小写
print(name.lower())


first_name = "dong"
last_name = "xiaoying"
#字符串中使用变量
full_name = f"{first_name}{last_name}"
print(full_name)
#输出中使用变量
print(f"{first_name}{last_name}")
#字符串中使用变量拼接消息,且首字母大写
message = f"Hello,{first_name.title()}"
print(message)

#制表符&换行符
print(f"第一章\t变量\t{first_name}\n第二章\t数据类型\t{last_name}\n结束......")


favorite_language = "  python  "
print(favorite_language)
#剔除末尾空白,变量值不变
print(favorite_language.rstrip())
#剔除开头空白，变量值不变
print(favorite_language.lstrip())
#剔除首尾空白，变量值不变
print(favorite_language.strip())


#字符串不可同时出现三个单引号或三个双引号

#练习2-3
test_name = "eric"
print(f"Hello {test_name.title()},would you like to learn some Python today?")

#练习2-4
print(f"{test_name.title()}")
print(f"{test_name.upper()}")
print(f"{test_name.lower()}")

#练习2-5
print('迪丽热巴说：“本人比视频和照片更美！”')

#练习2-6
di_name = "迪丽热巴·迪力木拉提"
message1 = '说：“本人比视频和照片更美！“'
print(f"{di_name}{message1}")

#练习2-7
di2_name = " dilereba "
print(f"HI\t{di2_name.lstrip()}")
print(f"HI\n{di2_name.rstrip()}")
print(f"Hello {di2_name.strip()}")



#整数
print(3+2)
print(3-2)
print(3*2)
print(3/2)
#两个星号代表乘方运算
print(3**5)
#运算次序
print((3+2)*5)
#空格不影响计算
print((3+ 2) * 5)

#浮点数（带小数点的）
print(0.1+ 0.2)#0.30000000000000004暂时忽略小数位数
print(0.1*2)

#函数str()避免类型错误 int类型变量转string
age  = 23
message = "Happy"+str(age)+"rd Brithday"
print(message)

#在Python2中整数计算，若结果为小数，则直接会删除小数部分；解决办法：其中一个数为浮点数，例如3/2.0


#练习2-8
print(9-1)
print(7+1)
print(2*4)
print(16/2)

#练习2-9
num = 7
love_num = "my favorite number is\t"+str(num)
print(love_num)



num1 = 14_000_000
print(num1)

num2,num3,num4 = 15_000_000,1,2
print(num2,num3,num4)

NUM5 = 1000
NUM5 = 2000
print(NUM5)

'''






