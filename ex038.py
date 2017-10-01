# -*- coding:utf-8 –*-

ten_things="Apple Orange Crows Telephone Light Sugar"

print "这里的清单不够十个单词，我们一起来修复它"

stuff=ten_things.split(" ")
more_stuff=["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff)!=10:
    add_one=more_stuff.pop()
    print "Add one stuff:",add_one
    stuff.append(add_one)
    print "现在清单里有%d件东西" % len(stuff)

print stuff

