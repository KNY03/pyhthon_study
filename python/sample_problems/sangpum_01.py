# 2026.02.25

code = (input("제품코드 입력: "))
name = input("제품명 입력: ")
num = int(input("수량 입력: "))
price = int(input("단가 입력: "))

sell = num * price

print("\n  제품코드 \t 제품명 \t 수량 \t 단가 \t 판매금액 ")
print("================================================")
print("  %4s \t %8s \t %3d \t %3d \t %6d" %(code, name, num, price, sell))
print("================================================")
