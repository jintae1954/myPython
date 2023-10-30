"""
  OOP
    - self
    - 인스턴스 메소드
    - 인스턴스 속성
    
  클래스와 인스턴스 차이를 이해하자.
  네임스페이스는 객체를 인스턴스화 할 때 저장된 공간이다.
  
  클래스 속성: 직접 접근 가능
  인스턴스 속성: 각각마다 별도 존재
"""

#1 e.g.
"""class Dog:
  # 클래스 속성
  species = 'first_dog'
  
  # 인스턴스 속성
  def __init__(self, name, age):
    self.name = name
    self.age = age
    

a = Dog("mikky", 2)
b = Dog("milkiss", 3)

# 네임스페이스
print('a', a.__dict__)
print('b', b.__dict__)

# 인스턴스 속성 확인
print('{} : {} and {} : {}'.format(a.name, a.age, b.name, b.age))

# 클래스 속성
if a.species == 'first_dog':
  print('{0} : {1}'.format(a.name, a.species))
  
print(Dog.species)
print(a.species)
print(b.species)"""

#2 e.g.
# self의 이해
"""class SelfTest:
  def func1():
    print('func1 called')
    
  def func2(self):
    print(id(self))
    print('func2 called')

    
f = SelfTest()

# print(dir(f))

print(id(f))
# f.func1()
f.func2()

SelfTest.func1()
# SelfTest.func2()
SelfTest.func2(f)"""

#3 e.g.
"""class Warehouse:
  fare = 1
  
  def __init__(self, owner_name) -> None:
    self.owner_name = owner_name
    Warehouse.fare += 1
    
  def __del__(self):
    Warehouse.fare -= 1
    
    
w1 = Warehouse('kimchi'); print(Warehouse.fare)
w2 = Warehouse('rice'); print(Warehouse.fare)

print(w1.__dict__)
print(w2.__dict__)
print(Warehouse.__dict__)

del w2
print(Warehouse.fare)"""

#4 e.g.
class Cat:  
    def __init__(self, name, age):
      self.name = name
      self.age = age
      
    def info(self):
      print(self.name, self.age)
      
    def meaw(self):
      if self.age <= 2:
        print("{} sounds like {}".format(self.name, 'meaw meaw'))
      else:
        print("{} sounds like {}".format(self.name, 'MEAW MEAW'))


nabi = Cat('nabi', 2)
bina = Cat('bina', 4)
nabi.info()
nabi.meaw()

bina.info()
bina.meaw()
