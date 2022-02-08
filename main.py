# 문자열(숫자포함) 입력받으면, 알파벳은 순서정렬, 숫자는 다 더해서 마지막에 출력
# 마지막 부분을 간략하게 표현할 수 있을듯

num = 0
def func(i):
	global num
	ascii = ord(i)
	if ascii >= ord('0') and ascii <= ord('9'):
		num += int(i)
		
	else:
		return i

a = [i for i in list(map(func,sorted(input()))) if i]
s = ''
for i in a:
	s+=i
s += str(num)

print(s)