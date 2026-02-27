# sangpum_file_read_01.py
# file로 불러오기

# -*- coding: utf-8 -*-
import os

if os.path.exists('sangpum_data.txt'): # 읽기 모드에서는 파일의 유무가 중요하다
    fp = open("sangpum_data.txt", "r", encoding="utf-8")

    lst = []
    for line in fp:
        dct = {}
        res = line.strip("\n").split(",") # 맨 마지막 단어에 \n이 들어가서 제거하기 위해서
        dct["code"] = res[0]
        dct["name"] = res[1]
        dct["num"] = res[2]
        dct["price"] = res[3]
        dct["sell"] = res[4]
        lst.append(dct)
        print()

    fp.close()

    print("\n=============== 📦 상품 판매 현황 ====================")
    print("\n  제품코드 \t 제품명 \t 수량 \t 단가 \t 판매금액 ")
    print("====================================================")
    print("====================================================")
    for dct in lst:
        print(
            "  %4s \t %8s \t %3d \t %3d \t %6d" %
            (dct["code"], dct["name"], int(dct["num"]), int(dct["price"]), int(dct["sell"])))

    print("====================================================")
    print("                   < 총 판매 금액 >")
    all_sell = 0
    for dct in lst:
        all_sell += dct["sell"]
    print("총 판매 금액은: %30d" % all_sell)
    print("====================================================")
    print("====================================================")
    print("                   ✔ 출력 완료 ✔")
    print("====================================================")

else:
    print("해당 파일이 없습니다!!")