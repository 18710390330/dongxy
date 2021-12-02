#20211104_dongxy
#列表

names = ['张三四','李五六','王七八','alice']
print(names)
print(names[0])
print(names[-1])
print(names[1][2])
print(names[3].title())

message = f"今天{names[3].upper()}穿的漂亮极了!"
print(message)


#练习3-1
names1 = ['德宝','相印','洁柔']
print(names1[0])
print(names1[1])
print(names1[-1])

#练习3-2
message1 = "早上好呀~"
print(f"{message1}{names1[-3]}")
print(f"{message1}{names1[-2]}")
print(f"{message1}{names1[-1]}")


#练习3-3
names2 = ['摩托车','bike','小汽车'] 
print(f"我喜欢在周一骑上我的{names2[0]}")
print(f"我不喜欢骑{names2[1]}")
print(f"想开但是还没有{names2[2]}")



update = ['hondaa','yamaha','suzuki']
#修改元素,当作变量重新赋值
update[0] = "honda"
print(update[0])
print(update)

#在列表末尾添加元素append()
update.append('bmw')
print(update)
#在空列表中添加元素
update1 = []
update1.append('air')#一次只能添加一个元素
update1.append('supermarket')
print(update1)
#在列表中插入元素insert(0,'abc')
update1.insert(0,'fax')
print(update1)

#使用del语句删除元素
del update1[0]
print(update1)
#使用pop方法删除元素(不加索引)
new_update1 = update1.pop()#删除列表末尾的值，后将被删除的元素赋值给新的变量；指出最后一个元素，用来查找也是可以的
print(update1)
print(new_update1)#为字符串，非列表元素
print(f"我新买的{new_update1}")

#使用pop方法删除元素(加索引)
new_update2 = update1.pop(0)
print(f"我新买的{new_update2}")

print("\n")
update1.append('ill')
update1.append('behind')
update1.append('again')
update1.append('again')
print(update1)
#根据元素值删除remove(),只会删除符合条件的第1个值，删除全部需要循环，第7章见
update1.remove("again")
print(update1)

new = "again"#元素声明，值是列表里的某元素；
update1.remove(new)#删除元素=该变量值,不影响变量
print(update1)
print(new)#变量正常输出
print(f"hihi,{new.title()} is very good!")

#练习3-4 嘉宾名单
dinner = ['赵找','王号','孙天','里美']
message3 = "Dear"
message2  = '邀请今天晚上来我家吃晚餐，不见不散～'
print(f"{message3}{dinner[0]},{message2}")
print(f"{message3}{dinner[1]},{message2}")
print(f"{message3}{dinner[2]},{message2}")
print(f"{message3}{dinner[3]},{message2}")

#练习3-5 修改嘉宾名单
print(f"无法参加聚会：{dinner[1]}")
dinner[1] = "六六"
print(f"{message3}{dinner[0]},{message2}")
print(f"{message3}{dinner[1]},{message2}")
print(f"{message3}{dinner[2]},{message2}")
print(f"{message3}{dinner[3]},{message2}")

#练习3-6添加嘉宾
dinner.insert(0,"五五")
dinner.insert(3,"七七")
dinner.append("默默")
print(f"{message3}{dinner[0]},{dinner[1]},{dinner[2]},{dinner[3]},{dinner[4]},{dinner[5]},{dinner[6]},{message2}")

#练习3-7缩减嘉宾
print(f"{message3}{dinner[0]},{dinner[1]},{dinner[2]},{dinner[3]},{dinner[4]},{dinner[5]},{dinner[6]},sorry,非常抱歉，由于餐桌原因，聚会可能会有变化。")
message4 = "sorry,今天的约会取消。"
del1 = dinner.pop()
print(f"{del1},{message4}")
del2 = dinner.pop()
print(f"{del2},{message4}")
del3 = dinner.pop()
print(f"{del3},{message4}")
del4 = dinner.pop()
print(f"{del4},{message4}")
del5 = dinner.pop()
print(f"{del5},{message4}")
print(f"还有{dinner}")
message5 = "计划不变，待会见。"
print(f"{dinner[0]},{message5}")


del dinner[0]
print(f"待处理邀请：{dinner}")
print(f"{dinner[0]},{message5}")
del dinner[0]
print(f"待处理邀请：{dinner}")

#组织列表(小写)
car = ['bmw','audi','toyota']

#按照字母永久正序排序
car.sort()
car.sort(reverse=False)
print(car)
#按照字母永久倒叙排序
car.sort(reverse = True)
print(car)
#永久倒序展示
car.reverse()
print(car)

#对列表按照字母顺序临时排序
print("这个是临时按字母正序排序：")
print(sorted(car))
print(sorted(car,reverse=False))

print("\n这是原本列表顺序：")
print(car)
#临时按照字母倒叙排序
print("\n这是临时按照字母倒叙排序：")
print(sorted(car,reverse=True))

#列表元素长度
print("\n列表元素长度：")
print(len(car))
#列表之和,只针对int列表
print("\n列表元素之和：")
num = [1,2,3]
print(sum(num))


#练习3-8放眼世界
coutry = ['korea','china','canada','pakistan','paris']
print(f"原始列表：{coutry}")
print(f"临时按字母正序排序：{sorted(coutry)}")
#排序优先大写，后小写
print(f"确认列表未被改变：{coutry}")
print(f"临时按字母倒序排序：{sorted(coutry,reverse=True)}")
print(f"确认列表未被改变：{coutry}")
#print(f"永久反向排序:{coutry.reverse()}")#也不知道为啥不行
coutry.reverse()
print(f"永久反向排序:{coutry}")
coutry.reverse()
print(f"确认恢复原始顺序：{coutry}")
coutry.sort()
print(f"永久按字母正序排序：{coutry}")
#发现函数在f字符串变量中不好使
coutry.sort(reverse=True)
print(f"永久按字母倒序排序：{coutry}")

#练习3-9晚餐嘉宾
print(f"今天实际邀请了{len(dinner)}位朋友来参加聚会")


#练习3-10各种函数

seq = [' banana ','apple','straberry']
seq1 = ['banana','apple','straberry']

print(f"首字母大写：{seq[0].title()}")
print(f"字母全大写：{seq[1].upper()}")
print(f"字母全小写：{seq[-1].lower()}")
print(f"剔除末尾空格:{seq[0].rstrip()}")
print(f"剔除开头空格:{seq[0].lstrip()}")
print(f"剔除首尾空格:{seq[0].strip()}")

seq[1] = "apples"
print(seq)
seq.append('pineapple')
print(seq)
seq.insert(4,'mango')
print(seq)
del seq[4]
print(seq)
dd = seq.pop()
print(seq)
print(dd)
dd1 = seq.pop(-1)
print(seq)
dd2 = seq.remove("apples")
print(seq)
seq.append('apples')
seq.append('manggo')
print(seq)

seq1.sort()
print(seq1)
seq1.sort(reverse=True)
print(seq1)

seq1.reverse()
print(seq1)
print(len(seq1))
print(sorted(seq1))
print(sorted(seq1,reverse = True))
seq1.reverse()
print(seq1)





























