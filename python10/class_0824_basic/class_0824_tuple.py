__author__ = 'zz'
#元组 关键字 tuple 标志()
#t=()#空元组？
#1：标志是() 关键字 tuple
#2:元组里面可以放任何类型的数据 元素与元素之间用逗号隔开
#3：元组里面的元素 也都有索引 是从0开始  跟字符串的索引方式是一致的
#4：元组取值方式：元组名[索引值]  正序 反序
#5：切片：元组名[m:n:k] 跟字符串是一样操作
# t_1=(1,2.0,[1,2,3],(4,5,6))

#最最最严重的区别：元组的值不能进行任何的增删改
a=([1,2,3],)#只有单个元素的时候  请加，来成为元组
#type  去帮你判断数据的类型