#-*- coding:utf-8 –*-

from sys import argv

# 需要在执行时传入username，script会自动获取脚本名称
script ,username=argv

note= "waiting for your inputting..."
print "hello %s :" % (username)
print "I'd like to ask you some questions"
print "How old are you ? %s" %(username)
age=int(raw_input(note))

print "%s,your age is %r " %(username,age)


