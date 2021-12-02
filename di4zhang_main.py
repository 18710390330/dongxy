
names = ['alice','david','carolina']
for name in names:
    print(f"Hello,{name.title()}同学")
    print(f"bye～{name.upper()}同学")
print("让我们明天见～")


#练习4-1 比萨
pizzas = ['fruit','cheese','sausage']
for pizza in pizzas:
    print(f"I like {pizza}pizza.")
print("I really love pizza.")

#练习4-2 动物
animals = ['cat','dog','bird']
for animal in animals:
    print(f"A {animal} would make a great pet!")
print("Any of these animals would make a great pet.")

#range()创建数据
for value in range(1,4):
    print(value)
#创建数据并以列表形式输出
num1 = list(range(1,10,2))
print(num1)

#对创建的数据加工后添加进列表
squares = []
for value1 in range(1,11):
    squares.append(value1 ** 2)
print(squares)

num2 = [1,2,3,4,5,6,7,8,9,0]
print(min(num2))#最小值
print(max(num2))#最大值
print(sum(num2))#和

#直接列表里创建数据
squares1 = [value2**2 for value2 in range(1,11)]
print(squares1)


#切片
python1 =['fiddler','internet','zhang','dou','li']
print(python1[0:3])
print(python1[:3])
print(python1[1:])
print(python1[-2:])

#遍历切片
for py in python1[0:3]:
    print(py.title())
#复制列表
python2 = python1[:]
print(python2)

#练习4-10 切片
items = ['dong','li','zhang','zhao','sun','bai','he']
print("The first items in the list are:")
print(items[0:3])
print("Three items from the middle of the list are:")
print(items[2:5])
print("The last three items in the last are:")
print(items[-3:])

#练习4-11你的比萨，我的比萨
pizzas = ['fruit','cheese','mango','tufo']
friend_pizzas = pizzas[:]
pizzas.append('yoyo')
friend_pizzas.append('hehe')
print('My favorite pizzas are:')
for my in pizzas[:]:
    print(my)
print('My friend favorite pizzas are:')
for her in friend_pizzas[:]:
    print(her)

#元组
yuan = (100,110)
print(yuan[0])
yuan1 = (111,)
print(yuan1[0])
#遍历元组
for y in yuan :
    print(y)
#修改元组变量（不可以直接修改某个元素的值，但支持重新定义元组）
yuan = (200,210)
print(yuan)

#练习4-13 自助餐
foods = ('油麦菜','豆腐','宽粉','香豆腐','撒尿牛丸')
print('菜品介绍：')
for food in foods:
    print(food)

foods = ('油麦菜','豆腐','宽粉','豆腐皮','方便面')
print("\n菜品调整：")
for food in foods:
    print(food)










