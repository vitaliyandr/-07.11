a = int(input())
b = a%10
c = (a // 10) % 10
d = (a // 100) % 10
e = a // 1000
print(b*1000 + c*100 + d*10 + e)
