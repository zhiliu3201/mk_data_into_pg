# coding=utf8

import ctypes

hashLib = ctypes.CDLL('./hash_part.so')
parts = 12

f1 = open('lineitem_1.tbl', 'w+') 
f2 = open('lineitem_2.tbl', 'w+')
f3 = open('lineitem_3.tbl', 'w+')
f4 = open('lineitem_4.tbl', 'w+')

part1 = {3, 7, 11}
part2 = {0, 4, 8}
part3 = {1, 5, 9}
part4 = {2, 6, 10}

line = 'aa'
with open('./lineitem.tbl', 'r') as f:
    while line :
        line = f.readline()
        lid = line.split('|')[0]
        if lid == '':
            print(line)
            continue
        part_idx = hashLib.get_hash_part_idx(int(lid), parts)
        if part_idx in part1:
            f1.write(line[:-2]+'\n')
        elif part_idx in part2:
            f2.write(line[:-2]+'\n')
        elif part_idx in part3:
            f3.write(line[:-2]+'\n')
        elif part_idx in part4:
            f4.write(line[:-2]+'\n')
        else:
            print(part_idx, lid)
