# -*- coding:utf-8 –*-

# 换工作之后每次公交由5元变为7元，写一个公交卡消费变化

# 每次消费5元总额
five_total=0
# 每次消费7元总额
seven_total=0

# 计算折扣
def discount(total,price):
    if total <100 :
        total+=price
    elif total>=100 and total<150:
        total+=price*0.8
    else:
        total+=price*0.5
    return total
print "换工作之后每次公交由5元变为7元，写一个公交卡消费变化^V^"

# 每天2次，每月按照2*23=46计算
for day in range(1,47):
    # 每次消费5元
    five_total= discount(five_total,5)
    # 每次消费7元
    seven_total= discount(seven_total,7)
    # 输出天数
    if day%2==0:
        print "第%r天,5元消费总额%r，7元消费总额%.1f，总共多花了%.1f" % (day/2,five_total,seven_total,seven_total-five_total)
