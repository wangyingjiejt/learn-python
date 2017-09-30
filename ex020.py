# -*- coding:utf-8 –*-

def print_all(file):
    print file.read()


def print_restart(file):
    file.seek(0) # 重新设置文件读取指针到开头

def print_one_ine(count,file):
    print count,file.readline()

#继续使用ex015_sample.txt的文件
fo=open("ex015_sample.txt")

print "输出文件所有内容"
print_all(fo)

print "重新指向文件开头"
print_restart(fo)

current_line=1
print_one_ine(current_line,fo)

current_line+=1
print_one_ine(current_line,fo)

current_line+=1
print_one_ine(current_line,fo)