"""
  input 사용법
    기본 타입: str
"""

# e.g.
name = input("Enter Your Name: ")
print(name)

# 형변환 e.g.
num1 = int(input("Enter Your Int: "))
num2 = float(input("Enter Your Float: "))
print(num1, num2)

"""
  input 사용법
    - 예외 처리
"""

# ex1)
try: 
  n = int(input('Enter Your Number: '))
  print('Your Number is: ', n)
except ValueError:
  print('This is not a number!!')
  
# ex2)
while True:
  try: 
    n = int(input('Enter Your Number: '))
    break
  except ValueError:
    print('This is not a number!!')

print('Your Number is: ', n)