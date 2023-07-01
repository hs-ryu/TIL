# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# falied -> 이유 모르겠음.

import sys


def input_data():
	readl = sys.stdin.readline
	N = int(readl())
	map_pic = [list(map(int, readl().strip())) for _ in range(N)]
	return N, map_pic


sol = 0
# 입력받는 부분
N, map_pic = input_data()
# print(map_pic)
# 여기서부터 작성
for num in range(1,10):
	cnt = 0
	t,b,l,r = 11,-1,11,-1
	for i in range(N):
		for j in range(N):
			if map_pic[i][j] == num:
				cnt += 1
				if t > i:
					t = i
				if b < i:
					b = i
				if l > j:
					l = j
				if r < j:
					r = j
	
	if t == 11 or b == -1 or l == 11 or r == -1:
		continue
	check = True
	for i in range(t,b+1):
		for j in range(l,r+1):
			if map_pic[i][j] != num:
				check = False
				break
		if check == False:
			break
	if check == True:
		sol += 1
	
# 출력하는 부분
print(sol)
