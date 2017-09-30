# -*- coding:utf-8 –*-

from sys import argv
# 继续使用ex015_sample.txt进行测试
script,filename=argv

print "现在正要清除%r的内容" % filename
print "如果不想清除请按Ctrl+c退出否则按任意键继续..."
raw_input("否则按任意键继续...")
print "打开文件..."
target=open(filename,"w")
print "正在清除..."
target.truncate()

print "清除完毕"

print "请输入一句话到该空文档"
line1=raw_input("line1:")
target.write(line1)
print "添加完成！"

