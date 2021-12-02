'''
control+r 默认运行main.py文档
shift+control+r 运行选中文档，这之后再按control+r会运行选中文档
'''
'''
#if语句
cars = ['bmw','toyota','suzuki','sand']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#大小写会区分
ii = 'cici'
iii = 'Cici'
print(ii.title()==iii)
print(ii!=iii)
if ii != iii:
    print('ii不等于iii')
else:
    print('ii等于iii')
#数值比较
age = 17
age1 = 16
#一个条件时可以这样
if age and age1 < 18  :
    print('你们未满18岁')
else:
    print('恭喜你们，年龄符合！')
#不同条件时这样拼装
if age <= 11 and age1 <= 18 :
    print('你们未满18岁')
else:
    print('恭喜你们，年龄符合！')

#if-else:语句
age2 = 3
if age2 >= 18:
    print('您年满18。')
else:
    print('对不起，您未满18岁。')

#if-elif-else:语句
if age2 < 4:
    print('your admission cost is $0')
elif age2 <= 18:
    print('your admission cost is $25')
else :
    print('your admission cost is $40')

#多个elif模块
if age2 < 4:
    price = 0
elif age2 <= 18:
    price = 25
elif age2 < 65:
    price = 40
else:
    price = 20
print(f"your admission cost is ${price}")

#省略else模块
if age2 < 4:
    price = 0
elif age2 <= 18:
    price = 25
elif age2 < 65:
    price = 40
elif age2 >= 65:
    price = 20
print(f"your admission cost is ${price}")

#测试多个条件
requested_toppings = ['葱花','香菜','辣椒','醋']
if '葱花' in requested_toppings:
    add = '葱花'
    print(f'您要加{add}')
if '香菜' in requested_toppings:
    add = '香菜'
    print(f'您要加{add}')
if '辣椒' in requested_toppings:
    add = '辣椒'
    print(f'您要加{add}')
if '醋' in requested_toppings:
    add = '醋'
    print(f'您要加{add}')
print('请您核对！')

#练习5-3外星人颜色
alien_colour = 'green'
if alien_colour == 'green' :
    print('您射杀的是绿色机器人')
    print('获得5分！')
else:
    print('您射杀的不是绿色机器人')
    print('获得10分！')
#if-elif-else
if alien_colour == 'green':
    print('您射杀的是绿色机器人')
    print('获得5分！')
elif alien_colour == 'yellow':
    print('您射杀的是黄色机器人')
    print('获得10分！')
else:
    print('您射杀的是红色机器人')
    print('获得15分！')
#练习5-6人生的不同阶段
age3 = 2
if age3 < 2:
    print('这个人是婴儿')
elif age3 < 4:
    print('这个人是幼儿')
elif age3 < 13:
    print('这个人是儿童')
elif age3 < 20:
    print('这个人是青少年')
elif age3 < 65:
    print('这个人是成年人')
else:
    print('这个人是老年人')
#5-7水果练习
favorite_fruit = ['banana','apple','mango']
if 'banana' in favorite_fruit:
    print('you really like banana.')
if 'apple' in favorite_fruit:
    print('you really like apple.')
if 'mango' in favorite_fruit:
    print('you really like mango.')
if 'pear' in favorite_fruit:
    print('you really like pear.')
if 'pizza' in favorite_fruit:
    print('you really like pizza.')

#if语句处理列表
#检查特殊元素
request_peiliao = ['xiangcai','conghua','lajiao']
for request in request_peiliao:
    if request == 'xiangcai':
        print('sorry,xiangcai meiyoule.')
    else:
        print(f'adding{request}.')

request_pizzas = []
if request_pizzas:
    for request in request_pizzas:
        print(f'adding{request}')
    print('请您确认添加')
else:
    print('请确定是否购买原味pizza？')


available_toppings = ['qingcai','bocai','nangua']
requested_toppings1 = ['qingcai','machixian','qincai']
for requested in requested_toppings1:
    if requested in available_toppings:
        print(f'adding{requested}.')
    else:
        print(f'sorry,we don`t have {requested}.')
print('start making your pizza!')


#练习5-8
users = ['zhang','li','admin','wang','dong']
for user in users:
    if user == 'admin':
        print(f'Hello {user},would you like to see a status report?')
    else:
        print(f'Hello {user},thank you for logging in again.')
#练习5-9判断空列表
if users :
    for user in users:
        if user == 'admin':
            print(f'Hello {user},would you like to see a status report?')
        else:
            print(f'Hello {user},thank you for logging in again.')
else:
    print('We need to find some users!')

#练习5-10检查用户名
current_users = ['zhang','li','admin','wang','dong']
#current_users1 = current_users[:]
new_users = ['zhangs','LI','admin','wangs','dongs']
for new_user in new_users:
   if new_user.upper() in current_users:
       print('{new_user}用户名重复，请重新输入！')
   if new_user.lower() in current_users:
       print(f'{new_user}用户名重复，请重新输入！')
   else:
       print(f'{new_user}用户名可用！')

#练习 序数
num = [1,2,3,4,5,6,7,8,9]
for n in num:
    if n == 1:
        print(f'{n}st')
    elif n == 2:
        print(f'{n}nd')
    elif n == 3:
        print(f'{n}rd')
    else:
        print(f'{n}th')

'''


