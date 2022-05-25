# 예외처리 테스트
from typing import final


def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def mul(x, y):
    return x*y


def div(x, y):
    return x/y  # 문제 발생


print('테스트 시작')
(x, y) = (4, 1)
print(f'더하기 {x} + {y} = {add(x, y)}')
print(f'빼기   {x} - {y} = {sub(x, y)}')
print(f'곱하기 {x} * {y} = {mul(x, y)}')
try:
    print(f'나누기 {x} / {y} = {div(x, y)}')
    print(17+3)
    print(int('4.0'))
except ZeroDivisionError as ex:  # ZeroDivisionError에 대한 예외처리
    print('제수에 0을 넣지 마세요', ex)
except TypeError as ex:
    print('문자열과 수를 + 연산으로 더할 수 없습니다.', ex)
except ValueError as ex:
    print('값 에러가 났습니다.', ex)
except Exception as ex:
    print('예외가 발생햇습니다.', ex)
finally:  # 예외가 났단 안 났든 무조건 냄, 없어도 됨, ex)파일을 안 닫고 에러가 났을때 무조건 파일을 닫을 수 있도록 함.
    print('예외가 발생한 구간을 지나갔습니다.')
print('계산기 종료')
