# -*- coding:utf-8 –*-

# 需要在执行时传入username，script会自动获取脚本名称
# script ,filename=argv
filename = raw_input("input filename")
if filename != "ex015_sample.txt":
    print "您输入的文件不存在"
else:
    txt = open(filename)
    print txt.read()
