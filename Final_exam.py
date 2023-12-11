#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20201921 이름 : 황규희

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target):
   # 제한사항 확인
    if not (1 <= len(my_string) <= 100 and all(char.islower() for char in my_string) and
            1 <= len(target) <= 100 and all(char.islower() for char in target)):
        return 0 
    # 부분 문자열 찾기
    return 1 if my_string.find(target) != -1 else 0

    
#test
my_string = "catdog"
target1 = "cat"
target2 = "abc"

print(solution(my_string, target1))
print(solution(my_string, target2)) 

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    # 공백 기준 리스트
    morsecode = letter.split(' ')
    answer = ''
    # 모스부호 변환
    for list in morsecode:
        if list in morse:
            answer += morse[list]

    return answer


#test
#letter = amor fati
letter = ".- -- --- .-. / ..-. .- - .."
print(solution(letter))


# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    answer = ''
    # 나이 문자열로 변환
    for num in str(age):
        # 아스키 코드에 해당하는 문자로 변환
        answer += chr(ord('a') + int(num))
    
    return answer

#test
print(solution(857))
print(solution(23))


# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution(r1, r2):
    answer = 0

    # 범위 생성, 좌표 확인
    for x in range(-r2, r2 + 1):
        for y in range(-r2, r2 + 1):
            # 원의 방정식 사용 좌표 조건 충족 확인
            if x**2 + y**2 >= r1**2 and x**2 + y**2 <= r2**2 and x % 1 == 0 and y % 1 == 0:
                answer += 1

    return answer

#test
print(solution(2, 4))
print(solution(1, 3))



# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

from functools import cmp_to_key

# 비교 함수
def compare(x, y):
    return int(str(x) + str(y)) - int(str(y) + str(x))

# 정렬
def solution(numbers):
    list = sorted(numbers, key=cmp_to_key(compare), reverse=True)
    
    # 이어붙임
    answer = ''.join(map(str, list))
    
    # 0인지 확인
    return answer if int(answer) != 0 else '0'

# test
numbers = [8, 30, 17, 2, 23]
print(solution(numbers))  