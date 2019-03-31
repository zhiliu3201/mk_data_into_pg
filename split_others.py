# coding=utf8

f1 = open('customer.tbl', 'r') 
f2 = open('nation.tbl', 'r')
f3 = open('orders.tbl', 'r')
f4 = open('partsupp.tbl', 'r')
f5 = open('part.tbl', 'r')
f6 = open('region.tbl', 'r')
f7 = open('supplier.tbl', 'r')


f11 = open('customer1.tbl', 'w+')
f21 = open('nation1.tbl', 'w+')
f31 = open('orders1.tbl', 'w+')
f41 = open('partsupp1.tbl', 'w+')
f51 = open('part1.tbl', 'w+')
f61 = open('region1.tbl', 'w+')
f71 = open('supplier1.tbl', 'w+')


line = 'aa'
while line :
    line = f1.readline()
    f11.write(line[:-2]+'\n')


line = 'aa'
while line :
    line = f2.readline()
    f21.write(line[:-2]+'\n')
line = 'aa'
while line :
    line = f3.readline()
    f31.write(line[:-2]+'\n')
line = 'aa'
while line :
    line = f4.readline()
    f41.write(line[:-2]+'\n')
line = 'aa'
while line :
    line = f5.readline()
    f51.write(line[:-2]+'\n')
line = 'aa'
while line :
    line = f6.readline()
    f61.write(line[:-2]+'\n')
line = 'aa'
while line :
    line = f7.readline()
    f71.write(line[:-2]+'\n')
