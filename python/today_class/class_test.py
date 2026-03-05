class Person:
    def __init__(self, name, age, address):
        self.hello = "Hello"
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다. '.format(self.hello, self.name))

james = Person('마리아', 20, '서울시 서초구')
james.greeting()

print('이름: ', james.name)
print('나이: ', james.age)
print('주소: ', james.address)

"""
접근 제한자
- 파이썬은 자바나 C++처럼 명시적으로 public, protected, private와 같은 키워드를 사용하지 않는 대신 밑줄(_) 를 사용해서 접근제한을 구분한다.
- 밑줄이 없는 경우 public처럼 객체 생성 후 누구나 외부에서 직접 접근이 가능하다.
- 밑줄이 하나인 경우 비공개모드로서 직접적인 접근을 제한하고 있고 객체 생성 후 외부에서 직접적인 접근을 해서는 안된다. 하지만 접근을 시도하면 오류없이 접근은 가능하다.
- 밑줄이 두개인 경우는 객체 생성 후 외부에서 직접적인 접근을 할 수 없으며 객체 생성 후 직접 접근을 시도하면 정의되지 않은 속성이나 메소드 라고 오류 메시지가 발생한다.
- 밑줄이 두개인 경우 객체 내부에서는 접근이 가능하며 자식 틀래스에세 상속도지 않는다. 
"""

class Person:
    def __init__(self, name, age, address, wallet):
        self.hello = "Hello"
        self._name = name
        self._age = age
        self._address = address
        self.__wallet = wallet

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def get_wallet(self):
        return self.__wallet
    def set_wallet(self, wallet):
        self.__wallet = wallet

    name=property(get_name, set_name)
    age = property(get_age, set_age)
    address = property(get_address, set_address)
    wallet = property(get_wallet, set_wallet)

    def pay(self, amount):
        self.__wallet -= amount
        print("이제 {0}원 남았음".format(self.__wallet))

if __name__ == '__main__':
    james = Person('마리아', 20, '서울시 서초구', 10000)
    print(james.name)
    james.name = "anan"
    print(james.name)
    james.pay(100)