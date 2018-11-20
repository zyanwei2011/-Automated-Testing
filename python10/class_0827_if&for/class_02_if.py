__author__ = 'zz'
#条件语句 循环语句
#缩进  在Python里面 空格来控制 键盘上tab
#语法：if 条件表达式:
         #满足条件表达式执行的代码块  True

# score=-1
# if score>0:
#     print('哎哟不错哟')
# else:
#     print('小于10分了！继续努力了！')

# color = 'green'
# if color == 'red':
#     print('红灯停')
# elif color == 'green':
#     print('绿灯行')
# elif color == 'yellow':
#     print('黄灯请你等一等')
# else:
#     print('灯坏了！危险！！！')

#1：else 后面不能加条件表达式
#2：elif 后面必须加添加表达式
#3：一个完整的条件语句里面只能有一个if  一个else 但是可以有多个elif
#4：如果数据为空 或者为null  就代表False 不为空的  就为True
a={'age':18}
if a:
    print('我是if语句')
else:
    print('我是else语句')
