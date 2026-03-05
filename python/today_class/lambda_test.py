# 기본적인 람다 사용

def add_num(x):
    return x + 10

print(list(map(add_num, ([1, 2, 3]))))


## 위에 함수와 수식을 lambda를 이용하면 더 짧게 작성이 가능하다.
a = list(map(lambda x: x + 10 , [1, 2, 3]))
print(a)

#########################################################

circle_area = lambda radius, pi: pi * (radius ** 2)
print(circle_area(3, 3.14))
# 저장을 했기 때문에 여러번 사용이 가능

print((lambda radius, pi: pi * (radius ** 2))(3, 3.14))
# lambda radius, pi: pi * (radius ** 2) 일회성으로 사용될 수 밖에 없음

#############################################################
def circle_area(radius, print_format):
    area = 3.14 * (radius ** 2)
    print_format(area)

if __name__ == '__main__':
    circle_area(3, (lambda x: print("결과값: ", round(x, 1)))) # round는 소숫첨 뒤에 값 까지 출력하고 반올림 해라 라는 뜻
    circle_area(3, (lambda x: print("결과값: ", round(x, 2))))

