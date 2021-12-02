'''
字典练习
'''
'''
dong = {'name':'T-dongxy','age':25,'gender':'woman'}
print(dong['name'])
#访问字典
alien_0 = {'color':'green','points':'5','speed':'medium'}
new_points = alien_0['points']
print(f'you just earned {new_points} points.')
#添加字典键值对
alien_0['x'] = 0
alien_0['y'] = 25
print(alien_0)
#创建空字典
alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
print(alien_1)
#修改键值对
alien_1['color'] = 'yellow'
alien_1['points'] = 15
alien_1['xx'] = 12
print(alien_1)
alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x1 = 1
elif alien_0['speed'] == 'medium':
    x1 = 2
else:
    x1 = 3
alien_0['x'] = x1 + alien_0['x']
print(f'new x = {alien_0["x"]}')
#删除键值对
del alien_1['xx']
print(alien_1)

#使用get()来访问值
points_value = alien_1.get('point','默认兜底输出')
speed_value = alien_1.get('speeds')
print(points_value)
print(speed_value)

#练习6-1人
friend_message = {'first_name':'杨','last_name':'星月','age':25,'city':'XiAn'}
print(friend_message['first_name'],friend_message['last_name'],
      friend_message['age'],friend_message['city'])

#6-3喜欢的数
friend_like_num = {'zhang':1,'li':2,'wang':3,'wu':4,'zhao':5}
print(friend_like_num)

new_friend = friend_like_num['bai'] = 6
print(f'另一个朋友bai-like_num:{new_friend}')
print(friend_like_num)

alter_frind = friend_like_num['wu'] = 14
print(f'实际上wu喜欢的数字是：{alter_frind}')
print(friend_like_num)

del friend_like_num['wang']
print('实际上wang不再是我的朋友了')
print(friend_like_num)

how_num = friend_like_num.get('cheng','not cheng friend')
print(f'my friend cheng like num is {how_num}')

print(f'li like num is {friend_like_num["li"]}')

#遍历字典
user_0 = {'zhang':'python','li':'java','dong':'python'}

for key,value in user_0.items():
    print(f'key:{key}')
    print(f'value:{value}')
#遍历键
#遍历的时候什么都不加，会默认遍历字典的所有键
for key in user_0.keys():
    print(f'key:{key}')
for key in user_0:
    print(key)
#遍历值（不排除重复）
for value in user_0.values():
    print(f'value:{value}')
#遍历值（去重）
for value in set(user_0.values()):
    print(value)

#列一个元组
friend = ['zhang','li']
#第一步：先遍历一下上面的字典的键，这时候变量name的值==字典的key
for name in user_0.keys():
    print(f'Hi {name} ')
#第二步：判断如果name变量的值存在于元组里，那么输出字典里对应的value
    if name in friend:
        message = user_0[name].title()
        print(f' {name},I know you like {message}.')
#判断是否存在于字典里
if 'delia' not in user_0.keys():
    print('delia not in dict')

#按特定顺序遍历字典键,作用是把字典的键进行了字母排序
for n in sorted(user_0.keys()):
    print(n)

#集合 没有冒号的就是集合，都是用花括号包含
jihe = {'name','age','gender'}

#练习6-4 词汇表
study = {'keys()':'键',
         'value()':'值',
         'set()':'去重',
         'get()':'默认值',
         'items()':'字典变元组'}

for key,value in study.items():
    print(f'\nKey:{key}')
    print(f'Value:{value}')
for key in study.keys():
    print(f'key:{key}')
for value in study.values():
    print(f'Value:{value}')
    if 'not' not in study.values():
        print('not in')

#练习6-5 河流
rivers = {'rever1':'china','rever2':'U.K','river3':'America'}
for river,coutry in rivers.items():
    print(f'The {river} runs {coutry}.')

for river in rivers.keys():
    print(river)
for coutry in rivers.values():
    print(coutry)
user_0 = {'zhang':'python','li':'java','dong':'python'}
#6-6调查
diaocha = ['zhang','li','dong','wang','dou']


#嵌套（列表中嵌套字典）
robot_1 = {'color':'green','points':5}
robot_2 = {'color':'yellow','points':10}
robot_3 = {'color':'red','points':15}

robot_z = [robot_1,robot_2,robot_3]
print(robot_z)

robots = []
for r in range(30):
    new_robot = {'color':'green','points':5,'speed':'slow'}
    robots.append(new_robot)
for r in robots[:5]:
    print(r)
print(f'共新增：{len(robots)}个机器人。')

#修改前3个机器人
for r in robots[:3]:
    if r['points'] == 6:
        r['color'] = 'yellow'
        r['points'] = 10
        r['speed'] = 'medium'
    elif r['color'] == 'green':
        r['color'] = 'red'
        r['points'] = 15
        r['speed'] = 'fast'
for r in robots[:5]:
    print(r)

#嵌套（字典中嵌套列表）
pizza = {'crust':['thick'],
         'toppings':['cheese','mango','meat'],
         'language':['chinese','japanese'],}
print(pizza['crust'])
for p in pizza['toppings']:
    print(p)

favorite_language = {'zhang':['c++','java'],
                     'li':['python','rn'],
                     'wu':['c']}
for name,value in favorite_language.items():
    if len(value) == 1:
        for v in value:
            print(f'姓名：{name},喜欢的语言shi：{v}')
    else:
        print(f'姓名：{name},喜欢的语言：')
        for v in value:
            print(v)

# 嵌套（字典中嵌套字典）
users = {'zhanglele':{'first':'zhang',
                      'last':'lele',
                      'age':18},
         'lidoudou':{'first':'li',
                     'last':'doudou',
                     'age':19},
         'zhaohongjuan':{'first':'zhao',
                         'last':'hongjuan',
                         
#字典练习


dong = {'name':'T-dongxy','age':25,'gender':'woman'}
print(dong['name'])
#访问字典
alien_0 = {'color':'green','points':'5','speed':'medium'}
new_points = alien_0['points']
print(f'you just earned {new_points} points.')
#添加字典键值对
alien_0['x'] = 0
alien_0['y'] = 25
print(alien_0)
#创建空字典
alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
print(alien_1)
#修改键值对
alien_1['color'] = 'yellow'
alien_1['points'] = 15
alien_1['xx'] = 12
print(alien_1)
alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x1 = 1
elif alien_0['speed'] == 'medium':
    x1 = 2
else:
    x1 = 3
alien_0['x'] = x1 + alien_0['x']
print(f'new x = {alien_0["x"]}')
#删除键值对
del alien_1['xx']
print(alien_1)

#使用get()来访问值
points_value = alien_1.get('point','默认兜底输出')
speed_value = alien_1.get('speeds')
print(points_value)
print(speed_value)

#练习6-1人
friend_message = {'first_name':'杨','last_name':'星月','age':25,'city':'XiAn'}
print(friend_message['first_name'],friend_message['last_name'],
      friend_message['age'],friend_message['city'])

#6-3喜欢的数
friend_like_num = {'zhang':1,'li':2,'wang':3,'wu':4,'zhao':5}
print(friend_like_num)

new_friend = friend_like_num['bai'] = 6
print(f'另一个朋友bai-like_num:{new_friend}')
print(friend_like_num)

alter_frind = friend_like_num['wu'] = 14
print(f'实际上wu喜欢的数字是：{alter_frind}')
print(friend_like_num)

del friend_like_num['wang']
print('实际上wang不再是我的朋友了')
print(friend_like_num)

how_num = friend_like_num.get('cheng','not cheng friend')
print(f'my friend cheng like num is {how_num}')

print(f'li like num is {friend_like_num["li"]}')

#遍历字典
user_0 = {'zhang':'python','li':'java','dong':'python'}

for key,value in user_0.items():
    print(f'key:{key}')
    print(f'value:{value}')
#遍历键
#遍历的时候什么都不加，会默认遍历字典的所有键
for key in user_0.keys():
    print(f'key:{key}')
for key in user_0:
    print(key)
#遍历值（不排除重复）
for value in user_0.values():
    print(f'value:{value}')
#遍历值（去重）
for value in set(user_0.values()):
    print(value)

#列一个元组
friend = ['zhang','li']
#第一步：先遍历一下上面的字典的键，这时候变量name的值==字典的key
for name in user_0.keys():
    print(f'Hi {name} ')
#第二步：判断如果name变量的值存在于元组里，那么输出字典里对应的value
    if name in friend:
        message = user_0[name].title()
        print(f' {name},I know you like {message}.')
#判断是否存在于字典里
if 'delia' not in user_0.keys():
    print('delia not in dict')

#按特定顺序遍历字典键,作用是把字典的键进行了字母排序
for n in sorted(user_0.keys()):
    print(n)

#集合 没有冒号的就是集合，都是用花括号包含
jihe = {'name','age','gender'}

#练习6-4 词汇表
study = {'keys()':'键',
         'value()':'值',
         'set()':'去重',
         'get()':'默认值',
         'items()':'字典变元组'}

for key,value in study.items():
    print(f'\nKey:{key}')
    print(f'Value:{value}')
for key in study.keys():
    print(f'key:{key}')
for value in study.values():
    print(f'Value:{value}')
    if 'not' not in study.values():
        print('not in')

#练习6-5 河流
rivers = {'rever1':'china','rever2':'U.K','river3':'America'}
for river,coutry in rivers.items():
    print(f'The {river} runs {coutry}.')

for river in rivers.keys():
    print(river)
for coutry in rivers.values():
    print(coutry)
user_0 = {'zhang':'python','li':'java','dong':'python'}
#6-6调查
diaocha = ['zhang','li','dong','wang','dou']


#嵌套（列表中嵌套字典）
robot_1 = {'color':'green','points':5}
robot_2 = {'color':'yellow','points':10}
robot_3 = {'color':'red','points':15}

robot_z = [robot_1,robot_2,robot_3]
print(robot_z)

robots = []
for r in range(30):
    new_robot = {'color':'green','points':5,'speed':'slow'}
    robots.append(new_robot)
for r in robots[:5]:
    print(r)
print(f'共新增：{len(robots)}个机器人。')

#修改前3个机器人
for r in robots[:3]:
    if r['points'] == 6:
        r['color'] = 'yellow'
        r['points'] = 10
        r['speed'] = 'medium'
    elif r['color'] == 'green':
        r['color'] = 'red'
        r['points'] = 15
        r['speed'] = 'fast'
for r in robots[:5]:
    print(r)

#嵌套（字典中嵌套列表）
pizza = {'crust':['thick'],
         'toppings':['cheese','mango','meat'],
         'language':['chinese','japanese'],}
print(pizza['crust'])
for p in pizza['toppings']:
    print(p)

favorite_language = {'zhang':['c++','java'],
                     'li':['python','rn'],
                     'wu':['c']}
for name,value in favorite_language.items():
    if len(value) == 1:
        for v in value:
            print(f'姓名：{name},喜欢的语言shi：{v}')
    else:
        print(f'姓名：{name},喜欢的语言：')
        for v in value:
            print(v)

# 嵌套（字典中嵌套字典）
users = {'zhanglele':{'first':'zhang',
                      'last':'lele',
                      'age':18},
         'lidoudou':{'first':'li',
                     'last':'doudou',
                     'age':19},
         'zhaohongjuan':{'first':'zhao',
                         'last':'hongjuan',
                         'age':29},
}

for names,message in users.items():
    wan_name  = f"{message['first']}{message['last']}"#f语句可不放在输出，可直接赋值给变量
    message = message['age']
    print(f'\n姓名：{names}\n信息:{wan_name},年龄{message}')
#names:对应大字典中的键
#message:对应大字典中的值（该值是嵌套在大字典中的字典），访问时需要遍历message小字典里的键（索引）


#练习6-7 人们
people = {
    'user1':{'name':'张三',
             'age':18},
    'user2':{'name':'里斯',
             'age':19},
    'user3':{'name':'王武',
             'age':20},
}
for seq,message in people.items():
    message_name = message['name']
    message_age = message['age']
    print(f'序号：{seq},name:{message_name},age:{message_age}')

#练习6-8 宠物
pet1 = {'name':'doudou','owner':'mark'}
pet2 = {'name':'fugui','owner':'jack'}
pet3 = {'name':'dudu','owner':'rose'}
#列表中嵌套字典，无需引号，会变成str
pets_message = [pet1,pet2,pet3,]
for pet in pets_message:
    print(pet)

#喜欢的地方
favorite_places = {
    'jack':['xian','sichuan','xizang'],
    'rose':['beijing'],
    'mark':['shanghai','qinghai'],
}
for name,coutrys in favorite_places.items():
    if len(coutrys) == 1 :
        for c in coutrys:
            print(f'{name} like is:\n{c}')
    else:
        print(f'name:{name},like coutry:')
        for coutry in coutrys:
            print(coutry)

#练习6-11 城市
cities = {
    'shanxi':{'shenghui':'xian',
              'people':1000000,
              'mess':'古都'},
    'sichuan':{'shenghui':'chengdu',
               'people':2000000,
               'mess':'辣子'},
    'xinjiang':{'shenghui':'wulumuqi',
                'people':3000000,
                'mess':'葡萄干'},
}
for name,message in cities.items():
    message_shenghui = message['shenghui']
    message_people = message['people']
    message_mess = message['mess']
    print(f'城市：{name},'
          f'省会：{message_shenghui},'
          f'人口：{message_people},'
          f'特色：{message_mess}')

'''


