file = open("test.txt", "w") # 만든 파일이 없으면 현재 위치에 파일을 생성 ## w 또는 wt 사용가능
s = file.write("hello world!!")
file.close()        # 파일 객체 담기

# read(): 모든 글을 다 읽음, 문자열로 반환
file = open("test.txt", 'r') # rt도 가능함 ## 파일명에 경로도 가능함
s = file.read()             # readline(), readlines() 도 있음
print(s)
file.close()

# readline():  한 줄씩 순차적으로 반환 ,str형태로 반환 \ while을 사용해야함
with open("test.txt", 'r') as f:
    line = None         # 변수 line을 초기화
    while line != '':
        line = f.readline()
        print(line.strip("\n")) ## or print(line, end = ()) 줄바꿈이 2번 일어나는 걸 방지한다
"""
또는 for 문을 사용해서 실행해도 가능하다

with open("test.txt", 'r') as f:
    for line in f:
        print(line.strip("\n")) 
"""


# readlines(): 문자열이 아니라 한줄씩 리스트 형태로 반환
with open("test.txt", 'r') as f:
    lines = f.readlines()
    print(lines)


# with문
with open("test.txt", "rt") as file:
    s = file.read()
    print(s)
# print(file.read()) 밖에서 사용하면 오류가 발생한다. ValueError: I/O operator does not used

# 파일 반복문
with open("test.txt", "w") as file:
    for i in range(3):
        file.write("Hello World! {0}\n".format(i))


# 문자열 파일에 쓰기
lines = ["hi!\n", "python\n", "coding\n"]

with open("test.txt", "w", encoding= "utf8") as f: # 한국어로 쓰면 파일이 깨질 수 있으니 utf8로 인코딩 해준다.
    f.writelines(lines)

# # -*- coding: utf-8 -*- 이거를 사용하면 가능