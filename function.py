"""
  종류
  1. 매개변수가 필요한 함수
  2. 매개변수가 필요하지 않는 함수
  3. 결과값을 반환하는 함수
  4. 결과값을 반환하지 않는 함수
"""

def f1(a, b):
  print('f1 호출', a, b)

def f2():
  print('f2 호출', )  

def f3():
  print('f3 호출')

def f4(a, b):
  return "라면 먹고 갈래?"

# 실행
f1("라면", "먹고싶다")
f2()
f3()
ret = f4("착한", "생각") 
print(ret)

"""
  a. 다중 리턴
  b. *args, **kwargs
  c. 함수 표현식
  d. 람다 함수
"""
# 다중 리턴
def rets_mul_func():
  y1 = 10; y2 = 20; y3 = 30
  return y1, y2, y3
  # return (y1, y2, y3)
  # return [y1, y2, y3]

z1, z2, z3 = rets_mul_func()
print(z1, z2, z3)

# *args(언패킹)
def args_func(*args):
  for i, v in enumerate(args):
    print('Result : {idx}'.format(idx=i), v)
    
args_func('Lee', 'Park')

# **kwargs(언패킹)
def kwargs_func(**kwargs):
  for v in kwargs.keys():
    print('{}'.format(v), kwargs[v])
    
kwargs_func(name1='Lee', name2='Park')

# 람다식
lam_mul_func = lambda x,y: x*y

print(lam_mul_func(10, 50))

def mul_func(x, y):
  return x * y

print(mul_func(10, 50))
