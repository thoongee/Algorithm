import sys
input = sys.stdin.readline

# 3kg, 5kg 봉지 있음 -> 5는 3의 배수가 아닌데, 그럼 DP로 해야하는건가?


n = int(input())
cnt = 0

while n>=0:
    if n%5 == 0:
        cnt += n//5
        n = 0
        break
        
    n -= 3
    cnt += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1 (5의 배수가 될때까지 3을 빼준다는 것이 이 문제의 아이디어)
    
if n==0:
    print(cnt)
else:
    print(-1)
'''
bag = 0
check = True
while(check):
    # 
    if n//5 >=1 :
        n = n//5
        bag += 1
    elif n//3 >=1 :
        n = n//3
        bag += 1
    else:
        bag = -1
        check= False

print(bag)
'''
