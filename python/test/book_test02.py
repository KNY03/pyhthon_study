scores = list(map(int, input().split()))
all_s = 0
TF = ""

for score in scores:
    if  0 > score or score > 100 :
        print("잘못된 점수")
        TF = "worng"
        break

    all_s += score

if TF != "worng":
    avg = all_s / len(scores)

    if avg >= 80 :
        print("합격")

    else:
        print("불합격")

a = list(range(5, -10, -2))
print(a)

b= tuple(range(-10, 9, 2))
print(b)

c = tuple(range(-10, 9, 3))
print(c)


# 11. 7
# 인덱스가 홀수인 요소 구하기
n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print(n[1::2])

#11.8
# list remove
a = (input().split())

a = (a[:len(a) - 5])

print(tuple(a))

# 1 2 3 4 5 6 7 8 9 10

# 11.9
x1 = input()
x2 = input()

print(x1[1::2],end="")
print(x2[::2])