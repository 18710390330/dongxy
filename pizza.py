def make_pizza(size,*topping):
    print(f'您要制作{size}大小的pizza and 以下配料：')
    for t in topping:
        print(f'--{t}')

def sandwish(*toppings):
    print('您要添加的配料为：（请确认）')
    for top in toppings:
        print(f'--{top}')

