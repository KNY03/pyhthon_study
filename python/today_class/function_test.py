def add_sub(a, b):
    return a+b, a-b

# print(add_sub(10, 20)) # packing

x, y = add_sub(10, 20) # unpacking
print(x, y)

##################################################################

def mul(a, b): # a, b: 지역변수
    c =  a * b # c : 지역변수
    return c

def add(a, b):  # a, b: 지역변수
    c = a + b # c : 지역변수
    print(c)
    d = mul(a, b) # d : 지역변수
    print(d)
    # return 이 있는 것 과 마찬가지로 실행됨

x = 10 # 전역변수
y = 20 # 전역변수
add(x, y)

##################################################################

def circle_area(r): # r: 지역변수
    result = 3.14 * (r ** 2) # result : 지역변수
    return result

if __name__ == "__main__":
    radius = 3          # 전역변수
    area = circle_area(radius)  # 전역변수
    print("반지름은 %d, 면적은: %.2f" % (radius, area))
    # print(r) # r은 지역변수로써 위치를 벗어난 곳에서 사용했기 때문에 오류가 나온다.

##################################################################

pi = 3.1415

def circle_area_with_pi(r):
    # circle_area_with_pi의 local 영역
    pi = 3.14
    result = pi * (r ** 2)
    return result

def circle_area_without_pi(r):
    # circle_area_without_pi의 local 영역
    result = pi * (r ** 2)
    return result

def sum_areas():
    result = [circle_area_with_pi(3), circle_area_without_pi(3)]
    return sum(result)              # built-in의 sum함수를 호출

if __name__ == "__main__":
    print("PI: ", pi)
    print("반지름: ", 3, "면적: ", circle_area_with_pi(3))
    print("반지름: ", 3, "면적: ", circle_area_without_pi(3))
    print("sum_areas(): ", sum_areas())

##################################################################

pi = 3.14

def circle_area(r):
    # 전역변수를 참조한다는 선언문
    global pi # 특정 영역에서 전역변수를 사용하고 싶을 때 사용
    pi = pi + 0.0015
    result = pi * (r ** 2)
    return result

if __name__ == "__main__":
    print("PI: ", pi)
    print("반지름: ", 3, "면적: ", circle_area(3))
    print("PI: ", pi)
