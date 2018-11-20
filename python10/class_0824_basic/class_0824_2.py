# s_1='hello'
# s_2='python'

#字符串之间的拼接 +
# s_3=s_1+' '+s_2
# # print(s_3)
# # print(s_1,s_2)# 这个是输出2个变量
# # print('请输出s_1的值:',s_1)
# print(s_1+str(666)+s_2)
# print(type(int('66')))
#整数利用 str() 可以变成字符串
#字符串的值为数字的 可以了利用int()转成整数
# str(数据值或者是变量名)函数直接强制转换数据为字符串

#格式化输出 %
age=18
name='小尾巴'
score=99.789
# print("未来大佬"+name+"只有",age,"岁")
#%s 输出一个字符串 占坑  %d digital 整数类型的数字
# %f 浮点数默认精确到后6位
#按顺序赋值
# print("未来的大佬%s,只有%s岁,Python考试成绩是%d"%(name,age,score))

#第二种格式化输出 format 用{}来占坑
#如果不指定顺序 给空的{} 就按从左到右顺序赋值 有 几个{}
# 就给几个参数 否则 少了就报错
print("未来的大佬{2},只有{0}岁,Python考试成绩是{0}".format(name,age,score))
#format(name,age,score)) name 0  age-1 score-2