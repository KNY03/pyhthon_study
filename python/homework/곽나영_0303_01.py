"""임의의 큰수와 작은수를 입력받아 사이의 소수를 수해서 출력
한 줄에 소수 10개씩
마지막에는 소수의 갯수 출력
모든 작업의 내용을 4개의 함수로 만든다.
    1. 임의의 두수를 입력 받는 부분을 함수로 만든다.
    2. 작은수와 큰수를 구하는 과정을 함수로 만든다.
    3. 소수를 구해서 출력하는 과정을 함수로 만든다.
    4. 총소수의 개수를 출력하는 부분을 함수로 만든다.
"""
lst = []
count = 0

# 1. 임의의 두수를 입력 받는 부분을 함수로 만든다.
def input_num():
    # 두번 임의의 숫자를 입력 받음
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    return num1, num2

# 2. 작은수와 큰수를 구하는 과정을 함수로 만든다.
def min_max_num(num1, num2):
    return min(num1, num2), max(num1, num2)

# 3. 소수를 구해서 출력하는 과정을 함수로 만든다.
def cal_prim(num1, num2):
    global count
    # 두 숫자중 큰 수 작은수 찾아 for문 돌리고 range(작은수, 큰수)
    for i in range(num1, num2 + 1):
        # 소수 찾기
        for j in range(2, i):  # for 문 돌리면서 2 ~ 자기 자신 -1
            if i % j == 0:
                break
        else:  # for문이 break 없이 정상 종료되었을 때 실행됨
            if i > 1:
                lst.append(i)
                count += 1
                # 여기에 출력문을 써도 가능함
                print("%2d"% i, end=" ")
                if count % 10 == 0:
                    print()

# 4. 총소수의 개수를 출력하는 부분을 함수로 만든다.
# 소수 갯수 출력하기
def count_prim():
    print("\n총 소수의 갯수 = ", count)

if __name__ == "__main__":
    num1, num2 = input_num()
    min_num, max_num = min_max_num(num1, num2)
    cal_prim(min_num, max_num)
    count_prim()