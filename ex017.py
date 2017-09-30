# -*- coding:utf-8 –*-

from sys import argv
from os.path import exists
# 继续使用ex015_sample.txt进行测试
script,from_file,to_file=argv
print "将文件%r复制到%r" %(from_file,to_file)

in_file=open(from_file)
indata=in_file.read()

print "源文件的长度是%r字节" %len(indata)
print "输出文件是否存在？%r" % exists(to_file)
out_file=open(to_file,"w")
out_file.write(indata)

out_file.close()
in_file.close()
