'''
用户输入&while循环
'''

'''
#input（）
prompt = '邀请您参与我们的小测试，'
prompt += '\n请输入您的幸运数字：'
p = input(prompt)
print(f'wow,原来您的幸运数字是：{p}。')
#int()
num = int(p)
if num >= 7:
    print('int类型的7')

#求模mu运算符
num1 = 7 % 3
print(num1)
num2 = 4 % 2
print(num2)

#练习 7-1 汽车租赁
messagae = input('请问您想咨询什么类型的车？')
print(f'好的，现在让我来为您介绍{messagae}这款车。')

#练习 7-2 餐馆定位
desks = int(input('请问您几位用餐？'))
if desks > 8 :
    print('sorry,这边暂时无8人以上的桌。')
else:
    print(f'好的，这边已帮您预定{desks}人桌。')

#练习 7-3 10的整倍数
num3 = int(input('请输入：'))
print('为您计算该值是否为10的整倍数')
num4 = num3 % 10
if num4 != 0 :
    print(f'{num3}：不是10的整倍数。')
else:
    print(f'{num3}：是10的整倍数。')

#while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#用循环决定推出
message1341 = '若确定参加小测试请输入：'
message1341 += '\n若推出请输入"quit"'
mess = ""
while mess != 'quit':
    mess = input(message1341)
    if mess != 'quit':
        print(mess)
    else:
        print('您已退出。')

#标志
message1342 = '若确定参加小测试请输入：'
message1342 += '\n若退出请输入"quit"'
active = True

while active:
    mess = input(message1342)
    if mess == 'quit':
        active = False
        print('您已退出。')
    else:
        print(mess)

#while True,break
message1343 = '若确定参加小测试请输入：'
message1343 += '\n若退出请输入"quit"'

while True:
    mess = input(message1343)
    if mess == 'quit':
        print('您已退出。')
        break
    else:
        print(mess)

#continue
num = 0
while num < 10:
    num += 1
    if num % 2 ==0:
        print(num)
        continue
print('结束')

#练习 7-4 比萨配料

while True:
    add = input('(按quit结束)请输入添加配料：')
    if add == 'quit':
        print('好的，我们将为您添加您已选择的配料')
        break
    else:
        print(f"add:{add}")

#练习 7-5 电影票
age = '输入您的年龄为您计算票价'
age += '请输入您的年龄：'
while True:
    ages = int(input(age))
    if ages < 3:
        print('3岁（不含）以下年龄免费.')
        break
    elif ages < 12 :
        print('3岁（含）——12岁（不含）以内年龄$10.')
        break
    else:
        print('12岁（含）以上年龄$15.')
        break
print('请根据年龄买票。')


#使用while处理列表和字典
#在列表之间移动元素
old_users = ['zhang','li','wang']
new_users = []
while old_users:
    new = old_users.pop()
    new_users.append(new.title())

print('new user :')
for n in new_users:
    print(n)

pets = ['cat','cat','cat','dog']
while 'cat' in pets:
    pets.remove('cat')
for p in pets:
    print(p)

#使用用户输入来填充字典
diaocha = {}
active = True
while active:
    name = input('输入您的姓名：')
    answer = input('输入您的意见：')
    # 添加字典键值
    diaocha[name] = answer
    an = input('是否还要继续调查：（yes/no）')
    if an == 'no':
        active = False
        print('您已结束调查')
for name,answer in diaocha.items():
    print(f'{name}:{answer}')

#练习 7-8 熟食店
sandwish_orders = ['ff','ww','ee','ee','ee']
new_sandwish = []
while sandwish_orders:
    new = sandwish_orders.pop()
    new_sandwish.append(new)
    print(f'I made your {new} sandwish.')
for n in new_sandwish:
    print(n)

#练习 7-9 五香熏牛肉卖完了
orders = ['ff','ww','ee','ee','ee']
print('ee卖完了')
while 'ee' in orders:
     orders.remove('ee')
     continue
print(f'now have {orders}')


#梦想的度假胜地
shengdi = {}
active = True
while active:
    name = input('姓名：')
    answer = input('城市：')
    shengdi[name] = answer
    jixu = input('是否还要回答？（yes/no）')
    if jixu == 'no':
        print('结束调查')
        active = False
for name,answer in shengdi.items():
    print(f'{name}:{answer}')
'''



