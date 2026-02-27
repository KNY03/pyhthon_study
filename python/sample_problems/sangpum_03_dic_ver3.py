# sangpum_file_write_01.py
# 데이터를 file로 저장

# -*- coding: utf-8 -*-

fp = open("sangpum_data.txt", "w", encoding="utf-8") # csv형식으로 저장
# w, r, a 모드가 존재함

lst = []
all_sell = 0

while True:
    dct = {}

    dct["code"] = (input("제품코드 입력: "))

    if dct["code"].lower() == "exit":
        break

    dct["name"] = input("제품명 입력: ")
    dct["num"] = int(input("수량 입력: "))
    dct["price"] = int(input("단가 입력: "))

    dct["sell"] = dct["num"] * dct["price"]
    lst.append(dct)

    fp.write(dct["code"]+ "," + dct["name"]+ "," + str(dct["num"])+ "," + str(dct["price"])+ "," + str(dct["sell"]) + "\n")
    print()

fp.close()
