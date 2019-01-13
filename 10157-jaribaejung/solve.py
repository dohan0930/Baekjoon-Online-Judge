#https://www.acmicpc.net/problem/10157
C, R = input().split()
C = int(C)
R = int(R)
index = int(input())

if index > C*R :
	print("0")
else :
	circle_num = 1
	circle_length = C+R-4
	while index > circle_length :
		index = index - circle_length
		circle_num = circle_num + 1
		circle_length = circle_length - 8
	

	

