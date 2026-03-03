import csv

fieldnames = ["id", "name", "price", "amount"]
data = [
    {"id": "1", "name": "apple", "price": "100", "amount": "5"},
    {"id": "2", "name": "pencil", "price": "500", "amount": "42"},
    {"id": "3", "name": "pineapple", "price": "8000", "amount": "5"},
    {"id": "4", "name": "pen", "price": "1500", "amount": "10"}
]

f = open("data2.csv", "w")
writer = csv.DictWriter(f, fieldnames=fieldnames) # key를 fieldname으로 설정


writer.writeheader() # 이 코드를 쓰면 첫 줄에 fieldname 출력
# writer.writerows(data)

for row in data:
   writer.writerow(row)

f.close()

import csv

f = open("data2.csv", "r")
reader = csv.DictReader(f)

print(list(reader)) # 한번에 출력

for row in reader: # 한줄씩 출력
    print(row)

f.close()