# 숫자 입력, 큰수 작은수 , 출력
# homework 0225 과제를 함수를 사용해서 고침
def input_num():
    num1 = int(input("첫번째 숫자를 입력하시오 => "))
    num2 = int(input("두번째 숫자를 입력하시오 => "))
    return num1, num2

def min_max_num(num1, num2):
    return min(num1, num2), max(num1, num2)

def print_dan(num1, num2):
    for i in range(num1, num2 + 1):
        print(" ** %d단 ** " % i, end="\t\t")
    print("")
    for j in range(1, 10):
        for i in range(num1, num2 + 1):
            result = i * j
            print("%d * %d = %2d" % (i, j, result), end="\t\t")
        print("")

if __name__ == "__main__":
    num1, num2 = input_num()
    min_num, max_num = min_max_num(num1, num2)
    print_dan(min_num, max_num)
