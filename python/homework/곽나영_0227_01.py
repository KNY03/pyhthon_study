"""임의의 큰수와 작은수를 입력받아 사이의 소수를 수해서 출력
한 줄에 소수 10개씩
마지막에는 소수의 갯수 출력"""

lst = []
count = 0

# 두번 임의의 숫자를 입력 받음
num1 = int(input())
num2 = int(input())

# 두 숫자중 큰 수 작은수 찾아 for문 돌리고 range(작은수, 큰수)
"""
for i in range(3, int(num ** 0.5) + 1, 2)
계산을 많이 줄일 수 있음
짝수를 처리하고 루트를 사용해서 더 줄일 수 있었음
bool값을 써서 체크 하는 경우도 있었음
"""
for i in range(min(num1, num2),max(num1, num2) + 1):
    # 소수 찾기
    for j in range(2, i): # for 문 돌리면서 2 ~ 자기 자신 -1
        if i % j == 0:
            break
    else: # for문이 break 없이 정상 종료되었을 때 실행됨
        if i > 1:
            lst.append(i)
            count += 1
            # 여기에 출력문을 써도 가능함
            """
            print("%2d"% i, end=" ")
            if count % 10 == 0:
                print()
            """

a = 0
## 나와서 소수 10개씩 출력하기
for i in lst: # 굳이 여기에 출력문을 안해도 가능함
    print("%2d"% i, end=" ")
    a += 1
    if a % 10 == 0:
        print()

# 소수 갯수 출력하기
print("\n총 소수의 갯수 = ",count)

"""
for i in range(min_num, max_num +1)
    if i < 2:
        continue
        
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print("%5d"% i, end=" ")
        count += 1
        if count % 10 == 0:
            print()
if count % 10 != 0: # 만약 10의 자리로 끝나면 두번 줄바꿈 되니까 
    print()
    
print(count)
"""