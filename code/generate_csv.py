#!/usr/bin/env python3


import csv
import math

ls = []
for i in range(0,60):
    ls_t = []
    #  ls_t.append(8*math.pi/60*i)
    ls_t.append(i)
    ls_t.append(math.cos(8*math.pi/60*i)
            + math.cos(4*math.pi/60*i))
    ls.append(ls_t)

with open('cos_values.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in range(0, len(ls)):
        csvwriter.writerow(ls[i])

