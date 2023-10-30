"""
  SyntaxError, TypeError, NameError,
  IndexError, ValueError, KeyError, ...

  코드 실행 프로세스에서 발생하는 예외도 중요
    1. 예외는 반드시 코드로 처리해야 한다.
    2. 로그는 반드시 남긴다.
    3. 예외는 던져진다.
    4. 예외는 무시할 수 있다.
"""

# SyntaxError
# ...

# NameError: 참조가 없을 때 발생
"""a = 10
b = 15
print(c)"""

# ZeroDivisionError  분모가 0인 경우 발생

# KeyError: 존재하지 않는 Key를 접근할 때 발생, dict에서 주로 발생

# 예외가 없다고 가정하고 프로그램을 작성하라. 런타임 예외 발생 시에 예외 처리를 권장 
# by. EAFP문서

# AttributeError: 모듈, 클래스에 없는 속성을 사용했을 때 발생

# ValueError: 어떤 시퀀스형 자료형에서 접근하고자 하는 데이터가 존재하지 않을 때 발생

# FileNotFoundError: 현재 찾고자 하는 파일이 없을 때 발생

# TypeError: 자료형에 맞지 않는 연산을 수행할 경우 발생

# 예외처리
"""
  try
  except 에러명1
  except 에러명2
"""

names = ['kim', 'park', 'lee']

try:
  z = 'cho'
  x = names.index(z)
except Exception as e:
  print(e)
  print('Not found >>>', Exception.__name__)
else:
  print('ok..')
finally:
  print('it is finally >>>')