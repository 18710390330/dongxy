'''
第8章 函数
'''

'''
#def 实参和形参
def user(name):
    print(f'hello,{name}.')
user('dong')

#练习8-2 有参函数
def favorite_book(title):
    print(f'one of my favorite books is {title}.')
favorite_book('活着')


def pet(type,name='yoyo'):
    print(f'my pets name is {name},he is a {type}.')
pet('dog','dudu')
#位置参数
pet('cat','xiaoguai')
#关键字实参（可以颠倒形参顺序）
pet(name='niaoniao',type='cat')
#默认值(默认位置参数，默认参数如果不在最后一个，那么要给关键字实参）
pet('dog')
pet(type='dog')

#练习8-3 T恤
def make_shirt(size='大号',title='I Love Python'):
    print(f"size:{size},title:{title}")
make_shirt('xxl','天气糟糕')
make_shirt(size='xl',title='下雨')
#练习8-4 大号T恤
make_shirt()
make_shirt(size='中号')
make_shirt(title='I love Java')
#练习8-5 城市
def city(coutry,nation='china'):
    print(f'{coutry} in {nation}')
city('shanxi')
city(nation='U.K',coutry='london')
city(coutry='beijing')


#返回值
#让实参变成可选的（形参给空，再判断）
def formatted(first_name,last_name,meddle_name=''):
    if meddle_name:
        full_name = f'{first_name} {meddle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()
p = formatted('dong','yingying')
print(p)
p = formatted('dong','ying','xiao')
print(p)

#返回字典
def build_person(first_name,last_name):
    per = {'first':first_name,'last':last_name}
    return per
mm = build_person('dong','xiaodi')
for first,last in mm.items():
    print(first)
    print(last)

#结合使用函数及While循环
while True:
    print('请告诉我们您的信息。')
    print("按下'quit'退出.")
    fir_name = input('请输入你的姓：')
    if fir_name == 'quit':
        print('您已退出。')
        break
    print("按下'quit'退出.")
    last_name = input('请输入你的名：')
    if last_name == 'quit':
        break
    name = formatted(fir_name,last_name)
    print(f'Hello,{name}.')

#练习8-6 城市名
def city_coutry(city,nation):
    print(f'"{city},{nation}"')
city_coutry('西安','陕西')
city_coutry('太原','山西')
city_coutry('成都','四川')

#练习8-7 专辑
def make_alubm(people,zhuanji,totle = None):
    mess = {'people': people, 'zhuanji': zhuanji}
    if totle:
        mess['totle'] = totle
    return mess
music = make_alubm('张三','这天气专辑',10)
print(music)

#练习8-8 用户的专辑
while True:
    print('输入"q",退出系统。')
    me1 = input('请输入您的姓名：')
    if me1 == 'q':
        break
    me2 = input('请输入您的专辑名称：')
    if me2 == 'q':
        break
    print('暂不确定可输入"t"跳过该环节')
    me3 = input('请输入您的歌曲数量')
    if me3 == 'q':
        break
    elif me3 == 't':
        continue
    mm = make_alubm(me1,me2,me3)
    print(mm)


#向函数传递列表参数
def hello_name(names):
    for name in names:
        print(f'Hello,{name}.')
users = ['zhang','li','wang']
hello_name(users)

#在函数中修改列表
def pr(old):
    while old:
        new = old.pop()
        print(f'print module:{new}')
        new_line.append(new)
def zhanshi(new):
    for n in new:
        print(n)

old_line = ['one','two','three']
new_line = []

pr(old_line[:])#创建副本，使不影响原列表元素
zhanshi(new_line)
print(old_line)

#练习8-9 消息
message = ['today','tomorrow','yesterday']
send_messages = []
def show_message(mess):
    for m in mess:
        print(m)
show_message(message)
#练习8-10发送消息8-11
def send_message(mess1):
    while mess1:
        new = mess1.pop()
        print(f'now print mpdule:{new}')
        send_messages.append(new)
send_message(message[:])
print(message)
print(send_messages)

#传递任意数量的实参,*位置参数，**关键字参数
#定义函数时收集参数
def myprint(*param):
    print(param)
params = (1,2,3)
myprint(params)

def myprint1(**param):
    print(param)
myprint1(a=1,b=2)
#调用函数时分配参数
def myprint2(x,y):
    print(x)
    print(y)
params = (1,2)
myprint2(*params)

params = {'x':1,'y':2}
myprint2(**params)


#结合使用位置实参和任意数量实参
def make_pizza(size,*toppings):
    print(f'您点了{size}大小的pizza，和添加了：')
    for t in toppings:
        print(f'-{t}')
#默认第一个位置实参是形参size的值，其余为无限形参的值
make_pizza('xxl','洋葱','芝士','土豆')

#使用任意数量的关键字实参,关键字形参要在参数最后
def make_pizza1(size,another,**toppings):
    print(f'您点了{size}大小的pizza，和添加了：')
    print(toppings)
    print(another)
#调用时关键字实参可以不按顺序
make_pizza1(洋葱='芝士',土豆='豆土',size ='xxl',another='lolo')


#练习8-13三明治sandwish
def sandwish(*toppings):
    print('您要添加的配料为：（请确认）')
    for top in toppings:
        print(f'--{top}')
sandwish('洋葱','土豆')
#练习8-13用户简介
def build_my(first,last,**user_info):
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info
pri=build_my('dong','xiaoying',like='you')
print(pri)
#练习8-14汽车
def make_car(zhizao,xinghao,**dict):
    dict['zhizao'] = zhizao
    dict['xinghao'] = xinghao
    return dict
car = make_car('suzuki','outback',colour='purple',tow_package=True)
print(car)

#导入整个模块(使用模块名调用函数）
#使用as给模块别名
import pizza as p
p.make_pizza('xxl','洋葱','土豆')

#导入特定的函数（直接使用函数）
#使用as给函数别名
#导入模块中所有函数
from pizza import *
from pizza import make_pizza as mp,sandwish
mp('xxl','洋葱','土豆擦擦')
sandwish('洋葱','土豆')
'''












