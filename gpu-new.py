#!/usr/bin/python
import sys
import re

in_init=0
in_last=0
gpusn_init_arr = []
gpusn_last_arr = []

with open("GPU_list.dec7.txt") as my_file:
    for line in my_file:
       gpusn_init_arr.append(line.rstrip())

with open("GPU_list.Mar05_2018.txt") as my_file:
    for line in my_file:
       gpusn_last_arr.append(line.rstrip())

if str(sys.argv[1]) in gpusn_init_arr :
    in_init = 1


if (gpusn_last_arr.count(sys.argv[1]) >= 1 ):
    in_last = 1

if re.search('^032[\d][\d]1[5678].*', sys.argv[1]) :
    print "New"

elif in_init == 1 and in_last == 1:
    print "Old"

elif in_init == 1 and in_last == 0:
    print "Grade 1"
