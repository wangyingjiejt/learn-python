# -*- coding:utf-8 –*-

def sum(a,b):
    return a+b


def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

# 一个函数可以返回多个参数
def multi_return(a,b):
    sum=a+b
    sub=a-b
    return sum,sub


print multiply(sum(20,5),sub(5,1))

sum,sub=multi_return(2,9)

print "sum=%r;sub=%r"% (sum,sub)