'''
自动贩卖机：只接受1元、5元、10元的纸币或硬币，
# 单次投币可以1块，5元，10元。最多不超过10块钱。
# 饮料只有橙汁、椰汁、矿泉水、早餐奶，售价分别是3.5，4，2，4.5
# 写3个函数用来表示贩卖机的功能： 用户投钱和选择饮料，
# 并通过判断之后，给用户吐出饮料和找零。
'''
# 投币
goods_list = {'orange':3.5,'coconut':4,'water':2,'milk':4.5}
money_list = [1,5,10]

# money 为显示的余额，mon为新投入的币值
money = 0
def insert_coins(mon):
    global money
    if mon in money_list:
        if money+mon <= 10:
            money += mon
        else:
            money = money
            print('余额不应超过10元，投币失败')
    print(money)

def buy_goods(*args):
    global money
    for i in args:
        if i in goods_list.keys():
            if money > goods_list[i]:
                money -= goods_list[i]
            else:
                print('您的余额不足,请投币后继续购买')
                money = money

def refund_money():
    print('请取走你的余额{:.1f}元和商品'.format(money))

def main(mon,*args):
    insert_coins(mon)
    buy_goods(*args)
    refund_money()

if __name__ == '__main__':
    main(10,'orange','coconut','water','milk')



